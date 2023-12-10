# Stock Recommender
By: Jack Shangold and Alec Leyva

<img src = "https://i.insider.com/649afce86eb0a800194d541f?width=1136&format=jpeg" align = "right" width="120" height="178">

The big idea from our project came from a discussion between our two team members. Alec is a finance major at Babson College and Jack is a passionate stock follower and shareholder. We wanted to create something that could compare hundreds of stocks against eachother faster than any human could. We also wanted the ability to add our own paramters, so a stock would be returned based on specific recomendations. The three parameters are the initial investment amount, your risk safety, and the amount of days you will hold the asset for. The program will take all the historical data from valid stocks from the S&P500 and put them into a dictionary. Then, a linear regression model is done for all added stocks. Valid stocks are stocks that have enough recent information to conduct the  linear regression model. Based on the inputted information, the user will be given a stock that best fits the needed criteria. The code also connects to a flask website, for a more personalized feel. We really wanted to make the program feel like a search engine, and so we added the html to it. The only downside is because it does do hundreds of regression models, it takes quite a bit of time to load. Please be patient!

# Installation
[Click here to go to page](https://github.com/aleyva1/finalproject.git)
The code can be downloaded here. Please install everything in the project folder. It should be one python file named app.py and two HTML files named index.html and result.html respectively. 


# Dependencies
1. 'flask'
2. 'bs4'
3. 'requests'
4. 'yfinance'
5. 'pandas'
6. 'sklearn.linear_model'
7. 'numpy'




## Authors

- [Alec Leyva](https://github.com/aleyva1)
- [Jack Shangold](https://github.com/JShangold1)
