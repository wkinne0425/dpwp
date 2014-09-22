
import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):

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

class DisplayHeadlines(Ticker):
    def __init__(self):
        Ticker.__init__(self)

    def display(self):
        self.final = self.url + self.ticker
        self.request = urllib2.Request(self.final)
        self.opener = urllib2.build_opener()
        self.result = self.opener.open(self.request)
        self.xmldoc = minidom.parse(self.result)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
