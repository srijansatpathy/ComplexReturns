# PythonProject
PIC 16A Group 3 Project

## Project Name:

## Group Members:
  Anshul Vinayak  
  Srijan Satpathy  
  Petra Portabella Jarosilova  

## Project Description:
In our project, we will analyze the correlation between the language used by corporate executives and the relative stock returns of their companies. Our hypothesis is that clear and concise language relates to larger returns. To construct this cross-association, we will use quarterly earnings calls for our repository of executive speech patterns, and we will use the Gunning-Fox algorithm to rank their complexity. 

## Instructions on how to install the package requirements:
To install the spacy library run the following code in your command line:
>pip install -U spacy
  
To install the spacy_syllables library run the following code in your command line:
>pip install spacy_syllables
  
To download the pipeline package en_code_web_sm run the following code in your command line:
>import spacy
>spacy.cli.download("en_core_web_sm")
  

## Scope and limitations:
Our main project limitation is that we only analyze each company for the month of January 2019. It would be interesting to see how language complexity changes over time and how that compares to returns over time. 

## License and terms of use: 
MIT License

## References and acknowledgement:
Spacy reference: https://realpython.com/natural-language-processing-spacy-python/

## Tutorials used: 
https://realpython.com/natural-language-processing-spacy-python/: This tutorial was used to download spacy library as well as models and data for the English language. Beyond the downloading process the project is different to the tutorial because it implemenents the tokenization of words to determine the complexity of words. More specifically, our project specifically looks at if the token (word) has 3 or more syllables, ends in "ing", ends in "ed', ends in "es", and if it is a proper noun to determine whether it is considered a complex word accounding to the Gunning Fog Index criteria. Additionally, our project creates a Gunning Fog function that returns a Gunning Fog Index (which is not in the tutorial). 
