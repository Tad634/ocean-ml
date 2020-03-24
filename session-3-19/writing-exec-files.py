# to do
from netCDF4 import Dataset
import numpy
import datetime as td
dataset= Dataset(r"/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc")
time = dataset['time']
time_one = str(time[1])
print(time_one)