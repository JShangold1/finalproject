# Stock Recommender
# By: Jack Shangold and Alec Leyva

<img src = "https://i.insider.com/649afce86eb0a800194d541f?width=1136&format=jpeg" width="120" height="178">

</b Big Idea>: The big idea from our project came from a discussion between our two team members. Alec is a finance major at Babson College and Jack is a passionate stock follower and shareholder. We wanted to create something that could compare hundreds of stocks against eachother faster than any human could. We also wanted the ability to add our own paramters, so a stock would be returned based on specific recomendations. The three parameters are the initial investment amount, your risk safety, and the amount of days you will hold the asset for. The program will take all the historical data from valid stocks from the S&P500 and put them into a dictionary. Then, a linear regression model is done for all added stocks. Valid stocks are stocks that have enough recent information to conduct the  linear regression model. The code also connects to a flask website, for a more personalized feel. We really wanted to make the program feel like a search engine, and so we added the html to it. The only downside is because it does do hundreds of regression models, it takes quite a bit of time to load. Please be patient!

# Step-By-Step Breakdown
1. 
