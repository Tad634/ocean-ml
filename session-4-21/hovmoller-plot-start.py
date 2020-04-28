from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w_values = dataset["w"]
print(w_values.shape)

lat = dataset["latitude"]
first_plot = w_values[:,0,:,0]
first_plot = np.swapaxes(first_plot,0,1)
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
plt.show()