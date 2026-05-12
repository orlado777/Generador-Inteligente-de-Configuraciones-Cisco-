# Generador Inteligente de Configuraciones Cisco IOS

Proyecto desarrollado para la evaluación práctica de la unidad **IA Aplicada a Redes** de la asignatura **Networking I** en INACAP La Serena.

La aplicación utiliza Python y la API de Groq para generar configuraciones Cisco IOS automáticamente a partir de distintos escenarios de red ingresados por el usuario.

---

# Integrantes

- Alexis Ponce
- Rogger Rojas
- Orlando Araya

---

# Descripción del proyecto

El sistema permite generar configuraciones Cisco IOS utilizando inteligencia artificial mediante la API de Groq.

La aplicación funciona mediante consola interactiva con sistema de menú, permitiendo seleccionar distintos escenarios de red y generar configuraciones automáticamente en tiempo real utilizando streaming.

---

# Funcionalidades implementadas

- Generación de configuraciones VLAN y trunking
- Configuración dinámica de OSPF
- Subnetting automático de redes IPv4
- Creación de ACL (Access Control List)
- Validación de entradas del usuario
- Manejo de errores de conexión y API
- Streaming en tiempo real con Groq
- Guardado automático de configuraciones en archivos `.txt`
- Historial conversacional en memoria
- Persistencia de configuraciones en carpeta `/configs`

---

# Escenarios soportados

## Escenario A — VLAN y Trunking

Permite generar configuraciones Cisco IOS para:
- creación de VLANs
- asignación de nombres
- asignación de puertos
- configuración trunk

### Datos solicitados:
- ID VLAN
- Nombre VLAN
- Puertos

---

## Escenario B — OSPF

Permite configurar protocolos de enrutamiento dinámico OSPF.

### Datos solicitados:
- ID de proceso
- Red
- Wildcard mask
- Área

---

## Escenario C — Subnetting

Permite realizar subnetting automático y generar configuraciones de interfaces Cisco IOS.

### Datos solicitados:
- Red base
- Prefijo
- Cantidad de subredes

---

## Escenario D — ACL (Extra)

Permite generar listas de control de acceso Cisco IOS.

### Datos solicitados:
- Red origen
- Wildcard mask

---

# Modo conversacional

El sistema implementa un modo conversacional durante la ejecución del programa.

Esto permite:
- mantener contexto entre consultas
- reutilizar configuraciones anteriores
- continuar generando configuraciones sin reiniciar la aplicación

La conversación se almacena utilizando una lista de mensajes en memoria.

---

# Tecnologías utilizadas

- Python 3
- Groq API
- python-dotenv
- Visual Studio Code
- Git
- GitHub

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/alexpo13362/eval-cisco-groq-ponce.git
```

---

## 2. Ingresar al proyecto

```bash
cd eval-cisco-groq-ponce
```

---

## 3. Crear entorno virtual

```bash
python -m venv venv
```

---

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de API Key

Crear archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_api_key
```

---

# Ejecución del proyecto

Ejecutar:

```bash
python Cisco_config_gen.py
```

---

# Ejemplos de uso

## Ejemplo VLAN

### Entrada

```text
VLAN: 10
Nombre: VENTAS
Puertos: Fa0/1-5
```

### Salida generada

```text
vlan 10
 name VENTAS

interface range fa0/1-5
 switchport mode access
 switchport access vlan 10
```

---

## Ejemplo OSPF

### Entrada

```text
Proceso: 1
Red: 192.168.1.0
Wildcard: 0.0.0.255
Area: 0
```

### Salida generada

```text
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
```

---

## Ejemplo Subnetting

### Entrada

```text
Red base: 192.168.1.0
Prefijo: /24
Cantidad subredes: 4
```

### Salida generada

```text
interface g0/0
 ip address 192.168.1.1 255.255.255.192
 no shutdown
```

---

# Streaming en tiempo real

El proyecto utiliza:

```python
stream=True
```

Esto permite:
- recibir respuestas en tiempo real
- imprimir configuraciones por fragmentos
- mejorar experiencia de usuario

---

# Validaciones implementadas

El sistema valida:

- VLANs entre 1 y 4094
- Prefijos entre /8 y /30
- IDs OSPF numéricos
- Cantidades válidas de subredes

Las entradas inválidas son rechazadas antes de consumir la API.

---

# Manejo de errores

El sistema implementa manejo de errores para:

- API Key faltante
- API Key inválida
- errores de conexión
- rate limit (HTTP 429)

---

# Justificación de parámetros IA

## Modelo utilizado

Se utilizó:

```text
llama-3.3-70b-versatile
```

Debido a:
- rapidez de respuesta
- buena generación técnica
- compatibilidad con streaming

---

## Temperature = 0.2

Se utiliza una temperatura baja para:
- reducir respuestas aleatorias
- obtener configuraciones consistentes
- generar comandos Cisco IOS más determinísticos

---

## max_tokens = 900

Se utiliza un límite alto de tokens para:
- permitir configuraciones extensas
- soportar múltiples interfaces
- generar escenarios complejos

---

# Estructura del proyecto

```text
eval-cisco-groq-ponce/
│
├── configs/
│   └── (archivos generados automáticamente)
│
├── Cisco_config_gen.py
├── hola_groq.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

# Archivos importantes

## `.gitignore`

Excluye:
- venv/
- __pycache__/
- .env

---

## `.env.example`

Muestra el formato requerido para la API Key sin exponer información sensible.

---

# Limitaciones conocidas

- La IA puede generar configuraciones diferentes para el mismo escenario.
- No se valida sintaxis avanzada IOS.
- No existe conexión directa a dispositivos Cisco reales.
- El sistema depende de conexión a Internet.
- La calidad de salida depende del prompt ingresado.

---

# Release final

Versión entregada:

```text
v1.0
```

---

# Repositorio GitHub

Repositorio oficial:

https://github.com/alexpo13362/eval-cisco-groq-ponce