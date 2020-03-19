# to do 
# for i in range(0,10):
# 	for j in range(0,10):
# 		for k in range(0,10):
# 			print(i,j,k)

from netCDF4 import Dataset
import numpy as np
import seawater as sw
import datetime as td
import tricubic
#input: salinity, temperature, and pressure in form of netcdf file 
#1st: import data and get all 
dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')
salinity= (dataset['so'])
temp = (dataset['to'])
pressure = dataset['depth']
latitude = dataset['latitude']
longitude = dataset['longitude']
time = dataset['time']
dynamic_h = dataset["zo"]
dynamic_h = dynamic_h[:] * 100


def interp(startgrid):
	num_depths = 30 # to avoid problems with seafloor depth
	z_step = 10 
	depth_list = [10, 20, 30, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500, 600, 
    700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1750, 2000, 2500, 
    3000, 3500, 4000, 4500, 5000]

	new_depth = np.arange(z_step,(num_depths+1)*z_step,z_step) 
	new_depth_index = []
	left = 0
	right = 1
	for i in range(0,len(new_depth)):
		target_value = new_depth[i]
		if target_value > depth_list[right]:
			right += 1
			left +=1
		left_value = depth_list[left]
		right_value = depth_list[right]
		a = target_value-left_value
		b = right_value-left_value
		new_index = a/b+left
		new_depth_index.append(new_index)
		#start grid is shape lat,lon,depth
		lat = startgrid.shape[1]
		lon = startgrid.shape[2]
		depth = startgrid.shape[0]

	interp_grid = np.zeros((len(new_depth_index),lat,lon))
	ip = tricubic.tricubic(list(startgrid),[depth,lat,lon])

	for i in range(0,lat):
		for j in range(0,lon):
			for k in range(0,len(new_depth_index)):
				res = ip.ip([new_depth_index[k],i,j])
				interp_grid[k,i,j] = res

	return interp_grid


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

time_1 = density[:,:,:,:]

# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			print(time_1[i,j,k])

# density_file = open('density_file.txt', "w")
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(time_1[i,j,k] ) + "\n") 
# density_file.close()
#80 is lat, 27 is lon

start = td.date(1950,1,1)

#loops through 0-1356 and sets hours to i and all other values.
for i in range(0,1356):
	dynamic_at_time = interp(dynamic_h[i,:,:,:])
	density_at_time = interp(density[i,:,:,:])
	hours = td.timedelta(hours = int(time[i]))
	after = start + hours
	date = after.strftime("%y") + after.strftime("%m") + after.strftime("%d")
	dh = open("/Users/brownscholar/Desktop/file_dynamic_height/dh_" + str(date) + ".gr", "w")
	density_times = open("/Users/brownscholar/Desktop/file_density/density_" + str(date) + ".gr", "w")
	dh.write("\t30\n\t80\t27")
	density_times.write("\t30\n\t80\t27")
	for j in range(0,30):
		for k in range(0,80):
			for r in range(0,27):
				density_times.write(str(density_at_time[j,k,r]) + "\n")
				dh.write(str(dynamic_at_time[j,k,r]) + "\n")
	density_times.close()
	dh.close()