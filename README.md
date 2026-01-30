Sistema de Identificación Facial

# BioEntry-AI: Sistema de Identificación Facial para Control de Acceso

BioEntry-AI es una solución robusta desarrollada en Python para la gestión de empleados y validación de identidad mediante biometría facial. El sistema permite registrar empleados con una foto de carnet (referencia) y validar su ingreso comparando dicha imagen con una captura en vivo a través de un motor de Inteligencia Artificial pre-entrenado.

## Arquitectura y Decisiones Técnicas

La solución sigue una **arquitectura de capas** para garantizar la separación de responsabilidades:
* **`/api`**: Definición de los endpoints y lógica de rutas.
* **`/core`**: Lógica de negocio y procesamiento de biometría facial (IA).
* **`/db`**: Modelado de datos y configuración de la persistencia.
* **`/schemas`**: Contratos de datos para validación de entrada y salida.
* **`/static`**: Almacenamiento local de activos (fotos de carnet).

## Gestión de Ramas (GitFlow)
Este proyecto cumple con el requerimiento de gestión mediante ramas:
* `main`: Versión estable para entrega final.
* `dev`: Desarrollo activo de funcionalidades.
* `test`: Entorno de pruebas de integración de modelos de IA.

---
