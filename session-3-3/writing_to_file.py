<<<<<<< HEAD
# to do 
# for i in range(0,10):
# 	for j in range(0,10):
# 		for k in range(0,10):
# 			print(i,j,k)

from netCDF4 import Dataset
import numpy as np
import seawater as sw

#input: salinity, temperature, and pressure in form of netcdf file 
#1st: import data and get all 
dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')
salinity= (dataset['so'])
temp = (dataset['to'])
pressure = dataset['depth']
latitude = dataset['latitude']
longitude = dataset['longitude']

#print(salinity.shape)
#print(temp.shape)
#print(pressure.shape)
#print(latitude.shape)
#print(longitude.shape)

pressure3D = np.zeros((31,80,27))


# firtst_layer=np.repeat(10,80*27).reshape(80,27)
# second_layer=np.repeat(20,80*27).reshape(80,27)

for i in range(0,31):
	pressure3D[i,:,:] = (np.repeat(pressure[i],80*27).reshape(80,27))

print(pressure3D)

density = (sw.dens(salinity[:], temp[:], pressure3D[:]))
density = density-1000
print(density.shape)

time_1 = density[10,:,:,:]
print(time_1)

# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			print(time_1[i,j,k])

density_file = open('density_file.txt', "w")
for i in range(0,31):
	for j in range(0,80):
		for k in range(0,27):
			density_file.write(str(time_1[i,j,k] ) + "\n") 
density_file.close()





=======
from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1581373134952.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

print(pressure.shape)
print(temperture.shape)
print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

# for depth_level in pressure:
# 	print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
density = density-1000

print(density.shape)

for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			print(i,j,k)
>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
