# to do: 
from netCDF4 import Dataset
import numpy as np

#input: salinity, temperature, and pressure in form of netcdf file 
#1st: import data and get all 
dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')
salinity= dataset['so']
temp = dataset['to']
pressure = dataset['depth']
latitude = dataset['latitude']
longitude = dataset['longitude']

print(salinity.shape)
print(temp.shape)
print(pressure.shape)
print(latitude.shape)
print(longitude.shape)

pressure3D = np.zeroes((31,80,27))

for i in pressure:
	pressure3D[1,:,:]


