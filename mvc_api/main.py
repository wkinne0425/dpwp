import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = StockView()
        s = StockController()

        #if statement that validates the input field is not emplty and displays proper info according to ticker

        if  self.request.GET and self.request.GET["ticker"] == "":
            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write("Must fill in this field")
            self.response.write(page.print_close())
        elif self.request.GET and self.request.GET["ticker"]:
            s.ticker = self.request.GET["ticker"]
            self.response.write(page.print_results_open())
            self.response.write("<h1 class='blue'>Top 3 results for " + s.ticker + "</h1>")
            self.response.write(s.displayInfo())
            self.response.write(page.print_close())
        else:
            self.response.write(page.print_full_open())
            self.response.write(page.input)
            self.response.write(page.print_close())




#This creates all the page attributes for the html
class StockView(object):
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
class StockModel(object):
    def __init__(self):
#Attributes that hold data for proper url
        self.url = "http://finance.yahoo.com/rss/headline?s="
        self.ticker = ""





#This class inherits from Ticker
class StockController(StockModel):
    def __init__(self):
        StockModel.__init__(self)
#This takes the url and ticker, adds them together and then parses the xml document
    def displayInfo(self):
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
