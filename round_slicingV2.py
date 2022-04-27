import pandas as pd 

class Basic_clean:
    def __init__(self, data, aggregated_data):
        # encoding = "ISO-8859-1" was added to solve for error 'utf-8' codec can't decode byte 0xf1 in position 107223: invalid continuation byte
        self.data = pd.read_csv(data, encoding = "ISO-8859-1")
        self.aggregated_data = pd.read_csv(aggregated_data)
        self.states_ = ['Alaska', 'Alabama','Arkansas', 'Arizona','California',\
'Colorado', 'Connecticut', 'District of Columbia', 'Delaware', 'Florida',\
'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky',\
'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri',\
    'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire',\
'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico',\
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia',\
'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
        
    def aggregated_regions(self):
        return self.aggregated_data.iloc[1:5]
    
    def regions(self, which_region):
        #which_region = input('Which Region? A: Northeast Region B: Midwest Region \
#\nC: South Region D: West Region  E: All Regions \n')
        if which_region == 'Northeast':
            Northeast_reg = self.data.loc[self.data['REGION'] == 1]
            return Northeast_reg
        elif which_region == 'Midwest':
            Midwest_reg = self.data.loc[self.data['REGION'] == 2]
            return Midwest_reg
        elif which_region == 'South':
            South_reg = self.data.loc[self.data['REGION'] == 3]
            return South_reg
        elif which_region == 'West':
            West_reg = self.data.loc[self.data['REGION'] == 4]
            return West_reg
        elif which_region == 'All':
            return self.data 

    def aggregated_states(self):
        ''' This method requires aggregated data file & returns all states
        '''
        return self.aggregated_data.iloc[5:]
        
    
    def state_cities(self, which_state):
        '''This method returns a specific stated, with all of its cities / counties
        '''
        #which_state = input('Which State? ')
        if which_state in self.states_:
            state = self.data.loc[self.data['STNAME'] == which_state]
            return state
        else:
            return "Invalid input, please try again"

    def city(self, which_state, which_city):
        state = self.state_cities(which_state)
        #which_city = input('Which City or County? ')
        city = state.loc[state['CTYNAME'] == which_city]
        
        if city.empty:
            return "Invalid input, please try again"
        else:
            return city
    
if __name__ == "__main__":
    # Start class to initiate DataFrame
    start = Basic_clean("data/co-est2021-alldata.csv", "data/NST-EST2021-alldata.csv")
    # Call section of Dataframe Region, states or Cities
    #region_df = start.regions()
    #agg_states = start.aggregated_states()
    
    #calling sum_statistics 
    #ss = Sum_statistics(region_df)
    #print(ss.summary('ESTIMATESBASE2020'))
    
    #ss_states = Sum_statistics(agg_states)
    #print(ss_states.summary('ESTIMATESBASE2020'))
    
    print(start.all_agg_states())
