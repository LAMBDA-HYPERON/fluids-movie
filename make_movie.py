#!/usr/bin/env python

import sys
import argparse

import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
from matplotlib import animation

"""
This script makes a fluid animation using NetCDF data.
"""

def main ():
	
	# Setup arguments.
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file',help="Input file containing our data")
	parser.add_argument('field_name',help="Data field to animate")
	args = parser.parse_args()
	
	# Open netCDF file (arg.input_file).
	f = nc.Dataset(args.input_file)
	vorticity = f.variables['vorticity_z']
	# vorticity dimension: Time, st_ocean (pressure), yt_ocean (latitude), xt_ocean (longitude)
	vorticity = vorticity[:]
	
	fig = plt.figure()
	images = []
	
	# Generate the plot at pressure level = 0
	for t in range(0,vorticity.shape[0]):
		#plt.imshow(vorticity[t,0,:,:])
		img = plt.imshow(vorticity[t,0,:,:])
		images.append([img])
		# To show plot immediately, use:
		# plt.show()
		# Save the plot as an image file
		#plt.savefig('vorticity'+str(t).zfill(3)+'.png')
		#plt.close()

	ani = animation.ArtistAnimation(fig,images,interval=20)
	plt.show()
	
	# Close the netcdf file.
	f.close()
	
	print "Completed..."
	return True

if __name__=="__main__":
	sys.exit(main())
