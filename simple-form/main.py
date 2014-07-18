


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
         head = '''
        <!doctype html>

        <html lang="en">
        <head>
            <meta charset="utf-8">

        <title>Simple Form</title>
          <meta name="description" content="The HTML5 Herald">
          <meta name="author" content="SitePoint">
          <link rel="stylesheet" href="css/main.css" />


















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)