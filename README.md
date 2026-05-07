# Generador Inteligente de Configuraciones Cisco IOS

Proyecto desarrollado para la evaluación práctica de la unidad **IA Aplicada a Redes** de la asignatura **Networking I** en INACAP La Serena.

La aplicación utiliza Python y la API de Groq para generar configuraciones Cisco IOS automáticamente a partir de escenarios de red ingresados por el usuario.

---

# Integrantes

- Alexis Ponce
- Rogger Rojas
- Orlando Araya

---

# Descripción del proyecto

El sistema permite generar configuraciones Cisco IOS utilizando inteligencia artificial mediante la API de Groq.

La aplicación será capaz de:

- Generar configuraciones VLAN y trunking
- Generar configuraciones OSPF
- Realizar subnetting y asignación IP
- Validar entradas antes de consumir la API
- Guardar configuraciones automáticamente en archivos `.txt`

---

# Tecnologías utilizadas

- Python 3
- Groq API
- Visual Studio Code
- GitHub

---

# Estructura inicial del proyecto

```text
Generador-Inteligente-de-Configuraciones-Cisco/
│
├── src/
│   └── prompts.py
│
├── configs/
│
├── cisco_config_gen.py
├── hola_groq.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md