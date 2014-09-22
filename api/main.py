
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



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
