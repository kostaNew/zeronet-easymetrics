import matplotlib.pyplot as plt
import numpy as np

def time_to_time(time):
	return (time - time[0]) / 60

dtemplate = np.dtype([('time', 'float64'), ('peers_connected', 'float64'), ('peers_good', 'float64'), ('peers_total', 'float64')])

zero_talk    = np.loadtxt('1TaLkFrMwvbNsooF4ioKAY9EuxTBTjipT',dtype=dtemplate)[0:-100]

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(time_to_time(zero_talk['time']), zero_talk['peers_connected'], label='peers_connected')
ax.plot(time_to_time(zero_talk['time']), zero_talk['peers_good'], label='peers_good')
ax.plot(time_to_time(zero_talk['time']), zero_talk['peers_total'], label='peers_total')

#ax.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, fancybox=True, shadow=True)

plt.show()
