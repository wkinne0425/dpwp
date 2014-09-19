
import webapp2

class MainHandler(webapp2.RequestHandler):

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
            <h1>Lets learn how good these players really are!</h1>
            <h3>Click below to reveal each players scoring average for 5 rounds of golf</h3>
        '''
        self.body = '''



        '''

        self.close = '''

        </body>
        </html>
        '''

        self.close = '''

        </body>
        </html>
        '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
