
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        w = Golf()
        w.round1 = 80
        w.round2 = 70
        w.round3 = 85
        w.round4 = 90
        w.round5 = 100

        m = Golf()
        m.round1 = 80
        m.round2 = 77
        m.round3 = 88
        m.round4 = 98
        m.round5 = 65

        p = Golf()
        p.round1 = 76
        p.round2 = 70
        p.round3 = 108
        p.round4 = 95
        p.round5 = 68

        s = Golf()
        s.round1 = 89
        s.round2 = 72
        s.round3 = 99
        s.round4 = 95
        s.round5 = 100

        a = Golf()
        a.round1 = 71
        a.round2 = 72
        a.round3 = 66
        a.round4 = 95
        a.round5 = 80



#Conditional that knows when a link is clicked and what to display
        if (self.request.GET and self.request.GET['golfer'] == 'walker'):
            self.response.write(page.head + page.body + str(w.calc_score()) + page.close)
        elif (self.request.GET and self.request.GET['golfer'] == 'marisa'):
            self.response.write(m.calc_score())
        elif (self.request.GET and self.request.GET['golfer'] == 'pinky'):
            self.response.write(p.calc_score())
        elif (self.request.GET and self.request.GET['golfer'] == 'scott'):
            self.response.write(s.calc_score())
        elif (self.request.GET and self.request.GET['golfer'] == 'alan'):
            self.response.write(a.calc_score())
        else: self.response.write(page.print_all())






#HTML class that handles all of the viusal aspects
class Page(object):
    def __init__(self):
        self.head = '''
        <!DOCTYPE>
            <html>
            <head>
            <title></title>
            <link rel="stylesheet" href="css/main.css" />
            <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
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

        self.links = '''
        <a href="?golfer=marisa">Marisa<img src="img/golf.jpg" /></a>

        <a href="?golfer=walker">Walker<img src="img/golf.jpg" /></a>
        <a href="?golfer=pinky">Pinky<img src="img/golf.jpg" /></a>
        <a href="?golfer=alan">Alan<img src="img/golf.jpg" /></a>
        <a href="?golfer=scott">Scott<img src="img/golf.jpg" /></a>
        '''
    def print_all(self):

         self.all = self.head + self.body + self.links + self.close
         return self.all





#Class that takes all the rounds in and runs the calculate function to get the average
class Golf(object):
    def __init__(self):
            self.round1 = 0
            self.round2 = 0
            self.round3 = 0
            self.round4 = 0
            self.round5 = 0
            self.__scoring_average = 0



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
        return self.__scoring_average



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
