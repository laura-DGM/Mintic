N=int(input())
producto=[]
nom=[]
vt=0
ivaT=0
for i in range(0,N):
    codigo=int(input())
    nombre=input()
    cantidad=float(input())
    valor_Uni=float(input())
    iva_op=int(input())
    valor=valor_Uni*cantidad
    if iva_op==1:
        iva=0
    elif iva_op==2:
        iva=0.05
    elif iva_op==3:
        iva=0.19
    vt+=valor*iva+valor
    ivaT+=valor*iva
    print(codigo)
    print(nombre)
    print(valor)
    print(valor*iva+valor)
print(vt)
if (ivaT==0):
    ivaT=0
    print(ivaT)
else:
    print(ivaT)
