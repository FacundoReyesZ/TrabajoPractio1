"""
Argentina:    LLNNNLL
Brasil:       LLLNLNN
Bolivia:      LLNNNNN
Paraguay:     LLLLNNN
Uruguay:      LLLNNNN    """

# TODOS EXCEPTO BRASIL Y BOLIV , PEAJE DE 300 , BRASIL 400 , BOLIVIA 200  (PESOS ARG)
importe_final = 300
importe_basico = 300

patente = tuple(input("Ingrese la patente del vehiculo"))
tipo_vehiculo = int(input("Ingrese el tipo de vehiculo"))
if(tipo_vehiculo==0):
    tipo_vehiculo = "motocicleta"
    importe_final = importe_final * 0.5
    importe_basico = importe_basico * 0.5
if(tipo_vehiculo==1):
    tipo_vehiculo = "automovil"
else:
    tipo_vehiculo = "camion"
    importe_final = importe_final * 1.6
    importe_basico = importe_basico * 1.6



forma_pago = int(input("Ingrese la forma de pago"))
if(forma_pago == 1):
    forma_pago = "manual"
else:
    forma_pago = "telepeaje"
    importe_final = importe_final * 0.90

pais = int(input("Ingrese el pais "))
if(pais == 0):
    pais = "Argentina"
if(pais == 1):
    pais = "Brasil"
    importe_final = importe_final * 1.33
    importe_basico = importe_basico * 1.33
if(pais == 2):
    pais = "Bolivia"
    importe_final = importe_final * 0.67
    importe_basico = importe_basico * 0.67
if(pais == 3):
    pais = "Paraguay"
if (pais == 4):
    pais = "Uruguay"

distancia = float(input("Ingrese la distancia desde la ultima cabina"))



print(f"El pais de procedencia es {pais}")
print(f"El importe a abonar es: ${importe_basico}")
print(f"si abona con telepeaje su valor final es: ${importe_final}")



print(patente,tipo_vehiculo,forma_pago,pais,distancia)