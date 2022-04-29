# US_Census_Visualizer

Authors:
Rebecca Weiss, Jacob Dengler, Matthew Quaglia, Ruben Lema, Sanjay Kanakaraj

## Purpose

The purpose of US_Census_Analyzer is to statistically analyze and visually present data based on the US census.

Data: https://www.census.gov/data/datasets/time-series/demo/popest/2020s-national-total.html 

## Organization

The package is divided into four classes as well as additional functions. 

The class round_slicing is used to round numerical data, slice the data frame into various categories, and return data on specific regions, states, and cities.

The class sum_statistics is used to find various statistical values of the entire data frame, inlcuding national mean, median, standard devation, etc.

The class combination_statistics has many similar function. However, this function takes in lists of specified combinations of state names and will output the statistical values for these unique combinations. 

The class census_bargraphs_piecharts allows users to insert specific column names to view the locational data in either bar graphs or pie charts, also incorporating a comparison bar graph for more than one variable of interest

Additional functions include mapviz and map_usa_heat, both offer a users view US census data directly on a model map of the US. The function scrape_FIPS will makes a map color-coded to values of interest. On the other hand, map_usa_heat shows a color scale for open-ended values. Both functions help the user visualize the variable of their choice for a clear view of how it looks mapped onto a model. 

Overall, the various functions and class are available to visually display the data in the form of maps and charts. 

## Examples of Use



## 1. Install dependencies 
pip install -r requirements.txt
