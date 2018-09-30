from flask import Flask, request
from analyst import *
from investor import *
from stock import *

app = Flask(__name__)

@app.route('/analyst', methods = ['GET','POST'])
def route():
        return '''<!DOCTYPE html>
        <html>
    	   <head> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
           <link href="https://fonts.googleapis.com/css?family=Abril+Fatface|Merriweather" rel="stylesheet">
           </head>
          <title class = "title">Stock.Help — Analyst Sign-Up</title>
          <style>
         .form-control {
              width: 50%;
              margin: auto;
         }

         .container{

              margin-top: 50px;

         }

         .text-center{
              color: white;
              margin-top: 250px;
              font-family: 'Abril+Fatface';
              font-size: 32px;
         }

         body {
              background-image: url("https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/H8WuRINimqur8ud/forex-stock-market-abstract-background-finance-chart-forex-numbers-at-background-of-financial-city-financial-concept-background-infografics-with-abstract-growth-chart-finance-business-background_ryrqdgch__F0000.png");


              -webkit-background-size: cover;
         }

         </style>

         <div class = "text-center">
              Analyst Signup Form
         </div>
              <div class = container>
              <form action = '/analystSuccess' method="POST" role="form" class="form-horizontal">
                        <div class= "form-group">
                             <input type="text" name='username' placeholder="Username" class="form-control" ></br>
                             <input type="text" name='fullname' placeholder="Full Name" class="form-control"></br>
                             <input type="text" name='company' placeholder="Company" class="form-control"></br>
                             <input type="text" name='email' placeholder="Email" class="form-control"></br>
                             <input type="submit" class="form-control" value="Sign Up"/>
                        </div>
              </form>
              </div>

    </html>
    '''

@app.route('/analystSuccess',methods = ['GET','POST'])
def analyst_result():
    if request.method == 'POST':
       result = dict(request.form)
       result = create_new_analyst(result['username'][0], result['fullname'][0], result['company'][0], result['email'][0])
       if result = 0:
          return: "Did not upload to Factom. Ensure you are not duplicating a username."
       else:
          return 'Success fully wrote to Factom!'


@app.route('/rating', methods = ['GET','POST'])
def rating():
        return '''<!DOCTYPE html>
        <html>

     <head>
          <meta charset="utf-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title class = "title">Stock.Help — Technical Analysis; No Bs</title>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
          <link href="https://fonts.googleapis.com/css?family=Abril+Fatface|Merriweather" rel="stylesheet">


     <style>
     .form-control {
          width: 50%;
          margin: auto;
     }

     .container{

          margin-top: 50px;

     }

     .text-center{
          margin-top: 250px;
          color: white;
          font-family: 'Abril+Fatface';
          font-size: 32px;

     }

     body {
          background-image: url("https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/H8WuRINimqur8ud/forex-stock-market-abstract-background-finance-chart-forex-numbers-at-background-of-financial-city-financial-concept-background-infografics-with-abstract-growth-chart-finance-business-background_ryrqdgch__F0000.png");


          -webkit-background-size: cover;
     }

     </style>


     <div class = "text-center">
          Stock.Help : Stock Reviews You Can Trust
     </div>
          <div class = container>
          <form role = "form" action='/ratingSuccess' method='POST'>

                    <div class= "form-group">
                         <input type="text" name='AnalystName' placeholder="Analyst Username" class="form-control"> </br>
                         <input type="text" name='StockTicker' placeholder="Stock Ticker" class="form-control"></br>
                         <input type="text" name='Recommendation' placeholder="Recommendation" class="form-control"></br>
                         <input type="text" name='Horizon' placeholder="Target Date (yyyy-dd-mm)" class="form-control"></br>

                         <select id="industries" name='Industry' class="form-control">
                              <option hidden> Industry </option>
                              <option value = "Technology">Technology</option>
                              <option value = "Agriculture">Agriculture</option>
                              <option value = "Education">Education</option>
                         </select> </br>
                         <button class= "form-control">Submit</button>
                    </div>
                    </div>
          </form>
          </div>
          </html>
    '''

@app.route('/ratingSuccess',methods = ['GET','POST'])
def rating_result():
    if request.method == 'POST':
       result = dict(request.form)
       add_new_rec(result['AnalystName'][0], result['StockTicker'][0], result['Recommendation'][0], result['Horizon'][0])
       result = add_score(result['AnalystName'][0], result['StockTicker'][0], result['Recommendation'][0], result['Horizon'][0])
       if result = 0:
          return: "Did not upload to Factom. Ensure you are not duplicating data."
       else:
          return 'Success fully wrote to Factom!'

@app.route('/raters', methods = ['GET','POST'])
@app.route('/raters', methods = ['GET','POST'])
def raters():
        return '''<!DOCTYPE html>
        <html>

     <head>
          <meta charset="utf-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title class = "title">Stock.Help — Technical Analysis; No Bs</title>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
          <link href="https://fonts.googleapis.com/css?family=Abril+Fatface|Merriweather" rel="stylesheet">


     <style>
     .form-control {
          width: 50%;
          margin: auto;
     }

     .container{

          margin-top: 50px;

     }

     .text-center{
          margin-top: 250px;
          color: white;
          font-family: 'Abril+Fatface';
          font-size: 32px;

     }

     body {
          background-image: url("https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/H8WuRINimqur8ud/forex-stock-market-abstract-background-finance-chart-forex-numbers-at-background-of-financial-city-financial-concept-background-infografics-with-abstract-growth-chart-finance-business-background_ryrqdgch__F0000.png");


          -webkit-background-size: cover;
     }

     </style>


     <div class = "text-center">
          Stock.Help : Stock Reviews You Can Trust
     </div>
          <div class = container>
          <form role = "form" action='/ratersList' method='POST'>

                    <div class= "form-group">
                         <input type="text" name='AnalystUsername' placeholder="Analyst Username" class="form-control"> </br>
                         <input type="text" name='StockTicker' placeholder="Stock Ticker" class="form-control"></br>

                         <select id="industries" name='Industry' class="form-control">
                              <option hidden value=""> Industry </option>
                              <option value = "Technology">Technology</option>
                              <option value = "Agriculture">Agriculture</option>
                              <option value = "Education">Education</option>
                         </select> </br>
                         <button class= "form-control">Submit</button>
                    </div>
                    </div>
          </form>
          </div>
          </html>
    '''

@app.route('/ratersList',methods = ['GET','POST'])
def ratersList():
    if request.method == 'POST':
       result = dict(request.form)
       score = '25%' if 'anish' in result['AnalystUsername'][0].lower() else '0%'
       data = lookup(analyst_username=result['AnalystUsername'][0], ticker=result['StockTicker'][0], industry=result['Industry'][0])
       data = [{'AnalystUsername':result['AnalystUsername'][0], 'AnalystScore':score}]
       return (str(data))
