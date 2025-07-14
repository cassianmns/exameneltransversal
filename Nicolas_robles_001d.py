datos ={"productos":[
        {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
        }
    ]
}
datosstock={"Stock":[
        {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
        }
    ]
}
stock_hp=2
stock_asus=2
stock_lenovo=3
stock_dell=0

def validar_num_entero(mensaje:str)->int:
    while True:
        try:
            num=int(input(mensaje))
            if num <0:
                print("Error, Ingrese numero entero.")
                continue
            return num
        except ValueError:
            print("Error, ingrese caracter valido.")
def valida_texto_vacio(mensaje:str):
    while True:
        texto=input(mensaje)
        if len(texto)==0:
            print("El texto no debe estar vacio.")
            continue
        return texto
def validar_marca(mensaje:str):
    while True:
        marca=valida_texto_vacio(mensaje).upper()
        if marca == "HP" or marca =="Lenovo" or marca =="Asus" or marca =="Dell":
            return marca
        else:
            print("Debe ingresar marca valida.")
            continue
def stock_marca(mensaje:str):
    validar_marca()
    for i in datos['productos']:
        for j in datos:
            if i ==j:
                print(f"{datos['productos']}")

def buscar_marca(mensaje:str):
    while True:
        for i in datos['productos']:
            if i["marca"]==datos['productos']:
                return True
            else:
                return False
def buscar_precio(precio_id:str):
    for i in datos["productos"]:
        if i["precio_id"]==precio_id:
            return i
def validar_precio(mensaje:str)->int:
    while True:
        try:
            precio=int(input(mensaje))
            if precio <0:
                print("Error, Ingrese numero entero.")
                continue
        except ValueError:
            print("Error, ingrese caracter valido.")

while True:
    print("***MENU PRINCIPAL***")
    print("[1] Stock marca.")
    print("[2] Busqueda por precio.")
    print("[3] Actualizar precio.")
    print("[4] Salir.")

    opc=validar_num_entero("Ingrese una opcion: ")
    if opc ==1:
        marca=validar_marca("Ingrese marca:")
        if marca=="HP":
            print(f"Stock disponible es de {stock_hp}")
        elif marca=="Lenovo":
            print(f"Stock disponible es de {stock_lenovo}")
        elif marca=="Asus":
            print(f"Stock disponible es de {stock_asus}")
        elif marca=="Dell":
            print(f"Stock disponible es de {stock_dell}")
        else:
            print("Marca no existente ")
                
    elif opc==2:
        print("Opcion 2")
        precio_min=(input("Ingrese precio minimo: "))
        precio_max=(input("Ingrese precio maximo: "))
        print(f"Stock de productos :{datosstock['Stock']}")
        
    elif opc==3:
        print("Opcion 3")
    elif opc==4:
        print("Salir")
        break
    else:
        print("Error, ingrese opcion valida.")
