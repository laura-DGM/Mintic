N=int(input())
cod=[]
can=[]
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}


ts_iva=[]
totals=[]
ivas=[]
for i in range(N):
    cod_p=int(input())
    cod.append(cod_p)
    cant=float(input())
    can.append(cant)
    t_iva=int(input())
    ts_iva.append(t_iva)

for i in range(N):
    print(cod[i])
    print(articulos[cod[i]])
    print(can[i]*precios[cod[i]])
    if ts_iva[i]==1:
        print(can[i]*precios[cod[i]])
        totals.append(can[i]*precios[cod[i]])
    elif ts_iva[i]==2:
        print(can[i]*precios[cod[i]]*1.05)
        totals.append(can[i]*precios[cod[i]]*1.05)
        ivas.append(can[i]*precios[cod[i]]*0.05)
    else:
        print(can[i]*precios[cod[i]]*1.19)
        totals.append(can[i]*precios[cod[i]]*1.19)
        ivas.append(can[i]*precios[cod[i]]*0.19)
    
print(sum(totals))
print(sum(ivas))
