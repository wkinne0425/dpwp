
import webapp2

class MainHandler(webapp2.RequestHandler):

    page = Page()
    


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

    def print_all(self):

         self.all = self.head + self.body + self.links + self.close
         return self.all

 class Golf(object):
    def __init__(self):
            self.round1 = 0
            self.round2 = 0
            self.round3 = 0
            self.round4 = 0
            self.round5 = 0
            self.__scoring_average = 0


    @property
    def scoring_average(self):
        return self.__scoring_average

    @scoring_average.setter
    def scoring_average(self, new_scoring_average):
        self.__scoring_average = new_scoring_average

     def calc_score(self):
        self.__scoring_average = (self.round1 + self.round2 + self.round3 + self.round4 + self.round5)/5
        return self.__scoring_average


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
