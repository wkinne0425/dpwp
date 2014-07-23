
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):


        if self.request.GET:
            page = Page()
            self.response.write(page.print_all())
        else: self.response.write("It worked")




        #set the attributes for the first golfer
        w = Golf()
        w.round1 = 81
        w.round2 = 77
        w.round3 = 85
        w.round4 = 83
        w.round5 = 75

        w.scoring_average = 90
        w.calc_score()


#set the attributes for the second golfer
        m = Golf()
        m.round1 = 65
        m.round2 = 71
        m.round3 = 80
        m.round4 = 68
        m.round5 = 70

        m.calc_score()

        p  = Golf()
        p.round1 = 76
        p.round2 = 71
        p.round3 = 85
        p.round4 = 78
        p.round5 = 79

        #p.calc_score()


        d  = Golf()
        d.round1 = 66
        d.round2 = 78
        d.round3 = 59
        d.round4 = 87
        d.round5 = 90

        #d.calc_score()


        a  = Golf()
        a.round1 = 90
        a.round2 = 67
        a.round3 = 85
        a.round4 = 90
        a.round5 = 106

        #a.calc_score()





class Page(object):
    def __init__(self):
        self.head = '''
        <!DOCTYPE>
            <html>
            <head>
            <title></title>
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









#created a class of golf that will eventually grab the average of 5 rounds of golf

class Golf(object):
    def __init__(self):
            self.round1 = 0
            self.round2 = 0
            self.round3 = 0
            self.round4 = 0
            self.round5 = 0
            self.__scoring_average = 0
#add 5 rounds of golf and also a private scoring average attr


#first getter to grab the scoring average
    @property
    def scoring_average(self):
        return self.__scoring_average

#first setter to change the scoring average if the user wants
    @scoring_average.setter
    def scoring_average(self, new_scoring_average):
        self.__scoring_average = new_scoring_average

#funct to calculate the average of the 5 rounds of golf
    def calc_score(self):
        self.__scoring_average = (self.round1 + self.round2 + self.round3 + self.round4 + self.round5)/5
        print self.__scoring_average



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
