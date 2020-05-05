from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w_values = dataset["w"]
print(w_values.shape)

lat = dataset["latitude"]
depth = dataset["depth"]

first_plot = w_values[:,60,:,0]
second_plot = w_values[:,60,:,14]
third_plot = w_values[:,60,:,29]
first_plot = np.swapaxes(first_plot,0,1)
second_plot = np.swapaxes(second_plot,0,1)
third_plot = np.swapaxes(third_plot,0,1)
print(first_plot.shape)

top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
newcmp = ListedColormap(newcolors, name='RedBlue')
plt.title("hovmoller diagram at latitude = " + str(lat[0]))
plt.xlabel('years')
plt.ylabel('longitude')
plt.pcolormesh(first_plot,cmap=newcmp)
plt.colorbar()
#plt.show()
_min = -10
_max = 10

fig, ax = plt.subplots(3,1)
ax[0].pcolormesh(first_plot,cmap=newcmp,vmin = _min, vmax = _max)
ax[1].pcolormesh(second_plot,cmap=newcmp,vmin = _min, vmax = _max)
ax[2].pcolormesh(third_plot,cmap=newcmp,vmin = _min, vmax = _max)
fig.suptitle("Hovmoller diagram at different depths, at latitude " + str(lat[60]))
ax[0].set_title("depth = " + str(depth[0]))
ax[1].set_title("depth = " + str(depth[14]))
ax[2].set_title("depth =" + str(depth[29]))
plt.show()