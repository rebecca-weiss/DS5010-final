import pandas as pd 
import matplotlib.pyplot as plt
from sum_statisticV2 import Sum_statistics

class Basic_clean:
    def __init__(self, data):
        # encoding = "ISO-8859-1" was added to solve for error 'utf-8' codec can't decode byte 0xf1 in position 107223: invalid continuation byte
        self.data = pd.read_csv(data, encoding = "ISO-8859-1")
        self.states_ = ['Alaska', 'Alabama','Arkansas', 'Arizona','California',\
'Colorado', 'Connecticut', 'District of Columbia', 'Delaware', 'Florida',\
'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky',\
'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri',\
    'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire',\
'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',\
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia',\
'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
        
    def regions(self):
        which_region = input('Which Region? A: Northeast Region B: Midwest Region \
\nC: South Region D: West Region  E: All Regions \n')
        if len(which_region) > 1:
            return "Invalid input, please try again"
        else:
            if which_region.upper() == 'A':
                Northeast_reg = self.data.loc[self.data['REGION'] == 1]
                return Northeast_reg
            elif which_region.upper() == 'B':
                Midwest_reg = self.data.loc[self.data['REGION'] == 2]
                return Midwest_reg
            elif which_region.upper() == 'C':
                South_reg = self.data.loc[self.data['REGION'] == 3]
                return South_reg
            elif which_region.upper() == 'D':
                West_reg = self.data.loc[self.data['REGION'] == 4]
                return West_reg
            elif which_region.upper() == 'E':
                return self.data 
    
    def states(self):
        which_state = input('Which State? ')
        if which_state in self.states_:
            state = self.data.loc[self.data['STNAME'] == which_state]
            return state
        else:
            return "Invalid input, please try again"
        
    def city(self):
        state = self.states()
        which_city = input('Which City or County? ')
        city = state.loc[state['CTYNAME'] == which_city]
        
        if city.empty:
            return "Invalid input, please try again"
        else:
            return city
    
def main():
    # Start class to initiate DataFrame
    start = Basic_clean("data/co-est2021-alldata.csv")
    # Call section of Dataframe Region, states or Cities
    region_df = start.regions()
    
    #calling sum_statistics 
    ss = Sum_statistics(region_df)
    ss.region_graph('STNAME', 'ESTIMATESBASE2020')
    
main()