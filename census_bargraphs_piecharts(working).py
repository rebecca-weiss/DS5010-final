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



class Vis_Census:
	'''This is the class to visualize the data with Bar Graphs and Pie Charts'''

	def __init__(self, data):
		self.data = data

	def bar_graph(self, var1): 

		input_1 = self.data[var1]
		lables = self.data['NAME']
		x = lables
		y = input_1

		fig, ax = plt.subplots(figsize =(15, 8))
		barWidth = .5
		br1 = np.arange(len(input_1))
		ax.bar(x,y, width = 1, edgecolor = 'white', linewidth =.7, label = var1)
		plt.xticks(range(len(x)), x, rotation='vertical')
		plt.xlabel("Location") #from x
		plt.ylabel('Number of People') #from y
		plt.legend()
		plt.show()

	def compare_bar_graph(self, var1, var2):

		fig = plt.subplots(figsize =(20, 8))
 
		input_1 = self.data[var1]
		input_2 = self.data[var2]

		barWidth = .35
		br1 = np.arange(len(input_1))
		br2 = [x + barWidth for x in br1]
 
		plt.bar(br1, input_1, width = barWidth, label = var1)
		plt.bar(br2, input_2, width = barWidth, label = var2)

		labels = self.data['NAME']

		plt.xlabel("Location")
		plt.ylabel('Number of People')
		plt.xticks([r + barWidth for r in range(len(input_1))], labels, rotation='vertical')
		plt.legend()
		plt.show()

	def pie_chart(self, var1):

		x = self.data[var1]
		labels = self.data['NAME']
	
		fig, ax = plt.subplots()

		ax.pie(x, radius = 3) # add if you want pie chart directly labeled (, labels = labels, autopct ='%.1f%%', pctdistance = 1.1, labeldistance = 1.2)
		percents = x.to_numpy() * 100 / x.to_numpy().sum()
		plt.legend(bbox_to_anchor=(2,1.5), labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels,percents)])
		centre_circle = plt.Circle((0, 0), 0.70, fc='white')
		fig = plt.gcf()
		plt.show()

	


if __name__ == "__main__":
	dataframe = data_converter_state(r"C:\Users\Ripper.000\Desktop\NST-EST2021-alldata.csv")

	data = Vis_Census(dataframe)
	print(data.compare_bar_graph('ESTIMATESBASE2020','POPESTIMATE2021'))
	print(data.bar_graph('ESTIMATESBASE2020'))
	print(data.pie_chart('ESTIMATESBASE2020'))

	dataframe = data_converter_region(r"C:\Users\Ripper.000\Desktop\NST-EST2021-alldata.csv")

	data = Vis_Census(dataframe)
	print(data.compare_bar_graph('ESTIMATESBASE2020','POPESTIMATE2021'))
	print(data.bar_graph('ESTIMATESBASE2020'))
	print(data.pie_chart('ESTIMATESBASE2020'))

