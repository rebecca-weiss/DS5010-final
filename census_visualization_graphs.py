import matplotlib.pyplot as plt
import numpy as np
import pandas as pds
import csv


#This is all arbitrary until base code is established. To run, just take out self. and run as individual functions 


class Vis_Census:
	'''This is the class to visualize the data with Scatter Plot, Bar Graphs, Histograms, and Pie Charts'''

	def __init__(self, data):
		self.data = pds.read_csv(r"C:\Users\Ripper.000\Desktop\NST-EST2021-alldata.csv")

	def x_axis(self, data):
		'''to differ between state and region/entire USA'''

		x_axis = 0

		if self.REGION > 0: #for state
			x_axis = self.data[5:]
			return x_axis
		else: #for regions and USA
			x_axis = self.data[:5]
			return x_axis

	def compare_bar_graph(self, column_name, column_name):

		barWidth = 0.25
		fig = plt.subplots(figsize =(12, 8))
 
		input_1 = self.data["column_name"]
		input_2 = self.data["column_name"]

		br1 = np.arange(len(input_1))
		br2 = [x + barWidth for x in br1]
 
		plt.bar(br1, input_1, width = barWidth, label ='column_name')
		plt.bar(br2, input_2, width = barWidth, label ='column_name')

		plt.xlabel("NAME" or "REGION")
		plt.ylabel('Value')
		plt.xticks([r + barWidth for r in range(len(input_1))],
		["NAME" or "REGION"])
		plt.legend()
		plt.show()

	def bar_graph(self, column_name): 
		
		x = self.data['column_name']
		y = self.data["column_name"]

		fig, ax = plt.subplots()

		ax.bar(x,y, width = 1, edgecolor = 'white', linewidth =.7)
		plt.xticks(range(len(x)), x, rotation='vertical')


		plt.xlabel('column_name') #from x
		plt.ylabel('column_name') #from y

		plt.show()

	def pie_chart(self, column_name):

		x = self.data[column_name]
		lables = self.data['NAME'] or self.data['REGION']
	
		fig, ax = plt.subplots()
	
		ax.pie(x, labels=lables,autopct='%.1f%%', radius=2, center=(5, 5),
			wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)

		plt.show()