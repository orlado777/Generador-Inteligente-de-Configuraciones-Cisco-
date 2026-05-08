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

Actualmente el sistema funciona en consola con interacción tipo menú, permitiendo seleccionar diferentes escenarios de red y generar configuraciones automáticamente.

### Funcionalidades principales:

- Generación de configuraciones VLAN y trunking
- Configuración dinámica de OSPF
- Subnetting automático de redes IP
- Creación de ACL (Access Control List)
- Validación de entradas del usuario
- Guardado automático de configuraciones en archivos `.txt`
- Historial de sesión conversacional en memoria

---

# 🧠 Modo conversacional (Sesión 2)

En esta segunda etapa se implementa un **modo conversacional dentro de una sola ejecución del programa**, permitiendo múltiples interacciones sin reiniciar la aplicación.

### Características implementadas:

- Uso de `while True` para mantener sesión activa
- Historial de conversación almacenado en memoria (`mensajes[]`)
- Contexto acumulado entre interacciones con la API de Groq
- Opción de visualizar historial completo de la sesión
- Generación continua de configuraciones sin reinicio del programa

### Flujo de interacción:

1. El usuario selecciona una opción (VLAN, OSPF, etc.)
2. Ingresa los parámetros requeridos
3. La IA genera la configuración Cisco IOS
4. Se guarda automáticamente en archivos `.txt`
5. Se almacena en el historial de la sesión
6. El usuario puede continuar interactuando sin reiniciar el sistema

---

# Tecnologías utilizadas

- Python 3
- Groq API
- Visual Studio Code
- Git & GitHub

---

# Estructura del proyecto

```text
Generador-Inteligente-de-Configuraciones-Cisco/
│
├── src/
│   └── prompts.py
│
├── Config/
│   ├── Cisco_config_gen.py
│   ├── hola_groq.py
│
├── configs/
│   └── (archivos generados automáticamente)
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md