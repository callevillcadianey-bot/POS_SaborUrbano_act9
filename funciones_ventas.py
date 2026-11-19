# ==========================================
# 2. FUNCIONES DE VENTAS CON LÓGICA DE NEGOCIO (MODULARIDAD)
# ==========================================
from funciones_interfaz import *

def ingresar_productos():
    """Pide precios al usuario hasta escribir 'fin' o '0'. Retorna el subtotal."""
    print("REGISTRO DE VENTAS")
    subtotal = 0.0
    while True:
        entrada = input("Ingrese precio (o 'fin' para terminar): ")
        if entrada == "0" or entrada.lower() == "fin":
            return subtotal  # Retorno temprano para salir limpio del ciclo
        
        try:
            precio = float(entrada)
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
            else:
                subtotal += precio
        except ValueError:
            print("Error: Ingrese un número válido o 'fin' para terminar.")

def seleccionar_metodo_pago():
    """Valida y retorna '1' (Efectivo) o '2' (Tarjeta)."""
    imprimir_separador()
    print("--- Método de pago ---")
    metodo_pago = ""
    while metodo_pago not in ["1", "2"]:
        metodo_pago = input("1. Efectivo\n2. Tarjeta\nOpción: ")
        if metodo_pago not in ["1", "2"]:
            print("Opción inválida. Seleccione 1 o 2.")
        #Fin-if
    #Fin-while
    return metodo_pago = ""

def calcular_totales(subtotal, metodo_pago):
    """Calcula IVA, descuento y total final. Retorna el total_final."""
    # TODO 2: Calcula monto_iva (19%) y total_iva.
    monto_iva = subtotal * 0.19
    total_iva_cliente = subtotal + monto_iva

    # TODO 3: Si metodo_pago == "1", aplica 5% de descuento sobre total_iva.
    if metodo_pago == "1":
        descuento = total_iva_cliente*0.05
        print("Descuento por efectivo (5%): ", descuento)
    #fin-if  
    
    # TODO 4: Imprime el detalle de la boleta usando imprimir_separador()
    imprimir_separador()

