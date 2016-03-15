import json
import os
from processing_core import clean_additional_header
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt

def default(general, task, scope):

	#Read and clean data
	data = pd.read_csv(os.path.join(general["folder"], general["zite_data"]))
	data = clean_additional_header(data)
	data['time'] = data['time'].astype('float')
	data['time'] = pd.to_datetime(data['time'], unit='s')
	data['peers_total'] = data['peers_total'].astype('int')
	
	#Peers by time
	plot_series = []
	for el in scope:
		zite_name = el['zite']
		temp_ = data[data.address == zite_name][['time','peers_total']].sort_values(by='time')
		plot_series.append({'time':temp_['time'], 'peers_total':temp_['peers_total'], 'label':el['label']})
	
	#Plots
	fig = plt.figure()
	ax = plt.subplot(111)

	for p in plot_series:
		ax.plot(p['time'], p['peers_total'], label=p['label'])
	
	plt.xticks(rotation=15)	

	majorFormatter = matplotlib.dates.DateFormatter('%m-%d %H:%M:%S')
	ax.xaxis.set_major_formatter(majorFormatter)
	ax.autoscale_view()
	
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
		  ncol=3, fancybox=True, shadow=True)

	plt.show()
