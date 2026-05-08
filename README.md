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
```
---

# Justificación de Parámetros del Modelo

Para cumplir con los requerimientos de la evaluación, se han configurado los siguientes parámetros en la API de Groq:

* [cite_start]**Temperature (0.2):** Se seleccionó un valor bajo para garantizar que las configuraciones de red sean determinísticas y precisas. [cite_start]En este contexto, un valor cercano a 0 evita que la IA genere comandos creativos o invente sintaxis, asegurando que el modelo se ciña estrictamente a los estándares de Cisco IOS  .
* [cite_start]**Max Tokens (800+):** Se definió este límite mínimo para permitir la generación de configuraciones completas sin cortes. [cite_start]Esto es esencial para escenarios que requieren múltiples líneas de comandos, como el anuncio de varias redes en OSPF o la creación de extensas listas de VLANs.
## Integrante

- Rogger Rojas: pruebas de API y soporte de configuración Cisco IOS