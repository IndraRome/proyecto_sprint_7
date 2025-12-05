# 🚗 Dashboard de Análisis Exploratorio de Datos – Vehículos en EE.UU.

Este proyecto consiste en un **dashboard interactivo** creado con **Python, Plotly y Dash**, que permite visualizar el análisis exploratorio de datos (EDA) del dataset `vehicles_us.csv`, el cual contiene información de automóviles publicados para venta en Estados Unidos.

El objetivo principal es explorar variables como el precio, kilometraje, condición del vehículo, año del modelo, tipo de combustible y más, mediante gráficos intuitivos y dinámicos.

---

## 📊 **Funciones del Dashboard**

El dashboard incluye un menú lateral con botones para generar diferentes visualizaciones interactivas:

### ✔ Histogramas
- **Distribución del odómetro (kilometraje)**
- **Distribución de los precios**

### ✔ Gráficos de dispersión (scatter)
- **Precio vs Odómetro**
- **Año del modelo vs Precio**

### ✔ Boxplot
- **Distribución de precios según la condición del vehículo**

Todas las gráficas se actualizan dinámicamente y permiten interacción como zoom, selección y descarga.

---

## 🛠 **Tecnologías Utilizadas**

- **Python 3.x**
- **Pandas** → manipulación del dataset  
- **Plotly Express** → visualizaciones interactivas  
- **Dash** → creación del dashboard web  
- **Dash Bootstrap Components** → estilo profesional  
- **Gunicorn** → despliegue en Render  

---

## 📁 **Estructura del Proyecto**
├── app.py # Aplicación principal del dashboard
├── vehicles_us.csv # Dataset utilizado
├── requirements.txt # Dependencias para Render o instalación local
└── README.md # Documentación del proyecto


Proyecto sobre herramientas de desarrollo de software.
