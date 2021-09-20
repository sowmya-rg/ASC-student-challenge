# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 07:22:02 2021

@author: RAGHU
"""

import IPython as IP 
IP.get_ipython().magic('reset -sf')

import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import sklearn as sk


plt.close('all')

# Load Data
ASC_2021_data = pd.read_csv("ASC-2021-1.csv")
ASC_2021_data_1=ASC_2021_data.loc[450:,:]
columns_X=['Cycle Number','Heat Rate 1 [C/min]','Ramp 1 Duration [min]',
           'Temperature Dwell 1 [min]','Heat Rate 2 [C/min]',
           'Ramp 2 Duration [min]','Temperature Dwell 2 [min]',
           'Vacuum Pressure (*Patm) [Pa]','Vacuum Start Time [min]',
           'Vacuum Duration [min]','Autoclave Pressure (*Patm) [Pa]',
           'Autoclave Start Time [min]','Autoclave Duration [min]']
columns_y=['AD. Porosity (%)','PR. Porosity (%)','Eff. Porosity (%)',
           'Max (Fiber Volume Fraction) (%)','Cure Cycle Total Time [min]',
           'PR. Volume [m^3]','Class']
ASC_2021_data_X = ASC_2021_data_1[columns_X]
ASC_2021_data_y = ASC_2021_data_1[columns_y]
X = ASC_2021_data_X
y = ASC_2021_data_y['AD. Porosity (%)']
X=columns_X
Y=['Class']
y=ASC_2021_data[Y]
#%% Plots of Raw Data - Independent Variables
# Heat Rate 1
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Heat Rate 1 [C/min]'], color='blue')
plt.title('Cycle Number vs Heat Rate 1 - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Heat Rate 1 [C/min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Heat Rate 1 - with 2 Heat Ramp.png', dpi = 300)

# Heat Rate 2
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Heat Rate 2 [C/min]'], color='blue')
plt.title('Cycle Number vs Heat Rate 2 - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Heat Rate 2 [C/min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Heat Rate 2 - with 2 Heat Ramp.png', dpi = 300)

# Ramp Duration 1
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Ramp 1 Duration [min]'], color='red')
plt.title('Cycle Number vs Ramp 1 Duration - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Ramp 1 Duration [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Ramp Duration 1 - with 2 Heat Ramp.png', dpi = 300)

# Ramp Duration 2
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Ramp 2 Duration [min]'], color='red')
plt.title('Cycle Number vs Ramp Duration 2 - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Ramp 2 Duration [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Ramp 2 Duration  - with 2 Heat Ramp.png', dpi = 300)

# Temp. Dwell 1
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Temperature Dwell 1 [min]'], color='red')
plt.title('Cycle Number vs Temperature Dwell 1 - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Temperature Dwell 1 [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Temperature Dwell 1 - with 2 Heat Ramp.png', dpi = 300)

# Temp. Dwell 2
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Temperature Dwell 2 [min]'], color='red')
plt.title('Cycle Number vs Temperature Dwell 2 - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Temperature Dwell 2 [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Temperature Dwell 2 - with 2 Heat Ramp.png', dpi = 300)

# Vacuum Pressure
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Vacuum Pressure (*Patm) [Pa]'], color='red')
plt.title('Cycle Number vs Vacuum Pressure - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Vacuum Pressure (*Patm) [Pa]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Vacuum Pressure - with 2 Heat Ramp.png', dpi = 300)
# Vacuum Start Time
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Vacuum Start Time [min]'], color='red')
plt.title('Cycle Number vs Vacuum Start Time - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Vacuum Start Time [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Vacuum Start Time - with 2 Heat Ramp.png', dpi = 300)
#Vacuum Duration
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Vacuum Duration [min]'], color='red')
plt.title('Cycle Number vs Vacuum Duration - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Vacuum Duration [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Vacuum Duration - with 2 Heat Ramp.png', dpi = 300)
#Autoclave Pressure
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Autoclave Pressure (*Patm) [Pa]'], color='red')
plt.title('Cycle Number vs Autoclave Pressure- with 2 Heat Ramp', fontsize=10)
plt.ylabel('Autoclave Pressure (*Patm) [Pa]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Autoclave Pressure - with 2 Heat Ramp.png', dpi = 300)
# Autoclave Start Time
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Autoclave Start Time [min]'], color='red')
plt.title('Cycle Number vs Autoclave Start Time - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Autoclave Start Time [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Autoclave Start Time - with 2 Heat Ramp.png', dpi = 300)
#Autoclave Duration
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_X['Autoclave Duration [min]'], color='red')
plt.title('Cycle Number vs Autoclave Duration - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Autoclave Duration [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Autoclave Duration - with 2 Heat Ramp.png', dpi = 300)
#%% Dependent Variables
#Adhesive Porosity
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['AD. Porosity (%)'], color='red')
plt.title('Cycle Number vs AD. Porosity - with 2 Heat Ramp', fontsize=10)
plt.ylabel('AD. Porosity (%)', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs AD. Porosity - with 2 Heat Ramp.png', dpi = 300)
#Prepreg Porosity
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['PR. Porosity (%)'], color='red')
plt.title('Cycle Number vs PR. Porosity - with 2 Heat Ramp', fontsize=10)
plt.ylabel('PR. Porosity (%)', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs PR. Porosity - with 2 Heat Ramp.png', dpi = 300)
#Effective Porosity
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['Eff. Porosity (%)'], color='red')
plt.title('Cycle Number vs Eff. Porosity - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Eff. Porosity (%)', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Eff. Porosity - with 2 Heat Ramp.png', dpi = 300)
#Max. Vf
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['Max (Fiber Volume Fraction) (%)'], color='red')
plt.title('Cycle Number vs Max (Fiber Volume Fraction) - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Max (Fiber Volume Fraction) (%))', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Max Vf - with 2 Heat Ramp.png', dpi = 300)
#Cure Cycle Time
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['Cure Cycle Total Time [min]'], color='red')
plt.title('Cycle Number vs Cure Cycle Total Time  - with 2 Heat Ramp', fontsize=10)
plt.ylabel('Cure Cycle Total Time [min]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs Cure Cycle Time - with 2 Heat Ramp.png', dpi = 300)
#PR. Volume
plt.figure(figsize=(6.5,4))
plt.scatter( ASC_2021_data_X['Cycle Number'],ASC_2021_data_y['PR. Volume [m^3]'], color='red')
plt.title('Cycle Number vs PR. Volume [m^3] - with 2 Heat Ramp', fontsize=10)
plt.ylabel('PR. Volume [$m^3$]', fontsize=10)
plt.xlabel('Cycle Number', fontsize=10)
plt.grid(True)
plt.show()
plt.tight_layout()
plt.savefig('Heat Ramp 2 - Plots/Cycle Number vs PR.Volume - with 2 Heat Ramp.png', dpi = 300)


