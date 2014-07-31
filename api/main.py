
import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        url = DisplayHeadlines()




        if  self.request.GET and self.request.GET["ticker"] == "":


            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write("Must fill in this field")
            self.response.write(page.print_close())
        elif self.request.GET and self.request.GET["ticker"]:
            url.ticker = self.request.GET["ticker"]
            self.response.write(page.print_results_open())
            self.response.write(url.display())
            self.response.write(page.print_close())



        else:
            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write(page.print_close())
















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
                    "<h3>Please use the field below to enter you ticker</h3>"
        self.ul_close = "</ul>"
        self.container_open = "<div class='cont'>"
        self.container_close = "</div>"

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

         self.open = self.head + self.body + self.main
         return self.open

    def print_results_open(self):

         self.open = self.head + self.body
         return self.open

    def print_close(self):
        return self.html_close


#This class creates and displays all the info
class Ticker(object):
    def __init__(self):
        self.url = "http://finance.yahoo.com/rss/headline?s="
        self.ticker = ""



    '''
    def return_url(self):

        self.final = self.url + self.ticker

        return self.final

'''
    def display(self):
        #return self.xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
        self.final = self.url + self.ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)
        #print self.final

        return self.xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue

    def return_url(self):
        self.final = self.url + self.ticker
        return self.final


class DisplayHeadlines(Ticker):
    def __init__(self):
        Ticker.__init__(self)

    def display(self):
        self.final = self.url + self.ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)
        self.header_1 = "<h1>" + self.xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue + "</h1>"
        self.link_1 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[2].firstChild.nodeValue + ">" + "Link To Story" + "</a>"

        self.header_2 = "<h1>" + self.xmldoc.getElementsByTagName('title')[3].firstChild.nodeValue + "</h1>"
        self.link_2 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[3].firstChild.nodeValue + ">" + "Link To Story" + "</a>"

        self.header_3 = "<h1>" + self.xmldoc.getElementsByTagName('title')[4].firstChild.nodeValue + "</h1>"
        self.link_3 = "<a href=" +  self.xmldoc.getElementsByTagName('link')[4].firstChild.nodeValue + ">" + "Link To Story" + "</a>"

        return self.header_1 + self.link_1 + self.header_2 + self.link_2 + self.header_3 + self.link_3 + "<a href='http://localhost:12080'>Home</a>"







'''
    @property
    def ticker(self):
        pass
    #Sets all the data and also loops the array
    @ticker.setter
    def ticker(self):
        pass
  '''












app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
