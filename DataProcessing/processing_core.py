import matplotlib
import numpy as np
import pandas as pd
import matplotlib.dates as md
import datetime as dt

def clean_additional_header(data):
	if not data.time.dtype == 'float64':
		return data.drop(data[data.time == 'time'].index)
	else: 
		return data
