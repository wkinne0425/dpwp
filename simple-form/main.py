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



        </head>
        '''

    body = '''

        <body>
        <form method="GET" action="">
               <label>Name: </label><input type="text" name="name" />
               <label>Email: </label><input type="text" name="email" />
               <label>Loan Amount: </label><input type="text" name="loan" />

                <div id="buttons">
               <h3>Choose your credit:</h3>

               <input type="radio" name="radio_button" value="excellent">Excellent
               <input type="radio" name="radio_button" value="good">Good
               <input type="radio" name="radio_button" value="fair">Fair
               </div>
               </div>



app = webapp2.WSGIApplication([
    ('/', MainHandler)])