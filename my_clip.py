# Author: Mitchell Lazarz
# Creation Date: 16 October 2020
# Python 2.7: my_clip.py
# Description: This code uses the clip tool in ArcGIS with a lake shapefile as the input feature, a basin shapefile
# as the clip feature, resulting in an output of all lakes within the basin shapefile.  The output lakes_myClip is
# saved to the local drive.

# Imports the arcpy site package
import arcpy

# Workspace environment folder is set
arcpy.env.workspace = "C:/CLARK/PythonProgramming/CompProg_Lab1"

# Clip tool is called with lakes and basin shapefiles as inputs, producing shapefile of all lakes within basin
arcpy.Clip_analysis("Data_Lab_1_Geoprocessing_ArcGIS/lakes.shp","Data_Lab_1_Geoprocessing_ArcGIS/basin.shp","Results/lakes_myClip.shp")
