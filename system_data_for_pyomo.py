
def system_data_for_pyomo(System_Data_Nodes, System_Data_Lines_Prima):
    # Network Data
    On = [System_Data_Nodes.loc[i,'On'] for i in System_Data_Nodes.index]
    Tb = {On[i]: System_Data_Nodes.loc[i,'Tb'] for i in System_Data_Nodes.index}
    PDa = {On[i]: System_Data_Nodes.loc[i,'PDa'] for i in System_Data_Nodes.index}      
    QDa = {On[i]: System_Data_Nodes.loc[i,'QDa'] for i in System_Data_Nodes.index} 
    PDb = {On[i]: System_Data_Nodes.loc[i,'PDb'] for i in System_Data_Nodes.index}      
    QDb = {On[i]: System_Data_Nodes.loc[i,'QDb'] for i in System_Data_Nodes.index} 
    PDc = {On[i]: System_Data_Nodes.loc[i,'PDc'] for i in System_Data_Nodes.index}      
    QDc = {On[i]: System_Data_Nodes.loc[i,'QDc'] for i in System_Data_Nodes.index}    
    Ol = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']) for i in System_Data_Lines_Prima.index}
    Raa_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Raa_p'] for i in System_Data_Lines_Prima.index}
    Xaa_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xaa_p'] for i in System_Data_Lines_Prima.index}
    Rbb_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rbb_p'] for i in System_Data_Lines_Prima.index}
    Xbb_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xbb_p'] for i in System_Data_Lines_Prima.index}
    Rcc_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rcc_p'] for i in System_Data_Lines_Prima.index}
    Xcc_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xcc_p'] for i in System_Data_Lines_Prima.index}
    Rab_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rab_p'] for i in System_Data_Lines_Prima.index}
    Xab_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xab_p'] for i in System_Data_Lines_Prima.index}
    Rac_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rac_p'] for i in System_Data_Lines_Prima.index}
    Xac_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xac_p'] for i in System_Data_Lines_Prima.index}
    Rbc_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rbc_p'] for i in System_Data_Lines_Prima.index}
    Xbc_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xbc_p'] for i in System_Data_Lines_Prima.index}
    Rba_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rba_p'] for i in System_Data_Lines_Prima.index}
    Xba_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xba_p'] for i in System_Data_Lines_Prima.index}
    Rca_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rca_p'] for i in System_Data_Lines_Prima.index}
    Xca_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xca_p'] for i in System_Data_Lines_Prima.index}
    Rcb_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Rcb_p'] for i in System_Data_Lines_Prima.index}
    Xcb_p = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Xcb_p'] for i in System_Data_Lines_Prima.index}     
    Imax = {(System_Data_Lines_Prima.loc[i,'FROM'],System_Data_Lines_Prima.loc[i,'TO']):System_Data_Lines_Prima.loc[i,'Imax'] for i in System_Data_Lines_Prima.index}
        
    Data_Network = [On, Ol, Tb, PDa, PDb, PDc, QDa, QDb, QDc, Raa_p, Xaa_p, Rbb_p, Xbb_p, Rcc_p, Xcc_p, Rab_p, Xab_p, Rac_p, Xac_p, Rbc_p, Xbc_p, Rba_p, Xba_p, Rca_p, Xca_p, Rcb_p, Xcb_p, Imax]
    
    return Data_Network