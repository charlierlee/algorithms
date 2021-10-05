import numpy as np
import time
def PCA(X , num_components):
     
    #Step-1
    X_meaned = X - np.mean(X , axis = 0)
     
    #Step-2
    cov_mat = np.cov(X_meaned , rowvar = False)
     
    #Step-3
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
     
    #Step-4
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
     
    #Step-5
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]
     
    #Step-6
    X_reduced = np.dot(eigenvector_subset.transpose() , X_meaned.transpose() ).transpose()
     
    return X_reduced

import pandas as pd
 
#Get the IRIS dataset
df = pd.read_csv('./maths/pca/solar-data2.csv',nrows=100000, skiprows=1, names=['timestamp','dc_voltage_scale_factor','ac_current_scale_factor','ac_voltage_scale_factor','ac_frequency_scale_factor','inverter_output_current','inverter_charge_current','inverter_buy_current','inverter_sell_current','output_ac_voltage','inverter_operating_mode','error_flags','warning_flags','battery_voltage','temperature_compensated_target_voltage','aux_output_state','transformer_temperature','capacitor_temperature','fet_temperature','ac_input_frequency','ac_input_voltage','minimum_ac_input_voltage','maximum_ac_input_voltage','sell_status','kwh_scale_factor','buy_kwh','sell_kwh','output_kwh','charger_kwh','output_kw','buy_kw','sell_kw','charge_kw','load_kw','ac_couple_kw','cc1_watts','cc1_battery_current','cc1_charger_state','cc2_watts','cc2_battery_current','cc2_charger_state','shunt_a_current','shunt_a_accumulated_kwh','shunt_a_accumulated_ah','shunt_b_current','shunt_b_accumulated_kwh','shunt_b_accumulated_ah','shunt_c_current','shunt_c_accumulated_kwh','shunt_c_accumulated_ah'])
target = df.iloc[:,23]
#prepare the data
df = df.loc[:, list(df.columns[1:23]) + list(df.columns[25:50])]
#x = x.apply(pd.to_numeric, axis=0)
df = df.loc[:, (df != 0).any(axis=0)]

#prepare the target


#Applying it to PCA function
mat_reduced = PCA(df , 2)
 
#Creating a Pandas DataFrame of reduced Dataset
principal_df = pd.DataFrame(mat_reduced , columns = ['PC1','PC2'])
 
#Concat it with target variable to create a complete Dataset
principal_df = pd.concat([principal_df , pd.DataFrame(target)] , axis = 1)

colors = list()
palette = {0: "red", 64: "green", 10: "blue", 26: "orange", 16: "yellow", 80: "black"}

for c in target: 
    colors.append(palette[int(c)])

import matplotlib.pyplot as plt
plt.scatter(principal_df['PC1'], principal_df['PC2'], c = colors, s=1)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
time.sleep(100)
