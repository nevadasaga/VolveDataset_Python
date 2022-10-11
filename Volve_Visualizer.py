## Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

## Opening the F-4 well Trajectory file
WITSML_file = r"C:\Users\Nevada\Desktop\1.xml"

# Reading the WITSML file
with open(WITSML_file) as f:
    data = f.read()

## Parse the WITSML file using the Beautiful library
data_xml = BeautifulSoup(data, 'xml')
