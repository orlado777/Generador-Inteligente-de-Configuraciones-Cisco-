from groq import Groq
from dotenv import load_dotenv
import os
import time

# =========================
# CARGAR VARIABLES ENTORNO
# =========================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: Falta GROQ_API_KEY en el archivo .env")
    exit()

# =========================
# CLIENTE GROQ
# =========================

client = Groq(api_key=api_key)

# =========================
# HISTORIAL CONVERSACIONAL
# =========================

mensajes = [
    {
        "role": "system",
        "content": """
Eres un ingeniero Cisco experto.

Debes responder SOLO con comandos Cisco IOS válidos.

Reglas:
- No expliques nada.
- No uses markdown.
- No uses bloques ``` .
- Usa comentarios IOS con ! cuando sea necesario.
- Toda salida debe ser configuración Cisco IOS real.
- Configura interfaces, VLANs, OSPF, subnetting o ACL según lo solicitado.
"""
    }
]

# =========================
# GUARDAR CONFIGURACIONES
# =========================

def guardar_config(texto, tipo):

    ruta = os.path.join(os.getcwd(), "configs")

    if not os.path.exists(ruta):
        os.makedirs(ruta)

    nombre = os.path.join(
        ruta,
        f"escenario_{tipo}_{int(time.time())}.txt"
    )

    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print(f"\n\n✔ Configuración guardada en: {nombre}")


# =========================
# GENERAR RESPUESTA IA
# =========================

def generar(prompt, tipo):

    global mensajes

    mensajes.append({
        "role": "user",
        "content": prompt
    })

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensajes,
            temperature=0.2,
            max_tokens=900,
            stream=True
        )

        salida = ""

        print("\n========== CONFIGURACIÓN IOS ==========\n")

        for chunk in response:

            if chunk.choices[0].delta.content:

                texto = chunk.choices[0].delta.content

                print(texto, end="")

                salida += texto

        mensajes.append({
            "role": "assistant",
            "content": salida
        })

        guardar_config(salida, tipo)

    except Exception as e:

        error = str(e)

        if "429" in error:
            print("\nERROR: Rate limit excedido en Groq")

        elif "401" in error:
            print("\nERROR: API Key inválida")

        elif "connection" in error.lower():
            print("\nERROR: Problema de conexión")

        else:
            print("\nERROR GENERAL:", e)


# =========================
# VALIDAR VLAN
# =========================

def validar_vlan(vlan):

    if not vlan.isdigit():
        return False

    vlan = int(vlan)

    if vlan < 1 or vlan > 4094:
        return False

    return True


# =========================
# VALIDAR OSPF
# =========================

def validar_ospf(ospf):

    return ospf.isdigit()


# =========================
# VALIDAR PREFIJO
# =========================

def validar_prefijo(prefijo):

    if not prefijo.isdigit():
        return False

    prefijo = int(prefijo)

    if prefijo < 8 or prefijo > 30:
        return False

    return True


# =========================
# MENÚ PRINCIPAL
# =========================

def main():

    print("\n===================================")
    print(" GENERADOR INTELIGENTE CISCO IOS ")
    print(" Python + Groq AI ")
    print("===================================")

    while True:

        print("\n------------- MENÚ -------------")
        print("1. Escenario VLAN")
        print("2. Escenario OSPF")
        print("3. Escenario Subnetting")
        print("4. Escenario ACL")
        print("5. Ver historial IA")
        print("6. Salir")
        print("--------------------------------")

        opcion = input("Seleccione opción: ")

        # =========================
        # SALIR
        # =========================

        if opcion == "6":

            print("\nSaliendo del sistema...")
            break

        # =========================
        # HISTORIAL
        # =========================

        elif opcion == "5":

            print("\n========== HISTORIAL ==========\n")

            for m in mensajes:

                print(f"{m['role'].upper()}:\n")

                print(m["content"])

                print("\n---------------------------\n")

            input("Presione ENTER para continuar...")

        # =========================
        # VLAN
        # =========================

        elif opcion == "1":

            vlan = input("Ingrese VLAN (1-4094): ")

            if not validar_vlan(vlan):
                print("ERROR: VLAN inválida")
                continue

            nombre = input("Nombre VLAN: ")

            puertos = input("Puertos (ej Fa0/1-5): ")

            prompt = f"""
Configura una VLAN Cisco IOS.

Datos:
- VLAN: {vlan}
- Nombre: {nombre}
- Puertos: {puertos}

Configura:
- VLAN
- Nombre VLAN
- Asignación de puertos
- Trunking
"""

            generar(prompt, "vlan")

        # =========================
        # OSPF
        # =========================

        elif opcion == "2":

            proceso = input("ID proceso OSPF: ")

            if not validar_ospf(proceso):
                print("ERROR: Proceso OSPF inválido")
                continue

            red = input("Red a anunciar: ")

            wildcard = input("Wildcard mask: ")

            area = input("Área OSPF: ")

            prompt = f"""
Configura OSPF Cisco IOS.

Datos:
- Proceso: {proceso}
- Red: {red}
- Wildcard: {wildcard}
- Área: {area}

Genera configuración completa IOS.
"""

            generar(prompt, "ospf")

        # =========================
        # SUBNETTING
        # =========================

        elif opcion == "3":

            red = input("Red base (ej 192.168.1.0): ")

            prefijo = input("Prefijo (8-30): ")

            if not validar_prefijo(prefijo):
                print("ERROR: Prefijo inválido")
                continue

            cantidad = input("Cantidad de subredes: ")

            if not cantidad.isdigit():
                print("ERROR: Cantidad inválida")
                continue

            prompt = f"""
Realiza subnetting Cisco IOS.

Datos:
- Red base: {red}/{prefijo}
- Cantidad subredes: {cantidad}

Debes:
- Crear subredes
- Mostrar gateways
- Configurar interfaces Cisco IOS
- Usar direccionamiento válido
"""

            generar(prompt, "subnetting")

        # =========================
        # ACL
        # =========================

        elif opcion == "4":

            red = input("Red origen: ")

            wildcard = input("Wildcard: ")

            prompt = f"""
Genera una ACL Cisco IOS.

Datos:
- Red origen: {red}
- Wildcard: {wildcard}

Permitir tráfico desde esa red.
Aplicar ACL en interfaz.
"""

            generar(prompt, "acl")

        else:

            print("ERROR: Opción inválida")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

if __name__ == "__main__":
    main()