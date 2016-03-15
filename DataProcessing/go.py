import json
import os
import sys
from processing_core import clean_additional_header
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt

def main():
	if not (len(sys.argv) == 3):
		print "FORMAT: python ./go <task> <scope>"
		print "SAMPLE: python ./go peers zeronet"
		exit()
	
	config = []
	with open('./config.json', 'r') as cf:
		config = json.load(cf)

	task = config['tasks'][sys.argv[1]]
	scope = config['scopes'][sys.argv[2]]

	from peers_per_site import default
	default(config['general'], task, scope)

if __name__ == "__main__":
	main()
