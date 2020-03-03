#to do
from netCDF4 import Dataset
import numpy as np
import seawater as sw

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')
geopotential_h = (dataset["zo"])
print(geopotential_h.shape)