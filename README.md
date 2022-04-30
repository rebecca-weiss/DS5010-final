# US_Census_Visualizer
## Authors: Rebecca Weiss, Jacob Dengler, Matthew Quaglia, Ruben Lema, Sanjay Kanakaraj

![US Population 2021](https://github.com/rebecca-weiss/DS5010-final/blob/main/output/2021population_map.png)


## Purpose
The purpose of US_Census_Analyzer is to statistically analyze and visually present data based on the US census.

Data can be found at https://www.census.gov/data/datasets/time-series/demo/popest/2020s-national-total.html 

## Organization
```.gitignore
README.md
__init__.py
census_bargraphs_piecharts.py
combined_statisticsV2.py
data
   |-- CO-EST2021-ALLDATA.pdf
   |-- NST-EST2021-ALLDATA.pdf
   |-- NST-EST2021-POPCHG2020-2021.pdf
   |-- NST-EST2021-alldata.csv
   |-- NST-EST2021-popchg2020_2021.csv
   |-- co-est2021-alldata.csv
main.py
mapviz.py
output
   |-- 2021population_map.png
requirements.txt
round_slicingV2.py
sum_statisticV2.py
```

The package is divided into four classes as well as additional functions. 

The `class round_slicing` is used to round numerical data, slice the data frame into various categories, and return data on specific regions, states, and cities.

The `class sum_statistics` is used to find various statistical values of the entire data frame, inlcuding national mean, median, standard devation, etc.

The class `combination_statistics` has many similar function. However, this function takes in lists of specified combinations of state names and will output the statistical values for these unique combinations. 

The class `census_bargraphs_piecharts` allows users to insert specific column names to view the locational data in either bar graphs or pie charts, also incorporating a comparison bar graph for more than one variable of interest

Additional functions include `mapviz` and `map_usa_heat`, both offer a users view US census data directly on a model map of the US. The function `map_usa` will makes a map color-coded to values of interest. On the other hand, `map_usa_heat` shows a color scale for open-ended values. Both functions help the user visualize the variable of their choice for a clear view of how it looks mapped onto a model. 

Overall, the various functions and class are available to visually display the data in the form of maps and charts. 

## Examples of Use

1. Finding the average estimated population of the United States of America for 2020. 
2. Showing a HeatMap of the birthrate of the United States of America in 2020.
3. Comparing the average Birthrate between the North and South both numerically and through a comparison bargraph 


To install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

