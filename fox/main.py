
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Animal()


        self.response.write(p.print_all())







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

        self.close = '''

        </body>
        </html>
        '''

        self.links = '''
        <a href="?golfer=marisa">Marisa</a>
        <a href="?golfer=walker">Walker</a>
        <a href="?golfer=pinky">Pinky</a>
        <a href="?golfer=alan">Alan</a>
        <a href="?golfer=scott">Scott</a>
        '''
    def print_all(self):

         self.all = self.head + self.body + self.links + self.close
         return self.all



class Animal(object):
    def __init__(self):
        #Page.__init__(self)

        self.__info = []
        '''
        self.Phylum = ""
        self.Class = ""
        self.Order = ""
        self.Family = ""
        self.Genus = ""
        self.Image = ""
        self.Avg = ""
        self.Geo = ""
        '''

    @property
    def info(self,arr):
        self.__info = arr

        for item in arr:
            print item















'''
    @property
    def scoring_average(self):
        return self.__scoring_average

#first setter to change the scoring average if the user wants
    @scoring_average.setter
    def scoring_average

#funct to calculate the average of the 5 rounds of golf
    def calc_score(self):
        self.__scoring_average = (self.round1 + self.round2 + self.round3 + self.round4 + self.round5)/5
        return self.__scoring_average
'''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
