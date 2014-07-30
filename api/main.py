
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        url = DisplayHeadline()

        self.response.write(url.return_url())

        url.ticker = "yhoo"







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

        self.html_close = '''

        </body>
        </html>
        '''





    def print_all(self):

         self.all = self.head + self.body +  self.html_close
         return self.all


#This class creates and displays all the info
class DisplayHeadline(object):
    def __init__(self):
        self.url = "http://finance.yahoo.com/rss/headline?s="
        self.__ticker = ""
    def return_url(self):
        self.final = self.url + self.__ticker
        return self.final





    @property
    def ticker(self):
        pass
    #Sets all the data and also loops the array
    @ticker.setter
    def ticker(self,str):
        self.__ticker = str
        print str











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
