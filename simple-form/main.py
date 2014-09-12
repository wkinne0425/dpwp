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
            <h1>Calculate Your Auto Loan</h1>
               <form method="GET" action="">
               <label>Car: </label><input type="text" name="car" />
               <label>Year: </label><input type="text" name="year" />
               <label>Cost of Car: </label><input type="text" name="loan" />

               <div id="buttons">
               <h3>Choose your credit:</h3>

               <label>Excellent </label><input type="radio" name="radio_button" value="excellent">
               <label>Good</label><input type="radio" name="radio_button" value="good">
               <label>Fair</label><input type="radio" name="radio_button" value="fair">
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
#function that does all the magic
        def calc():

            #begining attributes
            interest = 0
            year = self.request.GET['year']
            loan_amount = self.request.GET['loan']
            loan_number = int(loan_amount)
            car = self.request.GET['car']
            #sets interest rate according to selections
            if self.request.GET['radio_button'] == 'excellent':
                interest = 3
                #self.response.write(interest)

            elif self.request.GET['radio_button'] == 'good':
                interest = 5
                #self.response.write(interest)

            else:
                interest = 8
                #self.response.write(interest)
        #starts finding the total amount of interest by multiplying loan by interest then divide by 100
            total_interest = (loan_number * interest)
            number = int(total_interest)
            final_interest = number / 100.0
            final_interest_str = str(final_interest)

            #finds total loan amount after interest
            total_loan = loan_number + final_interest
            total_loan_str = str(total_loan)


            term = self.request.GET['length']
            term_number = int(term)

            monthly = total_loan / term_number / 12.0
            monthly_str = str(monthly)

            #self.response.write(monthly)







            self.response.write("here are your loan terms for your " + year + car + "<br />" )
            self.response.write("Loan Amount: " + "$" + loan_amount + "<br />")
            self.response.write("Interest Amount: " + "$" + final_interest_str + "<br />")
            self.response.write("Total Loan: " + "$" + total_loan_str + "<br />")
            self.response.write("Monthy Payments: " + "$" + monthly_str)







        if self.request.GET:
            calc()
        else:
            self.response.write(head + body + footer)



app = webapp2.WSGIApplication([
    ('/', MainHandler)])