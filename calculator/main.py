#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''

        <body>


        </body>



        ''')
#set the attributes for the first golfer
        w = Golf()
        w.round1 = 81
        w.round2 = 77
        w.round3 = 85
        w.round4 = 83
        w.round5 = 75
#tested the setter
        w.scoring_average = 90
        #w.calc_score()

        self.response.write("<div id='test'> " + str(w.scoring_average) + "</div>")
#set the attributes for the second golfer
        m = Golf()
        m.round1 = 65
        m.round2 = 71
        m.round3 = 80
        m.round4 = 68
        m.round5 = 70

        m.calc_score()

        self.response.write("<div id='test'> " + str(m.scoring_average) + "</div>")

        p  = Golf()
        p.round1 = 76
        p.round2 = 71
        p.round3 = 85
        p.round4 = 78
        p.round5 = 79

        p.calc_score()

        self.response.write("<div id='test'> " + str(p.scoring_average) + "</div>")






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



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
