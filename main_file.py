# Libraries
from pyomo.environ import *
import system_data_for_pyomo as sd
import three_phase_opf_model as pf
import pre_processing_system_data as psd
import print_results as prnt
import math 
import pandas as pd
import numpy as np

if __name__=="__main__":
    
    # General Parameters
    V0 = 4.16/math.sqrt(3)
    Tha0 = 0
    Thb0 = -2.0944
    Thc0 = 2.0944
    
    # Distribution System Data
    System_Data_Nodes = pd.read_excel('Nodes_25_3F.xlsx')
    System_Data_Lines = pd.read_excel('Lines_25_3F.xlsx')
    
# ---------  Pre-processing System Data --------------
    System_Data_Lines_Prima = psd.pre_processing_system_data(System_Data_Lines, System_Data_Nodes, Tha0, Thb0, Thc0)
        
# ---------  System Data for Pyomo --------------
    Data_Network = sd.system_data_for_pyomo(System_Data_Nodes, System_Data_Lines_Prima)
    
# --------- Create the Model --------------
    model =  pf.three_phase_opf_model(V0, Data_Network)      
    solver = SolverFactory('ipopt')
    results = solver.solve(model, tee=True)

# --------- Print Results --------------
    prnt.print_results(model,V0)