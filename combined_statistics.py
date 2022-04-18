import pandas as pds
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class combined_statistics:

	df = pds.read_csv("data/NST-EST2021-alldata.csv")


	def combined_mean(self, x, column_name):
		specifieddf = df[df.Name.isin(x)]
		values = list(specifieddf[column_name])

		for value in values:
			sum_terms += value
			num_terms += 1

		answer = sum_terms/num_terms
		return answer

	def combined_median(self, x, column_name):
		specifieddf = df[df.Name.isin(x)]
		values = list(specifieddf[column_name])

		if len(values) % 2 == 0:
            first = values[len(values) // 2]
            second = values[len(values) // 2 - 1]
            median = (first + second)/2
        else:
            median = values[len(values) // 2]
            
        return median

    def combined_minimum(self, x, column_name):
    	specifieddf = df[df.Name.isin(x)]
		values = list(specifieddf[column_name])

		min_value = min(values)
		return min_value

	def combined_maximum(self, x, column_name):
		specifieddf = df[df.Name.isin(x)]
		values = list(specifieddf[column_name])

		max_value = max(values)
		return max_value

	def combined_range_func(self, x, column_name):
		min_value = int(self.combined_minimum(x, column_name))
		max_value = int(self.combined_maximum(x, column, name))

		range_ = max_value - min_value

		return range_ 

	def combined_stand_dev(self, x, column_name):
		specifieddf = df[df.Name.isin(x)]
		values = list(specifieddf[column_name])

		mean = self.combined_mean(x, column_name)
		pop_size = len(values)

		sum_for_values = 0
		for value in values:
			sum_for_values += (value - mean) ** 2

		standard_dev = (sum_for_values / pop_size) ** .5

		return standard_dev


	def combined_summary(self, x, column_name):
		mean = self.combined_mean(x, column_name)
		median = self.combined_median(x, column_name)
		minimum = self.combined_minimum(x, column_name)
		maximum = self.combined_maximum(x, column_name)
		range_ = self.combined_range_func(x, column_name)
		standard_dev = self.combined_stand_dev(x, column_name)

		string = "Mean: {:,.2f}".format(mean) + \
           "\nMedian: {:,.2f}".format(median) + \
               "\nMinimum: {:,.2f}".format(minimum) + \
                   "\nMaximum: {:,.2f}".format(maximum) + \
                       "\nRange: {:,.2f}".format(range_) + \
                           "\nStandard Deviation: {:,.2f}".format(standard_dev)
        
        return string