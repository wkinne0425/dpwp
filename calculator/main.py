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
        w = Golf()
        w.round1 = 81
        w.round2 = 77
        w.round3 = 85
        w.round4 = 83
        w.round5 = 75
        w.scoring_average = 90
        #w.calc_score()

        self.response.write(str(w.scoring_average) + "<br />")

        m = Golf()
        m.round1 = 65
        m.round2 = 71
        m.round3 = 80
        m.round4 = 68
        m.round5 = 70

        m.calc_score()

        self.response.write(m.scoring_average)








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



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
