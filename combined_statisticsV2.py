from round_slicingV2 import Basic_clean

class Combined_statistics:
    def __init__(self, data_df):
        '''
        Class takes dataframe to run methods 
        '''
        self.data = data_df
        
    def combined_mean(self, x, cty_state_name, column_name):
        '''
        X - is a list, with user unput of States
        ----------
        x : List 
            X is a list, with user unput of States
        cty_state_name : String
            This is where we input the column name for the States or Cities.
        column_name : String
            Column for which the formulate will run to.

        Returns
        -------
        Combined Mean : Integer
            Returns the mean for the column selected.
        '''
        
        # Here we extract the number for data_location for each x 
        values = []
        for state in x:
            first = self.data.loc[self.data[cty_state_name] == state]
            values.append(first[column_name])
        
        # here we calculate the mean
        
        sum_terms = 0
        num_terms = 0 
        
        for value in values:
            sum_terms += int(value)
            num_terms += 1
            
        answer = sum_terms/num_terms
        return answer
    
    def combined_median(self, x, cty_state_name, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data[cty_state_name] == state]
            values.append(first[column_name])
    
        if len(values) % 2 == 0:
            first = int(values[len(values) // 2])
            second = int(values[len(values) // 2 - 1])
            median = (first + second)/2
        else:
            median = int(values[len(values) // 2])
            
        return median
    
    def combined_minimum(self, x, cty_state_name, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data[cty_state_name] == state]
            values.append(int(first[column_name]))
    
        min_value = min(values)
        return min_value
    
    def combined_maximum(self, x, cty_state_name, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data[cty_state_name] == state]
            values.append(int(first[column_name]))
    
        max_value = max(values)
        return max_value
    
    def combined_range_func(self, x, cty_state_name, column_name):
        min_value = int(self.combined_minimum(x, cty_state_name, column_name))
        max_value = int(self.combined_maximum(x, cty_state_name, column_name))
    
        range_ = max_value - min_value
    
        return range_
    
    def combined_stand_dev(self, x, cty_state_name, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data[cty_state_name] == state]
            values.append(int(first[column_name]))
    
        mean = self.combined_mean(x, cty_state_name, column_name)
        pop_size = len(values)
    
        sum_for_values = 0
        for value in values:
            sum_for_values += (value - mean) ** 2
    
        standard_dev = (sum_for_values / pop_size) ** 0.5
    
        return standard_dev
    
    def combined_summary(self, x, cty_state_name, column_name):
        mean = self.combined_mean(x, cty_state_name, column_name)
        median = self.combined_median(x, cty_state_name, column_name)
        minimum = self.combined_minimum(x, cty_state_name, column_name)
        maximum = self.combined_maximum(x, cty_state_name, column_name)
        range_ = self.combined_range_func(x, cty_state_name, column_name)
        standard_dev = self.combined_stand_dev(x, cty_state_name, column_name)
    
        string = (
            "\nMean: {:,.2f}".format(mean)
            + "\nMedian: {:,.2f}".format(median)
            + "\nMinimum: {:,.2f}".format(minimum)
            + "\nMaximum: {:,.2f}".format(maximum)
            + "\nRange: {:,.2f}".format(range_)
            + "\nStandard Deviation: {:,.2f}".format(standard_dev)
        )
    
        return string
    
    def comparison(self, x, y, cty_state_name, column_name):
        xdf = self.data.loc[self.data[cty_state_name] == x]
        x_value = xdf[column_name]
        ydf = self.data.loc[self.data[cty_state_name] == y]
        y_value = ydf[column_name]
    
        if int(x_value) > int(y_value):
            return "\n" + x
    
        elif int(x_value) < int(y_value):
            return "\n" + y
    
        elif int(x_value) == int(y_value):
            return "\nValues are equal"

        
if __name__ == "__main__":
    '''cs = Combined_statistics("data/NST-EST2021-alldata.csv")
    print(cs.combined_mean(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_median(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_minimum(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020')) 
    print(cs.combined_maximum(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020')) 
    print(cs.combined_range_func(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_stand_dev(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_summary(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.comparison('Massachusetts', 'New York', 'ESTIMATESBASE2020'))'''
    
    df_import = Basic_clean("data/co-est2021-alldata.csv", "data/NST-EST2021-alldata.csv")
    states = df_import.aggregated_states()
    cities = df_import.state_cities()
    cs = Combined_statistics(states)
    print(cs.combined_summary(['Alaska', 'Alabama','Arkansas'], 'NAME', 'BIRTHS2020'))
    
    scities = Combined_statistics(cities)
    print(scities.combined_summary(['Choctaw County', 'Cleburne County','Cullman County'], 'CTYNAME', 'BIRTHS2020'))
    