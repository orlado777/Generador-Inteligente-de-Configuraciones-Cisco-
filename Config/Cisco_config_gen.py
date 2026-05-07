from src.prompts import SYSTEM_PROMPT

def generar_configuracion(escenario):

    print("\n=== SYSTEM PROMPT ACTUAL ===\n")
    print(SYSTEM_PROMPT)

    print("\n=== ESCENARIO RECIBIDO ===\n")
    print(escenario)

    print("\nGenerando configuracion Cisco IOS...\n")


def main():

    print("===================================")
    print(" GENERADOR INTELIGENTE CISCO IOS ")
    print("===================================\n")

    escenario = input("Describe el escenario de red: ")

    generar_configuracion(escenario)


if __name__ == "__main__":
    main()