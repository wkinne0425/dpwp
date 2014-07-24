
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        a = Animal()
        #a.info =[ ['why'], ['wont'], ['this'], ['work'] ]

        a.list_all()

        self.response.write(a.print_all())







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



class Animal(Page):
    def __init__(self):
        Page.__init__(self)

        self.testing = [ ['0'], ['1'], ['2']]


        self.Phylum = ""
        self.Class = ""
        self.Order = ""
        self.Family = ""
        self.Genus = ""
        self.Image = ""
        self.Avg = ""
        self.Geo = ""


        self.test = ''

    def list_all(self):
        for item in self.testing:
         print item[0]




'''
    @property
    def info(self):
        pass

    @info.setter
    def info(self,arr):
        self.__info = arr

        for item in arr:

            self.Phylum = item[0]
            self.Class = item[1]
            self.Order = item[2]

            print self.Phylum + self.Class + self.Order

            print item[1]
'''















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
