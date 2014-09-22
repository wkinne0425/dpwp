
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


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
