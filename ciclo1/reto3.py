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

print(len(cod))
print(len(nom))
print(len(can))
print(len(val))
print(len(ts_iva))

for i in range(N):
    print(cod[i])
    print(nom[i])
    print(can[i]*val[i])
    if ts_iva[i]==1:
        print(can[i]*val[i])
        totals.append(can[i]*val[i])
    elif ts_iva[i]==2:
        print(can[i]*val[i]*1.05)
        totals.append(can[i]*val[i]*1.05)
        ivas.append(can[i]*val[i]*0.05)
    else:
        print(can[i]*val[i]*1.19)
        totals.append(can[i]*val[i]*1.19)
        ivas.append(can[i]*val[i]*0.19)
print(sum(totals))
print(sum(ivas))

