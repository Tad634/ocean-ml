from netCDF4 import Dataset
import numpy.ma as ma


# import the netcdf file using Dataset
dataset = Dataset(r'/Users/brownscholar/Desktop/Internship/ocean-ml/session-10-31/ssh_1572470095877.nc')

# read in and create variable for lat:
lat = dataset['latitude']

# lon:
lon = dataset['longitude']

# adt:
adt = dataset['adt']

# print shape of the adt variable:
#print(adt.shape)
#print(lon.shape)
#print(lat.shape)

# you will need this:
BATS_lat_max = 39.453
BATS_lon_max = 360 -59.648999999999994 # converting from degrees west to degrees east
BATS_lat_min = 19.663 
BATS_lon_min = 360 -66.211 #same

#print(lat[:])
print(BATS_lat_min,BATS_lat_max)


lat_index = set()
index = 0
for i in lat:
	if i < BATS_lat_max and i > BATS_lat_min:
		lat_index.add(index)
	index += 1

lon_index = set()
index = 0
for i in lon:
	if i < BATS_lon_max and i > BATS_lon_min:
		lon_index.add(index)
	index +=1 

print(lat_index)
print(lon_index)

latmin = min(lat_index)
latmax = max(lat_index)
lonmin = min(lon_index)
lonmax = max(lon_index)

BATSadt = adt[:, latmin:latmax, lonmin:lonmax]
print(BATSadt.shape)

