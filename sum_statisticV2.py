import pandas as pds
import matplotlib.pyplot as plt

class Sum_statistics:
    '''This is the class to summarize the data'''
    
    def __init__(self, data_location):
        '''The data should be a dataframe'''
        self.data = data_location
        
        
    def mean(self, column_name):
        values = list(self.data[column_name])

        sum_terms = 0
        num_terms = 0 
        
        for value in values:
            sum_terms += value
            num_terms += 1
            
        answer = sum_terms/num_terms
        return answer
    
    def median(self, column_name):
        values = list(self.data[column_name])
        
        if len(values) % 2 == 0:
            first = values[len(values) // 2]
            second = values[len(values) // 2 - 1]
            median = (first + second)/2
        else:
            median = values[len(values) // 2]
            
        return median
        
    def minimum(self, column_name):
        values = list(self.data[column_name])
        min_value = min(values)
        return min_value
    
    def maximum(self, column_name):
        values = list(self.data[column_name])
        max_value = max(values)
        return max_value
    
    def range_func(self, column_name):
        min_value = int(self.minimum(column_name))
        max_value = int(self.maximum(column_name))
        
        range_ = max_value - min_value
        
        return range_
    
    def stand_dev(self, column_name):
        values = list(self.data[column_name])
        mean = self.mean(column_name)
        pop_size = len(values)
        
        sum_for_values = 0
        for value in values:
            sum_for_values += (value - mean) ** 2
            
        standard_dev = (sum_for_values / pop_size) ** .5
        
        return standard_dev
    
    def summary(self, column_name):
        mean = self.mean(column_name)
        median = self.median(column_name)
        minimum = self.minimum(column_name)
        maximum = self.maximum(column_name)
        range_ = self.range_func(column_name)
        standard_dev = self.stand_dev(column_name)
        
        string = "Mean: {:,.2f}".format(mean) + \
            "\nMedian: {:,.2f}".format(median) + \
                "\nMinimum: {:,.2f}".format(minimum) + \
                    "\nMaximum: {:,.2f}".format(maximum) + \
                        "\nRange: {:,.2f}".format(range_) + \
                            "\nStandard Deviation: {:,.2f}".format(standard_dev)
        
        return string
        
    def region_graph(self, column_name, column_values):
        
        bargraph = self.data.plot(x = column_name, y = column_values)
        return bargraph
        '''values = list(self.data[column_name])
        label = list(self.data[region_name])
        
        names = label[1:5]
        pop_value = values[1:5]
 
        plt.bar(names, pop_value, color ='maroon',
                width = 0.4)
                
        plt.title('Population Density & Summary Statistics\n\n',
        		fontweight ="bold")
        plt.figtext(1,0.5, start.summary('ESTIMATESBASE2020') )
        
        plt.show()
'''




if __name__ == "__main__":
    #data = pds.read_csv(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")

    #df = pds.DataFrame(data)

    #test = data['SUMLEV']
    
    start = Sum_statistics(r"C:\Users\Ruben\Documents\NEU\DS5010\Project\DS5010-final\data\NST-EST2021-popchg2020_2021.csv")
    print(start.mean('ESTIMATESBASE2020'))
    print(start.median('ESTIMATESBASE2020'))
    print(start.minimum('ESTIMATESBASE2020'))
    print(start.maximum('ESTIMATESBASE2020'))
    print(start.range_func('ESTIMATESBASE2020'))
    print(start.stand_dev('ESTIMATESBASE2020'))
    print(start.summary('ESTIMATESBASE2020'))
    start.region_graph('POPESTIMATE2021', 'NAME')

