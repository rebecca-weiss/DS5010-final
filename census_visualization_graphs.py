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

	def scatter_plot(self, column_name):

		x = self.x_axis
		y = self.data[column_name]

		sizes = np.random.uniform(15, 80, len(x))
		colors = np.random.uniform(15, 80, len(x))

		fig, ax = plt.subplots()

		plt.show()

		pass

	def bar_graph(self, column_name): # example if you want to isolate and run alone (does include everything)

		x = self.data['NAME']
		y = self.data["ESTIMATESBASE2020"]

		fig, ax = plt.subplots()

		ax.bar(x,y, width = 1, edgecolor = 'white', linewidth =.7)
		plt.xticks(range(len(x)), x, rotation='vertical')


		plt.xlabel('State')
		plt.ylabel('Estimated Population 2020')

		plt.show()

	def pie_chart(self, column_name):
		x = self.data[column_name]
		colors = plt.get_cmap('Orange')(np.linspace(0.2, 0.7, len(x)))

		fig, ax = plt.subplots()
		ax.pie(x, colors=colors, radius=6, center=(4, 4),
		wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
		plt.show()

		pass