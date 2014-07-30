
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        page = Page()
        tiger = Tiger()
        shark = Shark()
        bird = Bird()


        tiger.inputs = [ "Lion", "Chordata", "Mammalia", "Carnivora", "Felidae", "Panthera tigris", "<img src='http://images.nationalgeographic.com/wpf/media-live/photos/000/007/cache/siberian-tiger_707_600x450.jpg' />", "<embed height='50' width='100' src='audio/lion.mp3'>", "<a href='?sound=lion'>Lion</a>", "10 - 14 Years", "Africa"]
        #stiger.inputs = [1,2,3,4,5]
        #self.response.write(tiger.print_all())
        shark.inputs = ["Shark", "Chordata", "Chondrichthyes", "Pristiophoiformes ", "Lamnidae", "Isurus oxyrinchus", "<img src='http://2.bp.blogspot.com/-1acB83dcmAk/UK2X6orz4LI/AAAAAAAACDs/L_5a6wcYwxA/s1600/Silvertip+Sharks2.jpg' />", "<embed height='50' width='100' src='audio/jaw_theme.mp3'>", "<a href='?sound=shark'>Shark</a>", "20 - 30 years", "Ocean"]
        #self.response.write(shark.print_all())
        bird.inputs = ["Bird", "Chordata", "Aves", "Passeriformes ", "Turdidae", "Turdus", "<img src='http://astromatrix.org/Content/images/Objects/Bird.jpg' />", "<embed height='50' width='100' src='audio/birds002.mp3'>", "<a href='?sound=bird'>Bird</a>", "50 - 80 Years", "Trees"]

        self.response.write(page.print_all())
'''
#conditional statement that checks url and displays accordingly
        if (self.request.GET and self.request.GET['sound'] == 'shark'):
            self.response.write(tiger.open() + shark.print_all() + shark.play() +  tiger.html_close)
        elif (self.request.GET and self.request.GET['sound'] == 'lion'):
            self.response.write(tiger.open() + tiger.print_all() + tiger.play() +  tiger.html_close)
        elif (self.request.GET and self.request.GET['sound'] == 'bird'):
            self.response.write(tiger.open() + bird.print_all() + bird.play() +  tiger.html_close)
        else: self.response.write(tiger.open() + tiger.print_all() + shark.print_all() + bird.print_all() +  tiger.html_close )
'''

#This creates all the page attributes for the html
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
        self.container_open = "<div class='cont'>"
        self.container_close = "</div>"

        self.html_close = '''

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

         self.all = self.head + self.body +  self.html_close
         return self.all


#This class creates and displays all the info
class AbstractAnimal(object):
    def __init__(self):
        #inherites the Page class



        #all the attributes needed
        self.title = ""
        self.phylum = ""
        self.a_class = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.image = ""
        self.avg = ""
        self.geo = ""
        self.sound = ""
        self.link = ""



        #stores all the data in a array
        self.__inputs = []




    @property
    def inputs(self):
        pass
    #Sets all the data and also loops the array
    @inputs.setter
    def inputs(self,arr):
        self.__inputs = arr


        self.title = "<h1>" + arr[0] + "</h1>"
        self.phylum =  "<li> Phylum: " + arr[1] + "</li>"
        self.a_class = "<li> Class: " + arr[2] + "</li>"
        self.order = "<li> Order: " + arr[3] + "</li>"
        self.family = "<li> Family: " + arr[4] + "</li>"
        self.genus = "<li> Genus: " + arr[5] + "</li>"
        self.avg = "<li>Average Life: " + arr[9] + "</li>"
        self.habitat = "<li> Habitat: " + arr[10] + "</li>"
        self.image = "<div>" + arr[6] + "</div>"
        self.sound = "<div>" + arr[7] + "</div>"
        self.link = arr[8]



#opens html
    def open(self):
        return self.head
#closes html
    def close(self):
        return self.html_close
#prints everything inside htmlMee
    def print_all(self):
        self.all = self.container_open +  self.Title + self.ul_open + self.Phylum + self.Class + self.Order + self.Family + self.Genus + self.Avg + self.Habitat  + self.ul_close + self.Image  + self.Link + self.container_close

        return self.all
#plays the sound for each bird
    def play(self):
        return self.sound


class Tiger(AbstractAnimal):
     def __init__(self):
        AbstractAnimal.__init__(self)

     def play(self):
         self.sound = "This is a tiger sound"
         return self.sound

class Shark(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)

    def play(self):
        self.sound = "This is a Shark sound"
        return self.sound

class Bird(AbstractAnimal):

    def __init__(self):
        AbstractAnimal.__init__(self)

    def play(self):
        self.sound = "This is a Bird sound"
        return self.sound


#I DID IT!!

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
