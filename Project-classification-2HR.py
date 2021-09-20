# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:33:39 2021

@author: raghu
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
ASC_2021_data = pd.read_csv("ASC2021_DataSet_1.csv")
ASC_2021_data_1=ASC_2021_data.loc[450:,:]
descr = ASC_2021_data.describe
columns_X=['Cycle Number','Heat Rate 1 [C/min]','Ramp 1 Duration [min]','Temperature Dwell 1 [min]','Heat Rate 2 [C/min]','Ramp 2 Duration [min]','Temperature Dwell 2 [min]','Vacuum Pressure (*Patm) [Pa]','Vacuum Start Time [min]','Vacuum Duration [min]','Autoclave Pressure (*Patm) [Pa]','Autoclave Start Time [min]','Autoclave Duration [min]']
columns_y=['AD. Porosity (%)','PR. Porosity (%)','Eff. Porosity (%)','Max (Fiber Volume Fraction) (%)','Cure Cycle Total Time [min]','PR. Volume [m^3]','Class']
# plt.figure()
# ASC_2021_data_1['Vacuum Pressure (*Patm) [Pa]'].hist()
# plt.figure()
# ASC_2021_data_1['Autoclave Pressure (*Patm) [Pa]'].hist()
# plt.figure()
# ASC_2021_data_1['Autoclave Duration [min]'].hist()
# plt.figure()
# ASC_2021_data_1['Autoclave Duration [min]'].hist()
# plt.figure()
# ASC_2021_data_1['Vacuum Duration [min]'].hist()

#scatter plot
colors =['red','blue','green']
markers =['s','*','p']
Class =['High-Consolidation','Low-Consolidation','Mod-Consolidation']

# =============================================================================
# Maximum Fibre Volume Fraction
# =============================================================================
#Vac Pressure vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1A.png', dpi = 300)

#Temp Dwell 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1B.png', dpi = 300)

#Heat Rate 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1C.png', dpi = 300)

#Ramp Dur 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1D.png', dpi = 300)

#Autoclave Pressure vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1E.png', dpi = 300)

#Vac Duration vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1F.png', dpi = 300)

#Autoclave Duration vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1G.png', dpi = 300)

#Vacuum Start time vs Vf
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1H.png', dpi = 300)

#Autoclave Start time vs Vf
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Start Time [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1I.png', dpi = 300)

#Temp Dwell 2 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1J.png', dpi = 300)

#Heat Rate 2 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1K.png', dpi = 300)

#Ramp Dur 2 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['Max (Fiber Volume Fraction) (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('Max (Fiber Volume Fraction) (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/1L.png', dpi = 300)
# =============================================================================
# Effective Porosity
# =============================================================================
#Vac Pressure vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2A.png', dpi = 300)
#Temp Dwell 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2B.png', dpi = 300)
#Heat Rate 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2C.png', dpi = 300)
#Ramp Dur 1 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2D.png', dpi = 300)
#Autoclave Pressure vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2E.png', dpi = 300)
#Vac Duration vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2F.png', dpi = 300)
#Autoclave Duration vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('Eff. Porosity (%)')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2G.png', dpi = 300)
#Vacuum Start time vs Vf
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2H.png', dpi = 300)
#Autoclave Start time vs Vf
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2I.png', dpi = 300)
#Temp Dwell 2 vs Eff. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2J.png', dpi = 300)

#Heat Rate 2 vs Eff. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2K.png', dpi = 300)

#Ramp Dur 2 vs Vf
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('Eff. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/2L.png', dpi = 300)
# =============================================================================
# Adhesive Porosity
# =============================================================================
#Vac Pressure vs AD.
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3A.png', dpi = 300)
#Temp Dwell 1 vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3B.png', dpi = 300)
#Heat Rate 1 vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3C.png', dpi = 300)
#Ramp Dur 1 vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3D.png', dpi = 300)
#Autoclave Pressure vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3E.png', dpi = 300)
#Vac Duration vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3F.png', dpi = 300)
#Autoclave Duration vs AD
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('AD. Porosity (%)')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3G.png', dpi = 300)
#Vacuum Start time vs AD
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3H.png', dpi = 300)
#AUTOCLAVE Start time vs AD
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['Eff. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Start Time [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3I.png', dpi = 300)

#Temp Dwell 2 vs AD. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3J.png', dpi = 300)

#Heat Rate 2 vs AD. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3K.png', dpi = 300)

#Ramp Dur 2 vs ad
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['AD. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('AD. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/3L.png', dpi = 300)
# =============================================================================
# Prepreg Porosity
# =============================================================================
#Vac Pressure vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4A.png', dpi = 300)
#Temp Dwell 1 vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4B.png', dpi = 300)
#Heat Rate 1 vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4C.png', dpi = 300)
#Ramp Dur 1 vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4D.png', dpi = 300)
#Autoclave Pressure vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4E.png', dpi = 300)
#Vac Duration vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4F.png', dpi = 300)
#Autoclave Duration vs PR
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('PR. Porosity (%)')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4G.png', dpi = 300)
#Vacuum Start time vs PR
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4H.png', dpi = 300)
#Autoclave Start time vs PR
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4I.png', dpi = 300)
#Temp Dwell 2 vs PR. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4J.png', dpi = 300)

#Heat Rate 2 vs PR. Porosity (%)
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4K.png', dpi = 300)

#Ramp Dur 2 vs pr
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['PR. Porosity (%)'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('PR. Porosity (%)')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/4L.png', dpi = 300)
# =============================================================================
# Prepreg Volume
# =============================================================================
#Vac Pressure vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5A.png', dpi = 300)
#Temp Dwell 1 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5B.png', dpi = 300)
#Heat Rate 1 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5C.png', dpi = 300)
#Ramp Dur 1 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5D.png', dpi = 300)
#Autoclave Pressure vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5E.png', dpi = 300)
#Vac Duration vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5F.png', dpi = 300)
#Autoclave Duration vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('PR. Volume [m^3]')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5G.png', dpi = 300)
#Vacuum Start time vs 'PR. Volume [m^3]'
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5H.png', dpi = 300)
#Autoclave Start time vs 'PR. Volume [m^3]'
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Start Time [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5I.png', dpi = 300)
#Temp Dwell 2 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5J.png', dpi = 300)

#Heat Rate 2 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5K.png', dpi = 300)

#Ramp Dur 2 vs 'PR. Volume [m^3]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['PR. Volume [m^3]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('PR. Volume [m^3]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/5L.png', dpi = 300)
# =============================================================================
# Cure Cycle Time
# =============================================================================
#Vac Pressure vs'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Pressure (*Patm) [Pa]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Pressure (*Patm) [Pa]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6A.png', dpi = 300)
#Temp Dwell 1 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 1 [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 1 [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6B.png', dpi = 300)
#Heat Rate 1 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 1 [C/min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 1 [C/min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6C.png', dpi = 300)
#Ramp Dur 1 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 1 Duration [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 1 Duration [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6D.png', dpi = 300)
#Autoclave Pressure vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Pressure (*Patm) [Pa]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Pressure (*Patm) [Pa]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6E.png', dpi = 300)
#Vac Duration vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Duration [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Duration [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6F.png', dpi = 300)
#Autoclave Duration vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Duration [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Duration [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6G.png', dpi = 300)
#Vacuum Start time vs 'Cure Cycle Total Time [min]'
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Vacuum Start Time [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Vacuum Start Time [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6H.png', dpi = 300)
#Autoclave Start time vs 'Cure Cycle Total Time [min]'
plt.legend()
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Autoclave Start Time [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Autoclave Start Time [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6I.png', dpi = 300)

#Temp Dwell 2 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Temperature Dwell 2 [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Temperature Dwell 2 [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6J.png', dpi = 300)

#Heat Rate 2 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Heat Rate 2 [C/min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Heat Rate 2 [C/min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6K.png', dpi = 300)

#Ramp Dur 2 vs 'Cure Cycle Total Time [min]'
plt.figure(figsize=(6.5,4))
for i in range(3):
    X= ASC_2021_data_1[ASC_2021_data_1['Class'] == Class[i]]
    plt.scatter(X['Ramp 2 Duration [min]'], X['Cure Cycle Total Time [min]'], c= colors[i], label =Class[i], marker=markers[i])
plt.xlabel('Ramp 2 Duration [min]')
plt.ylabel('Cure Cycle Total Time [min]')
plt.legend()
plt.tight_layout()
plt.savefig('CLASSIFICATION-HEATRAMP-2/6L.png', dpi = 300)