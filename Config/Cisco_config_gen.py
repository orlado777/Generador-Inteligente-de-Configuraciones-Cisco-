from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: Falta GROQ_API_KEY")
    exit()

client = Groq(api_key=api_key)

# 🧠 HISTORIAL GLOBAL (SESIÓN CONVERSACIONAL REAL)
mensajes = [
    {
        "role": "system",
        "content": """
Eres un ingeniero Cisco experto.
Debes responder SOLO con comandos Cisco IOS válidos.
No expliques nada.
Usa "!" para comentarios.
"""
    }
]


def guardar_config(texto, tipo):
    ruta = os.path.join(os.getcwd(), "configs")

    if not os.path.exists(ruta):
        os.makedirs(ruta)

    nombre = os.path.join(
        ruta,
        f"escenario_{tipo}_{int(time.time())}.txt"
    )

    with open(nombre, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"\n✔ Guardado en: {nombre}")


def generar(prompt, tipo):
    global mensajes

    mensajes.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensajes,
            temperature=0.2,
            max_tokens=800,
            stream=True
        )

        salida = ""

        print("\n--- CONFIGURACIÓN GENERADA ---\n")

        for chunk in response:
            if chunk.choices[0].delta.content:
                texto = chunk.choices[0].delta.content
                print(texto, end="")
                salida += texto

        mensajes.append({"role": "assistant", "content": salida})

        guardar_config(salida, tipo)

    except Exception as e:
        print("ERROR API:", e)


def main():
    print("\n=== GENERADOR CISCO IA (MODO CONVERSACIONAL) ===")

    while True:

        print("\n-----------------------------")
        print("1. VLAN")
        print("2. OSPF")
        print("3. SUBNETTING")
        print("4. ACL (EXTRA)")
        print("5. VER HISTORIAL")
        print("6. SALIR")
        print("-----------------------------")

        opcion = input("\nSelecciona opción: ")

        if opcion == "6":
            print("Saliendo del sistema...")
            break

        elif opcion == "5":
            print("\n========== HISTORIAL DE SESIÓN ==========\n")

            for m in mensajes:
                print(f"{m['role']}: {m['content']}\n")

            input("Presiona ENTER para volver al menú...")
            continue

        elif opcion == "1":
            vlan = input("VLAN (1-4094): ")
            if not vlan.isdigit() or not (1 <= int(vlan) <= 4094):
                print("VLAN inválida")
                continue
            generar(f"Configura VLAN {vlan} con trunking en switch Cisco", "vlan")

        elif opcion == "2":
            ospf = input("Proceso OSPF: ")
            if not ospf.isdigit():
                print("OSPF inválido")
                continue
            generar(f"Configura OSPF proceso {ospf} con redes básicas", "ospf")

        elif opcion == "3":
            red = input("Red (ej 192.168.1.0/24): ")
            generar(f"Haz subnetting de {red} y configura interfaces Cisco", "subnet")

        elif opcion == "4":
            red = input("Red ACL (ej 192.168.1.0): ")
            generar(f"Crea una ACL en Cisco que permita tráfico desde {red}", "acl")

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()