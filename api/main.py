
import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        url = DisplayHeadlines()




        if self.request.GET:
            url.ticker = self.request.GET["ticker"]
            request = urllib2.Request(url.return_url())
            opener = urllib2.build_opener()
            result = opener.open(request)
            xmldoc = minidom.parse(result)

            self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue)
            self.response.write(url.return_url())
            self.response.write(page.print_close())
        else:
            self.response.write(page.print_open())
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
            </head>
            <body>
        '''
        self.body = '''



        '''

        self.ul_open = "<ul>"
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





    def print_open(self):

         self.open = self.head + self.body
         return self.open

    def print_close(self):
        return self.html_close


#This class creates and displays all the info
class Ticker(object):
    def __init__(self):
        self.url = "http://finance.yahoo.com/rss/headline?s="
        self.ticker = ""
        self.final = ""



    def return_url(self):

        self.final = self.url + self.ticker

        return self.final



class DisplayHeadlines(Ticker):
    def __init__(self):
        Ticker.__init__(self)





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
