import pandas as pds
import csv

class Sum_statistics:
    '''This is the class to summarize the data'''
    
    def __init__(self, data_location):
        '''The data should be a dataframe'''
        self.data = pds.read_csv(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")
        
        
    def mean(self, column_name):
        values = list(self.data[column_name])
        values = values[5:]
        sum_terms = 0
        num_terms = 0 
        
        for value in values:
            sum_terms += value
            num_terms += 1
            
        answer = sum_terms/num_terms
        return answer
    
    def median(self, column_name):
        values = list(self.data[column_name])
        values = sorted(values[5:])
        if len(values) % 2 == 0:
            first = values[len(values) // 2]
            second = values[len(values) // 2 - 1]
            median = (first + second)/2
        else:
            median = values[len(values) // 2]
            
        return median
        
    def minimum(self, column_name):
        values = list(self.data[column_name])
        values = sorted(values[5:])
        min_value = min(values)
        return min_value
    
    def maximum(self, column_name):
        values = list(self.data[column_name])
        values = sorted(values[5:])
        max_value = max(values)
        return max_value
    
    def range(self, column_name):
        min_value = int(self.minimum(column_name))
        max_value = int(self.maximum(column_name))
        
        range_ = max_value - min_value
        
        return range_
        
    
    
    





if __name__ == "__main__":
    #data = pds.read_csv(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")

    #df = pds.DataFrame(data)

    #test = data['SUMLEV']
    
    start = Sum_statistics(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")
    print(start.mean('ESTIMATESBASE2020'))
    print(start.median('ESTIMATESBASE2020'))
    print(start.minimum('ESTIMATESBASE2020'))
    print(start.maximum('ESTIMATESBASE2020'))
    print(start.range('ESTIMATESBASE2020'))