#auto: guadalupe castro 
#fecha: marzo 18/2023
# programa que valida, nombre, eddad y correo
#============================================================
while True:
    menu=""" 
    bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del del 1 al 3:
    [1] digitar su nombre
    [2] digitar su edad 
    [3] digitar su correo electronico 
    """
    print(menu)
    opcion=input('entre la opcion 1 , 2 o 3')
    if opcion== "1":
        while True():
          nombre=input('digite su nombre: ')
          if nombre.isalpha():
           print("su nombre es:",nombre)
    
          else:
           print("su nombre esta mal digitado")
    #=========================================
    elif opcion=='2':
      while True():
         edad=input('ingrese su edad:')
         if edad.isnumeric():
           print('su edad es:',edad)
         else:
           print('no ingresaste bien tu edad')
    #==============================================
    elif opcion=='3':
      while True():
        correo=input('ingrese su correo electronico')
        if correo.find('@')==1 and correo.find('.')>=0:
              print('tu correo es: ',correo)
        else:
               print('metiste mal tu correo')
    elif opcion=='4':
      exit()