"""
Created on Tue Apr 26 11:27:21 2022

@author: Ruben
"""
import pandas as pd
from round_slicingV2 import Basic_clean
from sum_statisticV2 import Sum_statistics
from combined_statisticsV2 import Combined_statistics
from census_bargraphs_piecharts import Vis_Census


def main() :
    # Test Round slicing file, by creating a dataframe from each method
    bc = Basic_clean("data/co-est2021-alldata.csv", "data/NST-EST2021-alldata.csv")
    aggregated_regions = bc.aggregated_regions()
    regions = bc.regions("West")
    aggregated_states = bc.aggregated_states()
    states = bc.state_cities("Alabama")
    city = bc.city("New York", "New York")
    
    # Test Sum_Statistics with DataFrame
    ss = Sum_statistics(aggregated_regions)
    # the summary method calls all other methods in class, excluding graph
    print(ss.summary('ESTIMATESBASE2020'))
    
    ss = Sum_statistics(regions)
    print(ss.summary('ESTIMATESBASE2020'))
    
    # Test Combines_statistics with DataFrame
    # Note Combined statistics, is only to compare states and cities
    cs = Combined_statistics(aggregated_states)
    # the combined_summary method calls all other methods in class, comparison method
    print(cs.combined_summary(['Alaska', 'Alabama','Arkansas'], 'NAME', 'BIRTHS2020'))
    print(cs.comparison('Massachusetts', 'New York', 'NAME', 'ESTIMATESBASE2020'))
    
    cs = Combined_statistics(states)
    print(cs.combined_summary(['Choctaw County', 'Cleburne County','Cullman County'], 'CTYNAME', 'BIRTHS2020'))
    print(cs.comparison('Choctaw County', 'Cleburne County', 'CTYNAME', 'ESTIMATESBASE2020'))

    # We test the visualizations with Aggregated States 
    data = Vis_Census(aggregated_states)
    data.compare_bar_graph('NAME', 'ESTIMATESBASE2020','POPESTIMATE2021')
    data.bar_graph('NAME', 'ESTIMATESBASE2020')
    data.pie_chart('NAME', 'ESTIMATESBASE2020')

    # We test the visualizations with Aggregated Regions
    data = Vis_Census(aggregated_regions)
    data.compare_bar_graph('NAME', 'ESTIMATESBASE2020','POPESTIMATE2021')
    data.bar_graph('NAME', 'ESTIMATESBASE2020')
    data.pie_chart('NAME', 'ESTIMATESBASE2020')
    
    # We test the visualizations with A specific States and its cities
    states = bc.state_cities("Delaware")
    data = Vis_Census(states)
    data.bar_graph('CTYNAME', 'ESTIMATESBASE2020')
    data.bar_graph('CTYNAME', 'ESTIMATESBASE2020')
    data.pie_chart('CTYNAME', 'ESTIMATESBASE2020')
    
if __name__ == "__main__":
    main()