import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #header of the page
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
    #Body of the page
        body = '''

        <body>
            <h1>Calculate your Auto Loan</h1>
               <form method="GET" action="">
               <label>Car: </label><input type="text" name="name" />
               <label>Year: </label><input type="text" name="email" />
               <label>Cost of car: </label><input type="text" name="loan" />

               <div id="buttons">
               <h3>Choose your credit:</h3>

               <input type="radio" name="radio_button" value="excellent">Excellent
               <input type="radio" name="radio_button" value="good">Good
               <input type="radio" name="radio_button" value="fair">Fair
               </div>



               <h3> Choose your terms: </h3>
               <select name="length"><option value="15">15yr</option><option value="30">30yr</option></select>


               <input class="button" type="submit" value="Submit" />
               </form>
               '''

        footer = '''
        <footer></footer>
        </body>
        </html>

                '''

        self.response.write(head + body + footer)



app = webapp2.WSGIApplication([
    ('/', MainHandler)])