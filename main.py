import numpy as np
import matplotlib.pyplot as plt
from function import avg
File = open(r"ppg50.txt", "r")
y = []
for val in File.read().split():
    y.append(float(val))
File.close()
y=np.array(y)
fs=250 #sampling frequency
nei = 5 #neighbours for max
window = 150 #finds max from local max points
x=np.arange(0,len(y)/fs,1/fs)
plt.plot(x,y)
z = avg(y,10) #removing noise
z = z - sum(z)/len(z)
z = z/max(z)

points = []
for i in range(nei, len(z)-nei):
    if(z[i]>z[i+nei] and z[i]>z[i-nei]):
        points.append(i)

points = np.array(points)
New_max = []
New_max.append(points[0])
for i in range(0, len(points)):
    if(points[i]-points[i-1]>fs//3):
        New_max.append(points[i])
New_max = np.array(New_max)
final_max=[]
for i in range(0, len(New_max)):
    V = y[New_max[i]]
    I = New_max[i]
    start = New_max[i] - window
    end = New_max[i] + window
    if New_max[i] - window <= 0:
        start = 0
    if New_max[i] + window >= len(y):
        end = len(y)
    for j in range(start, end):
        if (y[j] > V):
            V = y[j]
            I = j
    final_max.append(I)
final_max = np.array(final_max)
peaks=[]
peaks.append(final_max[0])
for i in range(1,len(final_max)):
    if final_max[i]!=final_max[i-1]:
        peaks.append(final_max[i])
peaks=np.array(peaks)
plt.scatter(peaks/fs,y[peaks])

plt.show()




