import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np

temps_wed = [[5, 36.6], [6, 37.2], [10, 37.0], [11, 37.0], [12, 37.7], [13, 37.3], [14, 37.0], [15, 37.3], [16, 37.6], [17, 37.6], [18, 37.6], [19, 37.7], [20, 37.6], [21, 37.3], [22, 37.6], [23, 38.1], [24, 37.9]]
temps_thu = [[1, 37.6], [5, 35.7], [7, 35.3], [9, 35.2], [11, 35.7], [12, 36.2]]

hours_from_jab = list(range(49))

temp = [36.5]*49
chill = [0]*49
sweat = [0]*49
sleep = [0]*49
soreness = [0]*49


for x in temps_wed:
    temp[x[0]+6] = x[1]

for x in temps_thu:
    temp[x[0]+30] = x[1]

#temp = [x - 36.5 for x in temp]

chill[11] = 10
chill [12] = 10
for i in range(13, 22):
    chill[i] = 2
for i in range(22, 29):
    chill[i] = 4
for i in range(29, 32):
    chill[i] = 3
for i in range(32, 37):
    chill[i] = 2
for i in range(37, 39):
    chill[i] = 5
for i in range(39, 42):
    chill[i] = 4

sweat[16] = 7
for i in range(17, 22):
    sweat[i] = 6
for i in range(22, 28):
    sweat[i] = 3
for i in range(28, 31):
    sweat[i] = 5

for i in range(31, 39):
    sweat[i] = 10

for i in range(39, 43):
    sweat[i] = 6

for i in range(6, 11):
    sleep[i] = 10

for i in range(13, 17):
    sleep[i] = 10

for i in range(22, 25):
    sleep[i] = 10

for i in range(31, 39):
    sleep[i] = 10

for i in range(12, 20):
    soreness[i] = 10

for i in range(20, 25):
    soreness[i] = 8

for i in range(25, 39):
    soreness[i] = 7

for i in range(39, 43):
    soreness[i] = 5

paracetamol = [0]*49
paracetamol[12] = 10
paracetamol[19] = 10
paracetamol[26] = 10
paracetamol[32] = 10

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (hours from jab)')
ax1.set_ylabel('temp (C)', color=color)
plot1, = ax1.plot(hours_from_jab[10:], temp[10:], color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#ax2.set_ylabel('chills (range of 0 to 10)', color='olive')  # we already handled the x-label with ax1
plot2, = ax2.plot(hours_from_jab[10:], chill[10:], color='olive', linewidth=2, linestyle='dashed')
#ax2.tick_params(axis='y', labelcolor='olive')

ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#ax3.set_ylabel('sweating (range of 0 to 10)', color='blue')  # we already handled the x-label with ax1
plot3, = ax3.plot(hours_from_jab[10:], sweat[10:], color='blue', linewidth=3)
#ax3.tick_params(axis='y', labelcolor='blue')

ax4 = ax1.twinx()
plot4, = ax4.plot(hours_from_jab[10:], sleep[10:], color='gray', linewidth=1)

ax5 = ax1.twinx()
plot5, = ax5.plot(hours_from_jab[10:], soreness[10:], color='black', linewidth=1)

#ax6 = ax1.twinx()
#plot6, = ax6.scatter(hours_from_jab[10:], paracetamol[10:])

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

# plt.plot(hours_from_jab, temp)
# plt.plot(hours_from_jab, chill)
# plt.plot(hours_from_jab, sweat)
# plt.plot(hours_from_jab, soreness)
# plt.plot(hours_from_jab, sleep)
# plt.plot(hours_from_jab, headache)

plt.legend([plot1, plot2, plot3, plot4, plot5], ["temp (C)", "chills (range of 0 to 10) - scale to the right", "sweating (range of 0 to 10) - scale to the right", "sleep (binary 0/10) - scale to the right", "muscle/joint ssoreness (range of 0 to 10) - scale to the right"])
plt.show()