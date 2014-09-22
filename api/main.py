
import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
