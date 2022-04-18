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
            
        answer = "{:,.2f}".format(sum_terms/num_terms)
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
            
        return "{:,.2f}".format(median)
        
        
    
    
    





if __name__ == "__main__":
    #data = pds.read_csv(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")

    #df = pds.DataFrame(data)

    #test = data['SUMLEV']
    
    start = Sum_statistics(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")
    print(start.median('ESTIMATESBASE2020'))