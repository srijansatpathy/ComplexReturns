# PythonProject
PIC 16A Group 3 Project

## Project Name:

## Group Members:
  Anshul Vinayak  
  Srijan Satpathy  
  Petra Portabella Jarosilova  

## Project Description:
In our project, we will analyze the correlation between the language used by corporate executives and the relative stock returns of their companies. Our hypothesis is that clear and concise language relates to larger returns. To construct this cross-association, we will use quarterly earnings calls for our repository of executive speech patterns, and we will use the Gunning-Fog algorithm to rank their complexity. 

## Instructions on how to install the package requirements:
To install the spacy library run the following code in your command line:
>pip install -U spacy
  
To install the spacy_syllables library run the following code in your command line:
>pip install spacy_syllables
  
To download the pipeline package en_code_web_sm run the following code in your command line:
>import spacy
>spacy.cli.download("en_core_web_sm")


To install the yahoo_fin library run the following code in your command line:

>pip install yahoo_fin

To install the yfiannce library run the following code in your command line:

>pip install yfinance --upgrade --no-cache-dir

## Description of the demo file:
Once you have installed and downloaded the requirements you can run the demo file called Complexity.ipynb in the PythonProject folder by running the whole notebook.
At the output of this demo file should be the following two figures:
### Figure 1:
<img width="383" alt="Screen Shot 2022-03-16 at 3 31 03 PM" src="https://user-images.githubusercontent.com/97066940/158702483-03fd795b-0cb7-42a8-a82d-284068ac2d76.png">

### Figure 2:
<img width="424" alt="Screen Shot 2022-03-16 at 3 30 53 PM" src="https://user-images.githubusercontent.com/97066940/158702505-ac0bfd91-df4e-4a79-9f5e-9f128bf752ba.png">

Figure 1 is a scatter plot of the Gunning-Fog Index and the 2019 Q1 returns. Each dot on the plot is representative of one company that we looked at. As we can see there is not a very clear correlation that is visible by the naked eye. However, we added the correlation coefficient (-0.32) on top of the figure, which is indicative to a weak negative correlation.
To further investigate this correlation, we decided to plot a regression line on the scatter plot as we can see in Figure 2. Again, we see that the regression line is sloped downwards, indicating a negative correlation. 
Our results weakly show that the more complex the language is in earning calls the less returns we would expect from the given company.

## Scope and limitations:
Our main project limitation was the time it took to scrape the relevant data for each company, and as such we were only able analyze each company for the first quarter of 2019. It would be interesting to see how language complexity changes over time and how that compares to returns over time.

Another limitation was a potential bias in the source of the initial dataset, which was scraped from lists of companies that currently exist in 2022. As such, we had a ’survivor bias,’ as companies that failed or were delisted were not included in our sample. Furthermore considering the stock price volatility between 2020-2022, we decided to test each company in the year 2019. Another future project would be to find complete company data from a past year, and then run our tests in that same year.

## License and terms of use: 
MIT License

## References and acknowledgement:
Spacy reference: https://realpython.com/natural-language-processing-spacy-python/

yahoo_fin reference: http://theautomatic.net/yahoo_fin-documentation/

yfinance reference: https://algotrading101.com/learn/yfinance-guide/

## Background and source of the dataset:

We scraped the initial list of tickers using the following methods from yahoo_fin’s stock_info module: tickers_dow(), tickers_other(), tickers_ftse100(), tickers_nasdaq(), tickers_niftybank(), tickers_ftse250(), tickers_ibovespa(), tickers_nifty50(), and tickers_sp500(). This provided all tickers that existed at the date of request (3/1/22).

From this initial list of ~12000 tickers, we first removed all non-equities to get a list of ~6000 companies, and we secondly removed companies that did not exist past the date 1/1/18 for a final list of ~4000 companies.

Due to technical limitations, we opted to choose a random sample of 50 tickers (and later trimmed to 13) from this final list to use in our project. This random sample and their relevant price histories are in the file ‘data.csv’.

The files 'ticker_shares,' 'tickers_2018,' and 'tickers_used' are all additional pickle data files but not needed/referenced in our demo 'Complexity.ipynb'.  

## Tutorials used: 
https://realpython.com/natural-language-processing-spacy-python/: This tutorial was used to download spacy library as well as models and data for the English language. Beyond the downloading process the project is different to the tutorial because it implemenents the tokenization of words to determine the complexity of words. More specifically, our project specifically looks at if the token (word) has 3 or more syllables, ends in "ing", ends in "ed', ends in "es", and if it is a proper noun to determine whether it is considered a complex word accounding to the Gunning-Fog Index criteria. Additionally, our project creates a Gunning-Fog function that returns a Gunning-Fog Index (which is not in the tutorial). 
