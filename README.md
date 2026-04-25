# 🕒 Reloj Analógico en Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Pygame-Required-green">
  <img src="https://img.shields.io/badge/Estado-Activo-success">
</p>

---

## 📌 Descripción

Aplicación interactiva desarrollada en **Python** que representa un reloj en formato **analógico**.

El sistema se sincroniza automáticamente con la hora del sistema.

Se puede elegir diferentes fondos para el reloj usando las flechas del teclado (`←` y `→`).

Se puede elijir un pais para mira la hora actual de la ciudad principal de ese pais, las opciones son:
- USA (NY)
- USA (LA)
- UK (London)
- España (Madrid)
- Japón (Tokyo)
- China (Shanghai)
- India (Kolkata)
- Australia (Sydney)
- Brasil (Sao Paulo)
- México (Mexico City)

Se pueden elegir entre 4 modelos de reloj con estilos visuales distintos:
- Clásico: Modelo por defecto con números arábigos estándar
- Romano: Números romanos (I, II, III, etc.)
- Vintage: Estilo Bulova retro con números arábigos
- Decorativo: Diseño sin marco con números arábigos
---

## ✨ Características

- 🕐 Visualización analógica en tiempo real
- 🔄 Sincronización automática con la hora del sistema
-  ⌨️ cambio de fondo interactivo con flechas del teclado
- 🌍 Selección de zona horaria por país 
- 🎨 Cuatro estilos de reloj personalizables
- 📱 Interfaz gráfica intuitiva y atractiva
---

## 🧠 Estructura de Datos

### 🔗 Lista Doblemente Enlazada Circular

El sistema implementa una **lista doblemente enlazada circular**, utilizada para modelar el comportamiento cíclico de los números del reloj.

---
## ⚙️ Requisitos

### 🐍 Python

Se requiere **Python 3.11.9**

---
##  📦 Instalacion de Python
🔗 Descarga oficial:  
https://www.python.org/downloads/release/python-3119/

---

### 💻 Instalación por sistema operativo
#### 🪟 Windows
Desde la powershell o cmd, ejecuta el siguiente comando / si no funciona ábrelo con permisos de administrador:

```bash
winget install Python.Python.3.11
```
#### Realiza este pasi si python no se agrega automáticamente a las variables de entorno después de la instalación:

```bash
Escribe en la barra de búsqueda "variables de entorno" y
selecciona la opción "Editar las variables de entorno del sistema".
En la ventana que se abre, haz clic en el botón "Variables de entorno". 
En la sección "Variables del Usuario o Sistema", busca la variable llamada "Path" y haz clic en "Editar". 
```

Deberia aparecer dos rutas como esta:

```bash
\AppData\Local\Programs\Python\Python311\Scripts\
```
```bash
\Users\Mao\AppData\Local\Programs\Python\Python311\Scripts\
```
Si no aparecen, haz clic en "Nuevo" y agrega ambas rutas, busca la ruta de instalación de Python 3.11 en tu sistema y
agrega las rutas correspondientes a "Path" en las variables de entorno.

---

Desde Homebrew usando el siguiente comando:
🍎 MacOS
```bash
brew install python@3.11
```
---

🐧 Linux (Ubuntu/Debian)
Desde la terminal, ejecuta el siguiente comando:
```bash
sudo apt-get install python3.11
```
---

## 🧩Librería que se utiliza: 
- pygame 
- pytz
---

## 🛠️ Instalación 
- Clonar el reposorio 
---
## 🧑‍💻 Como Correr el Proyecto:

Una vez clonado abre la carpeta clock_project en un IDE de tu preferencia como: 
- Visual Studio Code 
- IntelliJ IDEA 
- PyCharm 
- etc

 ```
Tener en cuenta que la version de python previamente instalada debe estar agregado a las variables de entorno para poder ejecutar los siguientes comandos sin problemas.
```

---

## 🚶‍➡️Pasos Importantes: 
1. Abre la terminal integrada del IDE 
2. Instala el entorno virtual con el siguiente comando:

```bash
python -3.11 -m venv .venv
```
3. Activa el entorno virtual con el siguiente comando:


#### 🪟 Windows
```bash
.\.venv\Scripts\activate
```

#### En 🍎MacOS/ 🐧Linux

```bash
source .venv/bin/activate
```

4. Después de activar, instala las dependencias necesarias con el siguiente comando:
```bash
   pip install -r requirements.txt
 ```

5. El más importante, ejecuta el archivo main.py que se encuentra en La raiz de la carpeta del proyecto con el siguiente comando:

```bash
   python main.py
``` 
---

## 🖼️ Imagen del proyecto en ejecución:

![Reloj Analógico](assets/img.png)

---

## 👨‍🎓 Autor: 
- **Anderson Mauricio Ordoñez Zuñiga** 
---

## 🏫 Universidad:
- **Universidad Cooperativa de Colombia**
- **Campus Pasto** 
- **Facultad de Ingeniería** 
- **Programa de Ingeniería de Software** 
- **Semestre 2026-4** 
- **Curso: Estructuras de Datos** 
- **Profesor: Jhonatan Mideros** 
- **Fecha de entrega: 24/04/2026**

