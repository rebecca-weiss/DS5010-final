# US_Census_Analyzer

Authors:
Rebecca Weiss, Jacob Dengler, Matthew Quaglia, Ruben Lema, Sanjay Kanakaraj

## Purpose

The purpose of US_Census_Analyzer is to statistically analyze and visually present data based on the US census.

Data: https://www.census.gov/data/datasets/time-series/demo/popest/2020s-national-total.html 

## Organization

The package is divided into three classes as well as additional functions. 

The class round_slicing is used to round numerical data, slice the data frame into various categories, and return data on specific regions, states, and cities.

The class sum_statistics is used to find various statistical values of the entire data frame, inlcuding national mean, median, standard devation, etc.

The class combination_statistics has many similar function. However, this function takes in lists of specified combinations of state names and will output the statistical values for these unique combinations. 

Additionally, various functions are available to visually display the data in the form of maps and charts. 

## Examples of Use



## 1. Install dependencies 
pip install -r requirements.txt
