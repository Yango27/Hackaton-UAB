# 📡 WiFi Traffic Analytics – Hackathon UAB

Proyecto desarrollado durante la **Hackathon UAB** para analizar, visualizar y entender el **tráfico de red Wi-Fi** en distintos edificios del campus.  
El objetivo fue extraer patrones de uso, afluencia de personas y comportamiento temporal a partir de los puntos de acceso (APs) de la red.

---

## 🚀 Objetivos del proyecto

- Analizar los datos de conexión Wi-Fi (APs) del campus.
- Identificar los edificios con mayor tráfico y su evolución en el tiempo.
- Comparar el uso entre facultades y bibliotecas.
- Generar visualizaciones interactivas y estadísticas acumuladas por día, semana y mes.

---

## 📊 Descripción técnica

Los datos provienen de los **Access Points (APs)** distribuidos en distintas zonas del campus.  
Cada registro contiene:

| Campo | Descripción |
|--------|--------------|
| `timestamp` | Marca temporal de la conexión (en formato Unix) |
| `name` | Nombre del punto de acceso (AP) |
| `client_count` | Número de clientes conectados |
| `edifici` | Edificio o zona del campus (extraído del nombre del AP) |

El procesamiento se realiza con **Python** y **pandas**, y las visualizaciones con **matplotlib**.

---

## 🧠 Arquitectura del análisis

1. **Carga de datos**
   - Se usa `load_aps()` para importar los datos de conexión.
   - Se convierten los `timestamp` desde formato Unix a fechas legibles (`pd.to_datetime(..., unit='s')`).

2. **Preprocesamiento**
   - Se agrupan los datos por día (`init_APS()`), semana (`agruparSetmana()`) y mes (`agruparMes()`).
   - Se calcula el porcentaje de clientes por AP respecto al total diario (`initTable()`).

3. **Filtrado**
   - Se separan los datos por tipo de edificio:
     - Facultades (`facus`)
     - Bibliotecas (`biblios`)

4. **Visualización**
   - `plotNormal()` muestra la evolución diaria de conexiones totales.
   - `plotAccum()` genera gráficos apilados por edificio o categoría.
   - Los resultados permiten observar patrones de afluencia según el día o el tipo de edificio.

---

## 🧩 Estructura del repositorio


