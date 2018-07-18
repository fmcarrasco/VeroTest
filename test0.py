# Required libraries
import matplotlib.pyplot as plt
from netCDF4 import Dataset

# Path to the GOES-R simulated image file
path = './Datos/dato.nc'

# Open the file using the NetCDF4 library
nc = Dataset(path)

# Extract the Brightness Temperature values from the NetCDF
data = nc.variables['CMI'][:]

# Show data
plt.imshow(data, cmap='Greys')
plt.savefig('./Figuras/test0.jpg')
