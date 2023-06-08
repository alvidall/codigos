rut=[]
nombre=[]
edad=[]

while True:
    
    rutalumno= input("ingrese rut alumno:     fin= 0 :")
    if rutalumno=="0":
        break
    nombalumno=input("ingrese nombre alumno: ")
    edadalumno=input("ingrese edad alumno: ")
   
    rut.append(rutalumno)
    nombre.append(nombalumno)
    edad.append(edadalumno)

for i in range(len(rut)):
    print(f"{rut[i]\t} {nombre[i]}  {edad[i]} " )