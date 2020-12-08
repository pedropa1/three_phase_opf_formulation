
def print_results(model, V0):
    print('--------------------------------------------------------------------')
    print('\t\tPhA\t\tPhB\t\tPhC\t\tTotal')
    print('--------------------------------------------------------------------')
    print("PD\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.PDa[i].value for i in model.N),sum(model.PDb[i].value for i in model.N),sum(model.PDc[i].value for i in model.N),sum(model.PDa[i].value + model.PDb[i].value+ model.PDc[i].value  for i in model.N)))
    print("PS\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.PSa[i].value for i in model.N),sum(model.PSb[i].value for i in model.N),sum(model.PSc[i].value for i in model.N),sum(model.PSa[i].value + model.PSb[i].value+ model.PSc[i].value  for i in model.N)))
    print("Plss\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.Plss_a[i,j].value for i,j in model.L),sum(model.Plss_b[i,j].value for i,j in model.L),sum(model.Plss_c[i,j].value for i,j in model.L),sum(model.Plss_a[i,j].value + model.Plss_b[i,j].value + model.Plss_c[i,j].value  for i,j in model.L)))
    print('--------------------------------------------------------------------')
    print("QD\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.QDa[i].value for i in model.N),sum(model.QDb[i].value for i in model.N),sum(model.QDc[i].value for i in model.N),sum(model.QDa[i].value + model.QDb[i].value+ model.QDc[i].value  for i in model.N)))
    print("QS\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.QSa[i].value for i in model.N),sum(model.QSb[i].value for i in model.N),sum(model.QSc[i].value for i in model.N),sum(model.QSa[i].value + model.QSb[i].value+ model.QSc[i].value  for i in model.N)))
    print("Qlss\t\t%0.2f\t\t%0.2f\t\t%0.2f\t\t%0.2f"%(sum(model.Qlss_a[i,j].value for i,j in model.L),sum(model.Qlss_b[i,j].value for i,j in model.L),sum(model.Qlss_c[i,j].value for i,j in model.L),sum(model.Qlss_a[i,j].value + model.Qlss_b[i,j].value + model.Qlss_c[i,j].value  for i,j in model.L)))
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    print('i\tVa\t\tVb\t\tVc')
    print('--------------------------------------------------------------------') 
    for i in model.N:
        print("%i\t%0.5f\t\t%0.5f\t\t%0.5f"%(i,model.Va[i].value/V0,model.Vb[i].value/V0,model.Vc[i].value/V0))


