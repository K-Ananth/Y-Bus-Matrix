nb=int(input("Enter the number of buses including reference bus              :"))
ne=int(input("Enter the number of elements                                   :"))
nla=int(input("Enter the number of elements have line charging admittance     :"))
mat=[]
lca=[]
ybus=[]

def end1():
    print ("INVALID DATA !")
    exit()

for i in range(nb):
    ybus.extend([[0]])
    for j in range(nb-1):
        ybus[i].extend([0])
#print(ybus)

if nla>0:
   opl=input("Enter whether the line charging  values are line charging admittance or half line charging admittance (LA/HLA) :")
   if((opl!='la'and opl!='LA') and(opl!='hla'and opl!='HLA')):
        end1()
   opa=input("Enter whether the line charging values are in Impedance or Admittance (Z/Y) :")

   if((opa!='z'and opa!='Z') and(opa!='y'and opa!='Y')):
       end1()

op=input("Enter whether the values are in Impedance or Admittance (Z/Y) :")
if((op!='z'and op!='Z') and(op!='y'and op!='Y')):
       end1()

print("Enter the connections between buses :")
print("-------------------")
for i in range(ne):
        F=int(input("FROM :"))
        T=int(input("TO   :"))
        if F==T:
           End1()
        X=float(input("Real Part      :"))
        Y=float(input("Imaginary part :"))
        Vr=complex(X,Y)
        if (op=='z'or op=='Z'):
           V=1/Vr
        if (op=='y'or op=='Y'):
           V=Vr
        mat.extend([[F,T,V]])
        print("-------------------")

for i in range(ne):
    print(mat[i])

print ("*******************")
for i in range(nla):
    f=int(input("FROM :"))
    t=int(input("TO   :"))
    if t==f:
       end1()
    x=float(input("Real Part      :"))
    y=float(input("Imaginary part :"))
    vr=complex(x,y)
    if (opa=='z'or opa=='Z'):
       v=1/vr
    if (opa=='y'or opa=='Y'):
       v=vr
    if (opl=='la' or opl=='LA'):
       v=vr/2
    lca.extend([[f,t,v]])
    print("-------------------")

for i in range(nla):
    print(lca[i])

print ("*******************")

for k in range(nb+1):
    for I in range(ne):
        for j in range(2):
           if(k==mat[i][j]):
             #print(mat[i][j],"@@@@@@@@@",k)
             ybus[k-1][k-1]=ybus[k-1][k-1]+mat[i][2]

for i in range(1,nb+1):
    for j in range(1,nb+1):
       if i!=j:
          for a in range(ne):
              #print(I,j, "₹₹₹₹",mat[a][0],mat[a][1])
              if(i==mat[a][0])and(j==mat[a][1]):
                 #print(I,j,"::::::",mat[a][0],mat[a][1])
                 ybus[i-1][j-1]=(-1)*mat[a][2]
                 ybus[j-1][i-1]=(-1)*mat[a][2]

for u in range(nla):
    for v in range(2):
        for i in range(1,nb+1):
            for j in range(1,nb+1):
                #print(I,j,"-----"",u,v)
                if (i==lca[u][v]or j==lca[u][v]):
                   #print(I,j,"++++++",u,v)
                   ybus[i-1][j-1]=ybus[i-1][j-1]+lca[u][2]

n=0
for i in range(ne):
    for j in range(2):
        #print(I,j)
        if mat[i][j]==0:
           n=1
           break
if n==1:
   for i in range(nb-1):
           del ybus[i][nb-1]
   del ybus[nb-1]

print("Y bus :")

for i in range(nb-n):
     print(ybus[i])