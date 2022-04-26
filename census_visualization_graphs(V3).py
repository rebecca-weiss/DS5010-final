import matplotlib.pyplot as plt
import numpy as np
import pandas as pds


def data_converter_region(x):
	data = pds.read_csv(x)
	region = data[1:5]

	return(region)


def data_converter_state(x):
	data = pds.read_csv(x)
	state = data[5:]

	return(state)


#x = data_converter_state(r"C:\Users\Ripper.000\Desktop\NST-EST2021-alldata.csv")
#print(x)


class Vis_Census:
	'''This is the class to visualize the data with Bar Graphs and Pie Charts'''

	def __init__(self, data):
		self.data = data

	def bar_graph(self, column_name): 
		labels = self.data['NAME']


		x = self.data['NAME']
		y = self.data["column_name"]

		fig, ax = plt.subplots()

		ax.bar(x,y, width = 1, edgecolor = 'white', linewidth =.7)
		plt.xticks(range(len(x)), x, rotation='vertical')


		plt.xlabel(labels) #from x
		plt.ylabel(y) #from y

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

		labels = self.data['NAME']

		plt.xlabel("lables")
		plt.ylabel('Number of People')
		plt.xticks([r + barWidth for r in range(len(input_1))],
		["lablesa"])
		plt.legend()
		plt.show()

	def pie_chart(self, column_name):

		x = self.data[column_name]
		lables = self.data['NAME']
	
		fig, ax = plt.subplots()
	
		ax.pie(x, labels=lables,autopct='%.1f%%', radius=2, center=(5, 5),
			wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)

		plt.show()



dataframe = data_converter_region(r"C:\Users\Ripper.000\Desktop\NST-EST2021-alldata.csv")

data = Vis_Census(dataframe)


print(data.pie_chart('ESTIMATESBASE2020'))
print(data.bar_graph('ESTIMATESBASE2020'))