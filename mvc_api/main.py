
import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        url = DisplayHeadlines()
        sm = StockModel()
        sm.zip = self.request.GET and self.request.GET["ticker"]


        #if statement that validates the input field is not emplty and displays proper info according to ticker

        if  self.request.GET and self.request.GET["ticker"] == "":
            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write("Must fill in this field")
            self.response.write(page.print_close())
        elif self.request.GET and self.request.GET["ticker"]:
            url.ticker = self.request.GET["ticker"]
            self.response.write(page.print_results_open())
            self.response.write("<h1 class='blue'>Top 3 results for " + url.ticker + "</h1>")
            self.response.write(url.display())
            self.response.write(page.print_close())
        else:
            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write(page.print_close())


class StockModel(object):
    """ This fetches and sorts through api data"""

    def __init__(self):
        self.__url = "http://finance.yahoo.com/rss/headline?s="
        self.__ticker = ''

    def callApi(self):
        self.final = self.__url + self.__ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)



    @property
    def ticker(self):
        pass

    @ticker.setter
    def ticker(self, t):
        self.__ticker = t






  #This creates all the page attributes for the html
class Page(object):
    def __init__(self):
        self.head = '''
        <!DOCTYPE>
            <html>
            <head>
            <title></title>
            <link rel="stylesheet" href="css/main.css" />
            <link href='http://fonts.googleapis.com/css?family=Rajdhani' rel='stylesheet' type='text/css'>
            </head>
            <body>
        '''
        self.body = '''



        '''

        self.main = "<h1>Get your finance headlines</h1>" \
                    "<h3>Please use the field below to enter you ticker</h3>" \
                    "<p>&quot;You must enter a correct ticker or an error will appear&quot;</p>"
        self.ul_close = "</ul>"
        self.container_open = "<div class='cont'>"
        self.container_close = "</div>"
        self.main_container_open = "<div class='main_cont'>"
        self.main_container_close = "</div>"
        self.input = '''
        <form method="GET" action="">
        <label>Ticker: </label><input type="text" name="ticker" />
        <input class="button" type="submit" value="Submit" />
               </form>
        '''

        self.html_close = '''

        </body>
        </html>
        '''





    def print_full_open(self):

         self.open = self.head + self.body + self.main_container_open + self.container_open + self.main
         return self.open

    def print_results_open(self):

         self.open = self.head + self.body
         return self.open

    def print_close(self):
        self.close = self.container_close + self.main_container_close + self.html_close
        return self.close


#This is the Abstract Class
class Ticker(object):
    def __init__(self):
#Attributes that hold data for proper url
        self.url = "http://finance.yahoo.com/rss/headline?s="
        self.ticker = ""
#Method that connects url to one piece and also parse xml
    def display(self):

        self.final = self.url + self.ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)

#This class inherits from Ticker
class DisplayHeadlines(Ticker):
    def __init__(self):
        Ticker.__init__(self)
#POLY at work here. Over riding the method display and adding all the functionality to it
    def display(self):
        self.final = self.url + self.ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)
#displays info from the first title and link
        self.header_1 = "<h3>" + self.xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue + "</h3>"
        self.link_1 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[2].firstChild.nodeValue + ">" + "Link To Story" + "</a>"
#displays info from the second title and link
        self.header_2 = "<h3>" + self.xmldoc.getElementsByTagName('title')[3].firstChild.nodeValue + "</h3>"
        self.link_2 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[3].firstChild.nodeValue + ">" + "Link To Story" + "</a>"
#displays info from the third title and link
        self.header_3 = "<h3>" + self.xmldoc.getElementsByTagName('title')[4].firstChild.nodeValue + "</h3>"
        self.link_3 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[4].firstChild.nodeValue + ">" + "Link To Story" + "</a>"
#returns all information for display
        return self.header_1 + self.link_1 + self.header_2 + self.link_2 + self.header_3 + self.link_3 + "<a class='home' href='http://localhost:12080'>Home</a>"



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
