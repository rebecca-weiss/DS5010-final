import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

#Hey guys I am making more functions right now so I can compute everything called data_converter_region and data_converter_state
#Note I am adding a location atttachment to the the csv file for my sake to make my code run a little easier


class Vis_Census:
	'''This is the class to visualize the data with Scatter Plot, Bar Graphs, Histograms, and Pie Charts'''

	def __init__(self, data):
		self.data = dataframe

	def bar_graph(self, column_name): 

		labels = self.data['location']

		x = self.data['lables']
		y = self.data["column_name"]

		fig, ax = plt.subplots()

		ax.bar(x,y, width = 1, edgecolor = 'white', linewidth =.7)
		plt.xticks(range(len(x)), x, rotation='vertical')


		plt.xlabel('location') #from x
		plt.ylabel('column_name') #from y

		plt.show()

	def compare_bar_graph(self, column_name, column_name2):

		barWidth = 0.25
		fig = plt.subplots(figsize =(12, 8))
 
		input_1 = self.data["column_name"]
		input_2 = self.data["column_name2"]

		br1 = np.arange(len(input_1))
		br2 = [x + barWidth for x in br1]
 
		plt.bar(br1, input_1, width = barWidth, label ='column_name')
		plt.bar(br2, input_2, width = barWidth, label ='column_name2')

		labels = self.data['location']

		plt.xlabel("lables")
		plt.ylabel('Number of People')
		plt.xticks([r + barWidth for r in range(len(input_1))],
		["lablesa"])
		plt.legend()
		plt.show()

	def pie_chart(self, column_name):

		x = self.data[column_name]
		lables = self.data['location']
	
		fig, ax = plt.subplots()
	
		ax.pie(x, labels=lables,autopct='%.1f%%', radius=2, center=(5, 5),
			wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)

		plt.show()


if __name__ == "__main__":

	dataframe = data_converter_region("data/co-est2021-alldata.csv")
	print(dataframe.pie_chart('ESTIMATESBASE2020'))
	print(dataframe.compare_bar_graph('ESTIMATESBASE2020','POPESTIMATE2021'))
	dataframe = data_converter_state("data/co-est2021-alldata.csv")
	print(dataframe.bar_graph('ESTIMATESBASE2020'))