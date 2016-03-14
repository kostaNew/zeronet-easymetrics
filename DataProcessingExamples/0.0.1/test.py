import matplotlib.pyplot as plt
import numpy as np

def time_to_time(time):
	return (time - time[0]) / 60

dtemplate = np.dtype([('time', 'float64'), ('peers_connected', 'float64'), ('peers_good', 'float64'), ('peers_total', 'float64')])

zero_talk    = np.loadtxt('1TaLkFrMwvbNsooF4ioKAY9EuxTBTjipT',dtype=dtemplate)[0:-100]
ru_zero_talk = np.loadtxt('1Apr5ba6u9Nz6eFASmFrefGvyBKkM76QgE',dtype=dtemplate)[0:-100]
es_zero_talk = np.loadtxt('165eqHdoQfyf7CVGqtVCGNDvMBZhwVSJBL',dtype=dtemplate)[0:-100]
fr_zero_talk = np.loadtxt('1Vp5LH4wegCaqeB72yMw2jgNdVm4aR7ET',dtype=dtemplate)[0:-100]

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(time_to_time(zero_talk['time']), zero_talk['peers_total'], label='ZeroTalk')
ax.plot(time_to_time(ru_zero_talk['time']), ru_zero_talk['peers_total'], label='Ru-ZeroTalk')
ax.plot(time_to_time(es_zero_talk['time']), es_zero_talk['peers_total'], label='Es-ZeroTalk')
ax.plot(time_to_time(fr_zero_talk['time']), fr_zero_talk['peers_total'], label='Fr-ZeroTalk')

#ax.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, fancybox=True, shadow=True)

plt.show()
