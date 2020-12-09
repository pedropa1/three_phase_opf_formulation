# %% Upload Libraries
from pyomo.environ import *

def three_phase_opf_model(V0, Data_Network):

    #%% Data Processing
    N = Data_Network[0]
    L = Data_Network[1]
    Tn = Data_Network[2]
    
    # Power
    PDa = Data_Network[3]
    PDb = Data_Network[4]
    PDc = Data_Network[5]
    QDa = Data_Network[6]
    QDb = Data_Network[7]
    QDc = Data_Network[8]
    
    # Impedances Prima
    Raa_p = Data_Network[9]
    Xaa_p = Data_Network[10]
    Rbb_p = Data_Network[11]
    Xbb_p = Data_Network[12]
    Rcc_p = Data_Network[13]
    Xcc_p = Data_Network[14]
    Rab_p = Data_Network[15]
    Xab_p = Data_Network[16]
    Rac_p = Data_Network[17]
    Xac_p = Data_Network[18]
    Rbc_p = Data_Network[19]
    Xbc_p = Data_Network[20]
    Rba_p = Data_Network[21]
    Xba_p = Data_Network[22]
    Rca_p = Data_Network[23]
    Xca_p = Data_Network[24]
    Rcb_p = Data_Network[25]
    Xcb_p = Data_Network[26]
    Imax = Data_Network[27]
    
    #%% Type of Model
    model = ConcreteModel()
    #%% Define Sets
    model.N = Set(initialize=N)    # Set of Nodes
    model.L = Set(initialize=L)    # Set of lines 
    
    # Define Parameters
    model.Tn = Param(model.N, initialize=Tn, mutable=True)    # Type of node. SS node == 1
    model.V0 = Param(initialize=V0, mutable=True)
    
    # Network Parameters
    model.Raa_p = Param(model.L, initialize=Raa_p, mutable=True)
    model.Xaa_p = Param(model.L, initialize=Xaa_p, mutable=True)
    model.Rbb_p = Param(model.L, initialize=Rbb_p, mutable=True)
    model.Xbb_p = Param(model.L, initialize=Xbb_p, mutable=True)
    model.Rcc_p = Param(model.L, initialize=Rcc_p, mutable=True)
    model.Xcc_p = Param(model.L, initialize=Xcc_p, mutable=True)
    model.Rab_p = Param(model.L, initialize=Rab_p, mutable=True)
    model.Xab_p = Param(model.L, initialize=Xab_p, mutable=True)
    model.Rac_p = Param(model.L, initialize=Rac_p, mutable=True)
    model.Xac_p = Param(model.L, initialize=Xac_p, mutable=True)
    model.Rbc_p = Param(model.L, initialize=Rbc_p, mutable=True)
    model.Xbc_p = Param(model.L, initialize=Xbc_p, mutable=True)
    model.Rba_p = Param(model.L, initialize=Rba_p, mutable=True)
    model.Xba_p = Param(model.L, initialize=Xba_p, mutable=True)
    model.Rca_p = Param(model.L, initialize=Rca_p, mutable=True)
    model.Xca_p = Param(model.L, initialize=Xca_p, mutable=True)
    model.Rcb_p = Param(model.L, initialize=Rcb_p, mutable=True)
    model.Xcb_p = Param(model.L, initialize=Xcb_p, mutable=True)   
    model.Imax = Param(model.L, initialize=Imax, mutable=True)
    
    # Active and Reactive Demand Power
    model.PDa = Param(model.N, initialize=PDa, mutable=True)
    model.PDb = Param(model.N, initialize=PDb, mutable=True)
    model.PDc = Param(model.N, initialize=PDc, mutable=True)
    model.QDa = Param(model.N, initialize=QDa, mutable=True)
    model.QDb = Param(model.N, initialize=QDb, mutable=True)
    model.QDc = Param(model.N, initialize=QDc, mutable=True)
    
    # Define Varibles
    # --------------------------------------------
    # Voltages 
    # --------------------------------------------
    def Va_init_rule(model, i):
        if model.Tn[i] == 1:
            temp = model.V0
            model.Va[i].fixed = True
        else:
            temp = model.V0
            model.Va[i].fixed = False
        return temp
    model.Va = Var(model.N, initialize = Va_init_rule)  # Voltage Phase A
    
    def Vb_init_rule(model, i):
        if model.Tn[i] == 1:
            temp = model.V0
            model.Vb[i].fixed = True
        else:
            temp = model.V0
            model.Vb[i].fixed = False
        return temp
    model.Vb = Var(model.N, initialize = Vb_init_rule)  # Voltage Phase B
    
    def Vc_init_rule(model, i):
        if model.Tn[i] == 1:
            temp = model.V0
            model.Vc[i].fixed = True
        else:
            temp = model.V0
            model.Vc[i].fixed = False
        return temp
    model.Vc = Var(model.N, initialize = Vc_init_rule)  # Voltage Phase C
    
    # --------------------------------------------
    # Power 
    # --------------------------------------------
    
    # Active and Reactive Power of the Substation
    def PSa_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.PSa[i].fixed = True
        else:
            temp = 0
            model.PSa[i].fixed = False
        return temp
    model.PSa = Var(model.N, initialize = PSa_init_rule)  # Active Power SS Phase A
    
    def PSb_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.PSb[i].fixed = True
        else:
            temp = 0
            model.PSb[i].fixed = False
        return temp
    model.PSb = Var(model.N, initialize = PSb_init_rule)  # Active Power SS Phase B
    
    def PSc_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.PSc[i].fixed = True
        else:
            temp = 0
            model.PSc[i].fixed = False
        return temp
    model.PSc = Var(model.N, initialize = PSc_init_rule)  # Active Power SS Phase C
    
    def QSa_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.QSa[i].fixed = True
        else:
            temp = 0
            model.QSa[i].fixed = False
        return temp
    model.QSa = Var(model.N, initialize = QSa_init_rule)  # Reactive Power SS Phase A
    
    def QSb_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.QSb[i].fixed = True
        else:
            temp = 0
            model.QSb[i].fixed = False
        return temp
    model.QSb = Var(model.N, initialize = QSb_init_rule)  # Reactive Power SS Phase A
    
    def QSc_init_rule(model, i):
        if model.Tn[i] == 0:
            temp = 0
            model.QSc[i].fixed = True
        else:
            temp = 0
            model.QSc[i].fixed = False
        return temp
    model.QSc = Var(model.N, initialize = QSc_init_rule)  # Reactive Power SS Phase A
    
    # Active and Reactive Power of Lines
    model.Pa = Var(model.L, initialize=0)
    model.Pb = Var(model.L, initialize=0)
    model.Pc = Var(model.L, initialize=0)
    model.Qa = Var(model.L, initialize=0)
    model.Qb = Var(model.L, initialize=0)
    model.Qc = Var(model.L, initialize=0)
    
    # Active and Reactive Power Losses of Lines
    model.Plss_a = Var(model.L, initialize=0)
    model.Plss_b = Var(model.L, initialize=0)
    model.Plss_c = Var(model.L, initialize=0)
    model.Qlss_a = Var(model.L, initialize=0)
    model.Qlss_b = Var(model.L, initialize=0)
    model.Qlss_c = Var(model.L, initialize=0)
      
    
    #%% Define the Objective Fuction
    def Total_Active_Losses(model):
        return (sum(model.Plss_a[i,j] + model.Plss_b[i,j] + model.Plss_c[i,j] for i,j in model.L))
    model.obj = Objective(rule=Total_Active_Losses)
    
    #%% Define the Operational Constraints
    
    # ---------------------------------------------------------------
    # Define Active Power Losses
    # --------------------------------------------------------------
    def active_power_losses_phase_A_rule(model, i,j):
        return (model.Plss_a[i,j] ==   (1/(model.Va[i]*model.Va[i]))*(model.Raa_p[i,j]*model.Pa[i,j]*model.Pa[i,j] + model.Raa_p[i,j]*model.Qa[i,j]*model.Qa[i,j] +\
                                                                      model.Xaa_p[i,j]*model.Pa[i,j]*model.Qa[i,j] - model.Xaa_p[i,j]*model.Qa[i,j]*model.Pa[i,j]) +\
                                       (1/(model.Va[i]*model.Vb[i]))*(model.Rab_p[i,j]*model.Pb[i,j]*model.Pa[i,j] + model.Rab_p[i,j]*model.Qb[i,j]*model.Qa[i,j] +\
                                                                      model.Xab_p[i,j]*model.Pb[i,j]*model.Qa[i,j] - model.Xab_p[i,j]*model.Qb[i,j]*model.Pa[i,j]) +\
                                       (1/(model.Va[i]*model.Vc[i]))*(model.Rac_p[i,j]*model.Pc[i,j]*model.Pa[i,j] + model.Rac_p[i,j]*model.Qc[i,j]*model.Qa[i,j] +\
                                                                      model.Xac_p[i,j]*model.Pc[i,j]*model.Qa[i,j] - model.Xac_p[i,j]*model.Qc[i,j]*model.Pa[i,j]))                
    model.active_power_losses_phase_A = Constraint(model.L, rule=active_power_losses_phase_A_rule)
    
    def active_power_losses_phase_B_rule(model, i,j):
        return(model.Plss_b[i,j] == (1/(model.Vb[i]*model.Va[i]))*(model.Rba_p[i,j]*model.Pa[i,j]*model.Pb[i,j] + model.Rba_p[i,j]*model.Qa[i,j]*model.Qb[i,j] +\
                                                                   model.Xba_p[i,j]*model.Pa[i,j]*model.Qb[i,j] - model.Xba_p[i,j]*model.Qa[i,j]*model.Pb[i,j]) +\
                                    (1/(model.Vb[i]*model.Vb[i]))*(model.Rbb_p[i,j]*model.Pb[i,j]*model.Pb[i,j] + model.Rbb_p[i,j]*model.Qb[i,j]*model.Qb[i,j] +\
                                                                   model.Xbb_p[i,j]*model.Pb[i,j]*model.Qb[i,j] - model.Xbb_p[i,j]*model.Qb[i,j]*model.Pb[i,j]) +\
                                    (1/(model.Vb[i]*model.Vc[i]))*(model.Rbc_p[i,j]*model.Pc[i,j]*model.Pb[i,j] + model.Rbc_p[i,j]*model.Qc[i,j]*model.Qb[i,j] +\
                                                                   model.Xbc_p[i,j]*model.Pc[i,j]*model.Qb[i,j] - model.Xbc_p[i,j]*model.Qc[i,j]*model.Pb[i,j]))
    model.active_power_losses_phase_B = Constraint(model.L, rule=active_power_losses_phase_B_rule)

    def active_power_losses_phase_C_rule(model, i,j):
        return(model.Plss_c[i,j] == (1/(model.Vc[i]*model.Va[i]))*(model.Rca_p[i,j]*model.Pa[i,j]*model.Pc[i,j] + model.Rca_p[i,j]*model.Qa[i,j]*model.Qc[i,j] +\
                                                                   model.Xca_p[i,j]*model.Pa[i,j]*model.Qc[i,j] - model.Xca_p[i,j]*model.Qa[i,j]*model.Pc[i,j]) +\
                                    (1/(model.Vc[i]*model.Vb[i]))*(model.Rcb_p[i,j]*model.Pb[i,j]*model.Pc[i,j] + model.Rcb_p[i,j]*model.Qb[i,j]*model.Qc[i,j] +\
                                                                   model.Xcb_p[i,j]*model.Pb[i,j]*model.Qc[i,j] - model.Xcb_p[i,j]*model.Qb[i,j]*model.Pc[i,j]) +\
                                    (1/(model.Vc[i]*model.Vc[i]))*(model.Rcc_p[i,j]*model.Pc[i,j]*model.Pc[i,j] + model.Rcc_p[i,j]*model.Qc[i,j]*model.Qc[i,j] +\
                                                                   model.Xcc_p[i,j]*model.Pc[i,j]*model.Qc[i,j] - model.Xcc_p[i,j]*model.Qc[i,j]*model.Pc[i,j]))
    model.active_power_losses_phase_C = Constraint(model.L, rule=active_power_losses_phase_C_rule)  
    
    # ---------------------------------------------------------------
    # Define Reactive Power Losses
    # ---------------------------------------------------------------  
    
    def reactive_power_losses_phase_A_rule(model, i,j):
        return(model.Qlss_a[i,j] == (1/(model.Va[i]*model.Va[i]))*(-model.Raa_p[i,j]*model.Pa[i,j]*model.Qa[i,j] + model.Raa_p[i,j]*model.Qa[i,j]*model.Pa[i,j] +\
                                                                    model.Xaa_p[i,j]*model.Pa[i,j]*model.Pa[i,j] + model.Xaa_p[i,j]*model.Qa[i,j]*model.Qa[i,j]) +\
                                    (1/(model.Va[i]*model.Vb[i]))*(-model.Rab_p[i,j]*model.Pb[i,j]*model.Qa[i,j] + model.Rab_p[i,j]*model.Qb[i,j]*model.Pa[i,j] +\
                                                                    model.Xab_p[i,j]*model.Pb[i,j]*model.Pa[i,j] + model.Xab_p[i,j]*model.Qb[i,j]*model.Qa[i,j]) +\
                                    (1/(model.Va[i]*model.Vc[i]))*(-model.Rac_p[i,j]*model.Pc[i,j]*model.Qa[i,j] + model.Rac_p[i,j]*model.Qc[i,j]*model.Pa[i,j] +\
                                                                    model.Xac_p[i,j]*model.Pc[i,j]*model.Pa[i,j] + model.Xac_p[i,j]*model.Qc[i,j]*model.Qa[i,j]))
    model.reactive_power_losses_phase_A = Constraint(model.L, rule=reactive_power_losses_phase_A_rule)
    
    def reactive_power_losses_phase_B_rule(model, i,j):
        return(model.Qlss_b[i,j] == (1/(model.Vb[i]*model.Va[i]))*(-model.Rba_p[i,j]*model.Pa[i,j]*model.Qb[i,j] + model.Rba_p[i,j]*model.Qa[i,j]*model.Pb[i,j] +\
                                                                    model.Xba_p[i,j]*model.Pa[i,j]*model.Pb[i,j] + model.Xba_p[i,j]*model.Qa[i,j]*model.Qb[i,j]) +\
                                    (1/(model.Vb[i]*model.Vb[i]))*(-model.Rbb_p[i,j]*model.Pb[i,j]*model.Qb[i,j] + model.Rbb_p[i,j]*model.Qb[i,j]*model.Pb[i,j] +\
                                                                    model.Xbb_p[i,j]*model.Pb[i,j]*model.Pb[i,j] + model.Xbb_p[i,j]*model.Qb[i,j]*model.Qb[i,j]) +\
                                    (1/(model.Vb[i]*model.Vc[i]))*(-model.Rbc_p[i,j]*model.Pc[i,j]*model.Qb[i,j] + model.Rbc_p[i,j]*model.Qc[i,j]*model.Pb[i,j] +\
                                                                    model.Xbc_p[i,j]*model.Pc[i,j]*model.Pb[i,j] + model.Xbc_p[i,j]*model.Qc[i,j]*model.Qb[i,j]))
    model.reactive_power_losses_phase_B = Constraint(model.L, rule=reactive_power_losses_phase_B_rule)
    
    def reactive_power_losses_phase_C_rule(model, i,j):
        return(model.Qlss_c[i,j] == (1/(model.Vc[i]*model.Va[i]))*(-model.Rca_p[i,j]*model.Pa[i,j]*model.Qc[i,j] + model.Rca_p[i,j]*model.Qa[i,j]*model.Pc[i,j] +\
                                                                    model.Xca_p[i,j]*model.Pa[i,j]*model.Pc[i,j] + model.Xca_p[i,j]*model.Qa[i,j]*model.Qc[i,j]) +\
                                    (1/(model.Vc[i]*model.Vb[i]))*(-model.Rcb_p[i,j]*model.Pb[i,j]*model.Qc[i,j] + model.Rcb_p[i,j]*model.Qb[i,j]*model.Pc[i,j] +\
                                                                    model.Xcb_p[i,j]*model.Pb[i,j]*model.Pc[i,j] + model.Xcb_p[i,j]*model.Qb[i,j]*model.Qc[i,j]) +\
                                    (1/(model.Vc[i]*model.Vc[i]))*(-model.Rcc_p[i,j]*model.Pc[i,j]*model.Qc[i,j] + model.Rcc_p[i,j]*model.Qc[i,j]*model.Pc[i,j] +\
                                                                    model.Xcc_p[i,j]*model.Pc[i,j]*model.Pc[i,j] + model.Xcc_p[i,j]*model.Qc[i,j]*model.Qc[i,j]))
    model.reactive_power_losses_phase_C = Constraint(model.L, rule=reactive_power_losses_phase_C_rule)
    
    # ---------------------------------------------------------------
    # Active Power Balance
    # ---------------------------------------------------------------
    
    def active_power_balance_phase_A_rule(model, k):
        return (sum(model.Pa[j,i] for j,i in model.L if i == k) - sum(model.Pa[i,j] + model.Plss_a[i,j] for i,j in model.L if i == k) + model.PSa[k] == model.PDa[k])
    model.active_power_balance_phase_A = Constraint(model.N, rule=active_power_balance_phase_A_rule)

    def active_power_balance_phase_B_rule(model, k):
        return (sum(model.Pb[j,i] for j,i in model.L if i == k) - sum(model.Pb[i,j] + model.Plss_b[i,j] for i,j in model.L if i == k) + model.PSb[k] == model.PDb[k])
    model.active_power_balance_phase_B = Constraint(model.N, rule=active_power_balance_phase_B_rule)

    def active_power_balance_phase_C_rule(model, k):
        return (sum(model.Pc[j,i] for j,i in model.L if i == k) - sum(model.Pc[i,j] + model.Plss_c[i,j] for i,j in model.L if i == k) + model.PSc[k] == model.PDc[k])
    model.active_power_balance_phase_C = Constraint(model.N, rule=active_power_balance_phase_C_rule)
    
    # ---------------------------------------------------------------
    # Reactive Power Balance
    # ---------------------------------------------------------------
    
    def reactive_power_balance_phase_A_rule(model, k):
        return (sum(model.Qa[j,i] for j,i in model.L if i == k) - sum(model.Qa[i,j] + model.Qlss_a[i,j] for i,j in model.L if i == k) + model.QSa[k] == model.QDa[k])
    model.reactive_power_balance_phase_A = Constraint(model.N, rule=reactive_power_balance_phase_A_rule)
    
    def reactive_power_balance_phase_B_rule(model, k):
        return (sum(model.Qb[j,i] for j,i in model.L if i == k) - sum(model.Qb[i,j] + model.Qlss_b[i,j] for i,j in model.L if i == k) + model.QSb[k] == model.QDb[k])
    model.reactive_power_balance_phase_B = Constraint(model.N, rule=reactive_power_balance_phase_B_rule)

    def reactive_power_balance_phase_C_rule(model, k):
        return (sum(model.Qc[j,i] for j,i in model.L if i == k) - sum(model.Qc[i,j] + model.Qlss_c[i,j] for i,j in model.L if i == k) + model.QSc[k] == model.QDc[k])
    model.reactive_power_balance_phase_C = Constraint(model.N, rule=reactive_power_balance_phase_C_rule)

    # ---------------------------------------------------------------
    # Voltage Drop in Lines
    # ---------------------------------------------------------------
    
    def voltage_drop_phase_A_rule(model, i,j):
        return(model.Va[i]**2 - model.Va[j]**2 == 2*(model.Raa_p[i,j]*model.Pa[i,j] + model.Xaa_p[i,j]*model.Qa[i,j]) + 2*(model.Rab_p[i,j]*model.Pb[i,j] + model.Xab_p[i,j]*model.Qb[i,j]) +\
                                                  2*(model.Rac_p[i,j]*model.Pc[i,j] + model.Xac_p[i,j]*model.Qc[i,j]) -\
                                                (1/(model.Va[i]**2))*((model.Raa_p[i,j]*model.Pa[i,j] + model.Xaa_p[i,j]*model.Qa[i,j] +\
                                                                       model.Rab_p[i,j]*model.Pb[i,j] + model.Xab_p[i,j]*model.Qb[i,j] +\
                                                                       model.Rac_p[i,j]*model.Pc[i,j] + model.Xac_p[i,j]*model.Qc[i,j])**2)	-\
                                                (1/(model.Va[i]**2))*((model.Raa_p[i,j]*model.Qa[i,j] - model.Xaa_p[i,j]*model.Pa[i,j] +\
                                                                       model.Rab_p[i,j]*model.Qb[i,j] - model.Xab_p[i,j]*model.Pb[i,j] +\
                                                                       model.Rac_p[i,j]*model.Qc[i,j] - model.Xac_p[i,j]*model.Pc[i,j])**2))
    model.voltage_drop_phase_A = Constraint(model.L, rule=voltage_drop_phase_A_rule)
    
    def voltage_drop_phase_B_rule(model, i,j):
        return(model.Vb[i]**2 - model.Vb[j]**2 == 2*(model.Rab_p[i,j]*model.Pa[i,j] + model.Xab_p[i,j]*model.Qa[i,j]) + 2*(model.Rbb_p[i,j]*model.Pb[i,j] + model.Xbb_p[i,j]*model.Qb[i,j]) 	+\
                                                  2*(model.Rbc_p[i,j]*model.Pc[i,j] + model.Xbc_p[i,j]*model.Qc[i,j]) -\
                                                (1/(model.Vb[i]**2))*((model.Rba_p[i,j]*model.Pa[i,j] + model.Xba_p[i,j]*model.Qa[i,j] +\
                                                                       model.Rbb_p[i,j]*model.Pb[i,j] + model.Xbb_p[i,j]*model.Qb[i,j] +\
                                                                       model.Rbc_p[i,j]*model.Pc[i,j] + model.Xbc_p[i,j]*model.Qc[i,j])**2)	-\
                                                (1/(model.Vb[i]**2))*((model.Rba_p[i,j]*model.Qa[i,j] - model.Xba_p[i,j]*model.Pa[i,j] +\
                                                                       model.Rbb_p[i,j]*model.Qb[i,j] - model.Xbb_p[i,j]*model.Pb[i,j] +\
                                                                       model.Rbc_p[i,j]*model.Qc[i,j] - model.Xbc_p[i,j]*model.Pc[i,j])**2))
    model.voltage_drop_phase_B = Constraint(model.L, rule=voltage_drop_phase_B_rule)
    
    def voltage_drop_phase_C_rule(model, i,j):
        return(model.Vc[i]**2 - model.Vc[j]**2 == 2*(model.Rac_p[i,j]*model.Pa[i,j] + model.Xac_p[i,j]*model.Qa[i,j]) + 2*(model.Rbc_p[i,j]*model.Pa[i,j] + model.Xbc_p[i,j]*model.Qa[i,j]) +\
                                                  2*(model.Rcc_p[i,j]*model.Pc[i,j] + model.Xcc_p[i,j]*model.Qc[i,j]) -\
                                                (1/(model.Vc[i]**2))*((model.Rca_p[i,j]*model.Pa[i,j] + model.Xca_p[i,j]*model.Qa[i,j] +\
                                                                       model.Rcb_p[i,j]*model.Pb[i,j] + model.Xcb_p[i,j]*model.Qb[i,j] +\
                                                                       model.Rcc_p[i,j]*model.Pc[i,j] + model.Xcc_p[i,j]*model.Qc[i,j])**2)	-\
                                                (1/(model.Vc[i]**2))*((model.Rca_p[i,j]*model.Qa[i,j] - model.Xca_p[i,j]*model.Pa[i,j] +\
                                                                       model.Rcb_p[i,j]*model.Qb[i,j] - model.Xcb_p[i,j]*model.Pb[i,j] +\
                                                                       model.Rcc_p[i,j]*model.Qc[i,j] - model.Xcc_p[i,j]*model.Pc[i,j])**2))
    model.voltage_drop_phase_C = Constraint(model.L, rule=voltage_drop_phase_C_rule)
    
    return model


















