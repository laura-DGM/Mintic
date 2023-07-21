N=int(input())
cod=[]
nom=[]
can=[]
val=[]
ts_iva=[]
totals=[]
ivas=[]
for i in range(N):
    cod_p=int(input())
    cod.append(cod_p)
    nom_p=input()
    nom.append(nom_p)
    cant=float(input())
    can.append(cant)
    valor=float(input())
    val.append(valor)
    t_iva=int(input())
    ts_iva.append(t_iva)
    
def imp():
    l=sorted(nom)
    for i in range(N):
        print(cod[nom.index(l[i])])
        if ts_iva[nom.index(l[i])]==1:
            print(int(can[nom.index(l[i])]*val[nom.index(l[i])]-can[nom.index(l[i])]*val[nom.index(l[i])]))
            print(can[nom.index(l[i])]*val[nom.index(l[i])])
            print(can[nom.index(l[i])]*val[nom.index(l[i])])
            totals.append(can[nom.index(l[i])]*val[nom.index(l[i])])
        elif ts_iva[nom.index(l[i])]==2:
            print(can[nom.index(l[i])]*val[nom.index(l[i])]*1.05-can[nom.index(l[i])]*val[nom.index(l[i])])
            print(can[nom.index(l[i])]*val[nom.index(l[i])])
            print(can[nom.index(l[i])]*val[nom.index(l[i])]*1.05)
            totals.append(can[nom.index(l[i])]*val[nom.index(l[i])]*1.05)
            ivas.append(can[nom.index(l[i])]*val[nom.index(l[i])]*0.05)
        else:
            print(can[nom.index(l[i])]*val[nom.index(l[i])]*1.19-can[nom.index(l[i])]*val[nom.index(l[i])])
            print(can[nom.index(l[i])]*val[nom.index(l[i])])
            print(can[nom.index(l[i])]*val[nom.index(l[i])]*1.19)
            totals.append(can[nom.index(l[i])]*val[nom.index(l[i])]*1.19)
            ivas.append(can[nom.index(l[i])]*val[nom.index(l[i])]*0.19)
imp()
    
print(sum(totals))
print(sum(ivas))
