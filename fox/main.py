
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        tiger = AbstractAnimal()
        shark = AbstractAnimal()

        tiger.inputs = [ ("Lion", "Chordata", "Mammalia", "Carnivora", "Felidae", "Panthera tigris", "<img src='http://images.nationalgeographic.com/wpf/media-live/photos/000/007/cache/siberian-tiger_707_600x450.jpg' />", "<embed height='50' width='100' src='audio/lion.mp3'>")]
        #stiger.inputs = [1,2,3,4,5]
        self.response.write(tiger.print_all())
        shark.inputs = [ ("Shark", "Chordata", "Chondrichthyes", "Pristiophoiformes ", "Lamnidae", "Isurus oxyrinchus", "<img src='http://2.bp.blogspot.com/-1acB83dcmAk/UK2X6orz4LI/AAAAAAAACDs/L_5a6wcYwxA/s1600/Silvertip+Sharks2.jpg' />", "<embed height='50' width='100' src='audio/lion.mp3'>")]
        self.response.write(shark.print_all())






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

        self.close = '''

        </body>
        </html>
        '''

        '''
        self.links =
        <a href="?golfer=marisa">Marisa</a>
        <a href="?golfer=walker">Walker</a>
        <a href="?golfer=pinky">Pinky</a>
        <a href="?golfer=alan">Alan</a>
        <a href="?golfer=scott">Scott</a>
        '''



    def print_all(self):

         self.all = self.head + self.body + self.links + self.close
         return self.all



class AbstractAnimal(Page):
    def __init__(self):
        Page.__init__(self)



        self.Title = ""
        self.Phylum = ""
        self.Class = ""
        self.Order = ""
        self.Family = ""
        self.Genus = ""
        self.Image = ""
        self.Avg = ""
        self.Geo = ""
        self.Sound = ""



        self.__inputs = []




    @property
    def inputs(self):
        pass
    @inputs.setter
    def inputs(self,arr):
        self.__inputs = arr
        for item in arr:
             self.Title = "<h1>" + item[0] + "</h1>"
             self.Phylum =  "<li>" + item[1] + "</li>"
             self.Class = "<li>" + item[2] + "</li>"
             self.Order = "<li>" + item[3] + "</li>"
             self.Family = "<li>" + item[4] + "</li>"
             self.Genus = "<li>" + item[5] + "</li>"
             self.Image = "<div>" + item[6] + "</div>"
             self.Sound = "<div>" + item[7] + "</div>"

    



    def print_all(self):
        self.all = self.head + self.body + self.Title + self.ul_open + self.Phylum + self.Class + self.Order + self.Family + self.Genus  + self.ul_close + self.Image +  self.Sound + self.close

        return self.all




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
