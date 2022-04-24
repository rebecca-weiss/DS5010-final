import pandas as pds
import matplotlib.pyplot as plt

class Combined_statistics:
    def __init__(self, data_location):
        self.data = pds.read_csv(("data/NST-EST2021-alldata.csv"))
        
    def combined_mean(self, x, column_name):
        ''' X - is a list, with user unput of States
        '''
        
        # Here we extract the number for data_location for each x 
        values = []
        for state in x:
            first = self.data.loc[self.data['NAME'] == state]
            values.append(first[column_name])
        
        # here we calculate the mean
        
        sum_terms = 0
        num_terms = 0 
        
        for value in values:
            sum_terms += int(value)
            num_terms += 1
            
        answer = sum_terms/num_terms
        return answer
    
    def combined_median(self, x, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data['NAME'] == state]
            values.append(first[column_name])
    
        if len(values) % 2 == 0:
            first = int(values[len(values) // 2])
            second = int(values[len(values) // 2 - 1])
            median = (first + second)/2
        else:
            median = int(values[len(values) // 2])
            
        return median
    
    def combined_minimum(self, x, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data['NAME'] == state]
            values.append(int(first[column_name]))
    
        min_value = min(values)
        return min_value
    
    def combined_maximum(self, x, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data['NAME'] == state]
            values.append(int(first[column_name]))
    
        max_value = max(values)
        return max_value
    
    def combined_range_func(self, x, column_name):
        min_value = int(self.combined_minimum(x, column_name))
        max_value = int(self.combined_maximum(x, column_name))
    
        range_ = max_value - min_value
    
        return range_
    
    def combined_stand_dev(self, x, column_name):
        values = []
        for state in x:
            first = self.data.loc[self.data['NAME'] == state]
            values.append(int(first[column_name]))
    
        mean = self.combined_mean(x, column_name)
        pop_size = len(values)
    
        sum_for_values = 0
        for value in values:
            sum_for_values += (value - mean) ** 2
    
        standard_dev = (sum_for_values / pop_size) ** 0.5
    
        return standard_dev
    
    def combined_summary(self, x, column_name):
        mean = self.combined_mean(x, column_name)
        median = self.combined_median(x, column_name)
        minimum = self.combined_minimum(x, column_name)
        maximum = self.combined_maximum(x, column_name)
        range_ = self.combined_range_func(x, column_name)
        standard_dev = self.combined_stand_dev(x, column_name)
    
        string = (
            "Mean: {:,.2f}".format(mean)
            + "\nMedian: {:,.2f}".format(median)
            + "\nMinimum: {:,.2f}".format(minimum)
            + "\nMaximum: {:,.2f}".format(maximum)
            + "\nRange: {:,.2f}".format(range_)
            + "\nStandard Deviation: {:,.2f}".format(standard_dev)
        )
    
        return string
    
    def comparison(self, x, y, column_name):
        xdf = self.data.loc[self.data['NAME'] == x]
        x_value = xdf[column_name]
        ydf = self.data.loc[self.data['NAME'] == y]
        y_value = ydf[column_name]
    
        if int(x_value) > int(y_value):
            return x
    
        elif int(x_value) < int(y_value):
            return y
    
        elif int(x_value) == int(y_value):
            return "Values are equal"

        
if __name__ == "__main__":
    cs = Combined_statistics("data/NST-EST2021-alldata.csv")
    print(cs.combined_mean(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_median(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_minimum(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020')) 
    print(cs.combined_maximum(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020')) 
    print(cs.combined_range_func(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_stand_dev(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.combined_summary(['Massachusetts', 'Maine', 'New York'], 'ESTIMATESBASE2020'))
    print(cs.comparison('Massachusetts', 'New York', 'ESTIMATESBASE2020'))
    