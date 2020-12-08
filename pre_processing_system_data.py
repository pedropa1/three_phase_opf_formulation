import pandas as pd
import math 

def pre_processing_system_data(System_Data_Lines, System_Data_Nodes, Tha0, Thb0, Thc0):

    # From Ohm to mOhms as everythin is in kW
    for col in ['Raa', 'Xaa', 'Rbb', 'Xbb', 'Rcc', 'Xcc', 'Rab', 'Xab', 'Rac', 'Xac', 'Rbc', 'Xbc']:
        System_Data_Lines[col] = System_Data_Lines[col]/1000
    
    # Process System_Data_Lines to obtain the Impedance Prima
    System_Data_Lines_Impedances = pd.DataFrame(0.0, index = System_Data_Lines.index, columns = ['FROM', 'TO', 'Zaa', 'Thaa', 'Zbb', 'Thbb', 'Zcc', 'Thcc', 'Zab', 'Thab', 'Zac', 'Thac', 'Zbc', 'Thbc'])
    System_Data_Lines_Impedances['FROM'] =     System_Data_Lines['FROM'] 
    System_Data_Lines_Impedances['TO'] =     System_Data_Lines['TO'] 
    for i in System_Data_Lines_Impedances.index:
        System_Data_Lines_Impedances.iloc[i,2] = math.sqrt(System_Data_Lines.iloc[i,2]**2 + System_Data_Lines.iloc[i,3]**2) # Zaa
        System_Data_Lines_Impedances.iloc[i,3] = math.atan(System_Data_Lines.iloc[i,3]/System_Data_Lines.iloc[i,2])         # Thaa
        System_Data_Lines_Impedances.iloc[i,4] = math.sqrt(System_Data_Lines.iloc[i,4]**2 + System_Data_Lines.iloc[i,5]**2) # Zbb
        System_Data_Lines_Impedances.iloc[i,5] = math.atan(System_Data_Lines.iloc[i,5]/System_Data_Lines.iloc[i,4])         # Thbb
        System_Data_Lines_Impedances.iloc[i,6] = math.sqrt(System_Data_Lines.iloc[i,6]**2 + System_Data_Lines.iloc[i,7]**2) # Zcc
        System_Data_Lines_Impedances.iloc[i,7] = math.atan(System_Data_Lines.iloc[i,7]/System_Data_Lines.iloc[i,6])         # Thcc
        System_Data_Lines_Impedances.iloc[i,8] = math.sqrt(System_Data_Lines.iloc[i,8]**2 + System_Data_Lines.iloc[i,9]**2) # Zab
        System_Data_Lines_Impedances.iloc[i,9] = math.atan(System_Data_Lines.iloc[i,9]/System_Data_Lines.iloc[i,8])         # Thab
        System_Data_Lines_Impedances.iloc[i,10] = math.sqrt(System_Data_Lines.iloc[i,10]**2 + System_Data_Lines.iloc[i,11]**2) # Zac
        System_Data_Lines_Impedances.iloc[i,11] = math.atan(System_Data_Lines.iloc[i,11]/System_Data_Lines.iloc[i,10])         # Thac
        System_Data_Lines_Impedances.iloc[i,12] = math.sqrt(System_Data_Lines.iloc[i,12]**2 + System_Data_Lines.iloc[i,13]**2) # Zbc
        System_Data_Lines_Impedances.iloc[i,13] = math.atan(System_Data_Lines.iloc[i,13]/System_Data_Lines.iloc[i,12])         # Thbc
    
    System_Data_Lines_Prima = pd.DataFrame(0.0, index = System_Data_Lines.index, columns = ['FROM', 'TO', 'Raa_p', 'Xaa_p', 'Rbb_p', 'Xbb_p', 'Rcc_p', 'Xcc_p', 'Rab_p', 'Xab_p', 'Rac_p', 'Xac_p', 'Rbc_p', 'Xbc_p', 'Rba_p', 'Xba_p', 'Rca_p', 'Xca_p', 'Rcb_p' ,'Xcb_p', 'Imax'])
    System_Data_Lines_Prima['FROM'] =  System_Data_Lines['FROM'] 
    System_Data_Lines_Prima['TO'] =  System_Data_Lines['TO'] 
    System_Data_Lines_Prima['Imax'] =  System_Data_Lines['Imax']
    for i in System_Data_Lines_Prima.index:
        System_Data_Lines_Prima.iloc[i,2] = System_Data_Lines_Impedances.iloc[i,2]*math.cos(System_Data_Lines_Impedances.iloc[i,3] + Tha0 - Tha0) # Raa_p
        System_Data_Lines_Prima.iloc[i,3] = System_Data_Lines_Impedances.iloc[i,2]*math.sin(System_Data_Lines_Impedances.iloc[i,3] + Tha0 - Tha0) # Xaa_p
        System_Data_Lines_Prima.iloc[i,4] = System_Data_Lines_Impedances.iloc[i,4]*math.cos(System_Data_Lines_Impedances.iloc[i,5] + Thb0 - Thb0) # Rbb_p
        System_Data_Lines_Prima.iloc[i,5] = System_Data_Lines_Impedances.iloc[i,4]*math.sin(System_Data_Lines_Impedances.iloc[i,5] + Thb0 - Thb0) # Xbb_p
        System_Data_Lines_Prima.iloc[i,6] = System_Data_Lines_Impedances.iloc[i,6]*math.cos(System_Data_Lines_Impedances.iloc[i,7] + Thc0 - Thc0) # Rcc_p
        System_Data_Lines_Prima.iloc[i,7] = System_Data_Lines_Impedances.iloc[i,6]*math.sin(System_Data_Lines_Impedances.iloc[i,7] + Thc0 - Thc0) # Xcc_p
        System_Data_Lines_Prima.iloc[i,8] = System_Data_Lines_Impedances.iloc[i,8]*math.cos(System_Data_Lines_Impedances.iloc[i,9] + Thb0 - Tha0) # Rab_p
        System_Data_Lines_Prima.iloc[i,9] = System_Data_Lines_Impedances.iloc[i,8]*math.sin(System_Data_Lines_Impedances.iloc[i,9] + Thb0 - Tha0) # Xab_p
        System_Data_Lines_Prima.iloc[i,10] = System_Data_Lines_Impedances.iloc[i,10]*math.cos(System_Data_Lines_Impedances.iloc[i,11] + Thc0 - Tha0) # Rac_p
        System_Data_Lines_Prima.iloc[i,11] = System_Data_Lines_Impedances.iloc[i,10]*math.sin(System_Data_Lines_Impedances.iloc[i,11] + Thc0 - Tha0) # Xac_p
        System_Data_Lines_Prima.iloc[i,12] = System_Data_Lines_Impedances.iloc[i,12]*math.cos(System_Data_Lines_Impedances.iloc[i,13] + Thc0 - Thb0) # Rbc_p
        System_Data_Lines_Prima.iloc[i,13] = System_Data_Lines_Impedances.iloc[i,12]*math.sin(System_Data_Lines_Impedances.iloc[i,13] + Thc0 - Thb0) # Xbc_p
        System_Data_Lines_Prima.iloc[i,14] = System_Data_Lines_Impedances.iloc[i,8]*math.cos(System_Data_Lines_Impedances.iloc[i,9] + Tha0 - Thb0) # Rba_p
        System_Data_Lines_Prima.iloc[i,15] = System_Data_Lines_Impedances.iloc[i,8]*math.sin(System_Data_Lines_Impedances.iloc[i,9] + Tha0 - Thb0) # Xba_p
        System_Data_Lines_Prima.iloc[i,16] = System_Data_Lines_Impedances.iloc[i,10]*math.cos(System_Data_Lines_Impedances.iloc[i,11] + Tha0 - Thc0) # Rca_p
        System_Data_Lines_Prima.iloc[i,17] = System_Data_Lines_Impedances.iloc[i,10]*math.sin(System_Data_Lines_Impedances.iloc[i,11] + Tha0 - Thc0) # Xca_p
        System_Data_Lines_Prima.iloc[i,18] = System_Data_Lines_Impedances.iloc[i,12]*math.cos(System_Data_Lines_Impedances.iloc[i,13] + Thb0 - Thc0) # Rcb_p
        System_Data_Lines_Prima.iloc[i,19] = System_Data_Lines_Impedances.iloc[i,12]*math.sin(System_Data_Lines_Impedances.iloc[i,13] + Thb0 - Thc0) # Xcb_p
        
    return System_Data_Lines_Prima