# Documento de Requisitos del Producto (PRD) - Reloj Analógico en Python

## 1. Información General

**Nombre del Producto:** Reloj Analógico Interactivo  
**Versión:** 1.0  
**Fecha:** 24 de abril de 2026  
**Autor:** Anderson Mauricio Ordoñez Zuñiga  
**Institución:** Universidad Cooperativa de Colombia 
**Programa:** Ingeniería de Software  

## 2. Resumen Ejecutivo

Esta aplicación es un reloj analógico interactivo desarrollado en Python utilizando la biblioteca Pygame. El sistema permite la visualización en tiempo real de la hora, con funcionalidades de manipulación manual de las manecillas, selección de zonas horarias de diferentes países y elección entre múltiples modelos de reloj con estilos visuales distintos.

## 3. Objetivos del Producto

- Proporcionar una representación visual precisa y atractiva de la hora en formato analógico
- Permitir la interacción manual con las manecillas del reloj
- Ofrecer soporte para múltiples zonas horarias internacionales
- Implementar diferentes modelos estéticos de reloj
- Mantener una arquitectura modular y extensible

## 4. Audiencia Objetivo

- Estudiantes de programación y estructuras de datos
- Desarrolladores interesados en aplicaciones gráficas con Python
- Usuarios que requieren visualización de hora en múltiples zonas horarias
- Profesionales que buscan ejemplos de arquitectura MVC en Python

## 5. Características Principales

### 5.1 Funcionalidades Core
- **Visualización Analógica:** Representación gráfica de horas, minutos y segundos
- **Sincronización Automática:** Actualización en tiempo real con la hora del sistema
- **Interacción Manual:** Arrastrar manecillas con el mouse para ajustar la hora
- **Modo Persistente:** El reloj continúa funcionando desde la hora ajustada manualmente
- **Reinicio Rápido:** Tecla 'R' para restaurar la hora actual del sistema

### 5.2 Selección de Zona Horaria
- Soporte para 11 países/ciudades principales:
  - Estados Unidos (Nueva York)
  - Estados Unidos (Los Ángeles)
  - Reino Unido (Londres)
  - España (Madrid)
  - Japón (Tokio)
  - China (Shanghái)
  - India (Calcuta)
  - Australia (Sídney)
  - Brasil (São Paulo)
  - México (Ciudad de México)
  - Colombia (Bogotá)

### 5.3 Modelos de Reloj
- **Clásico:** Modelo por defecto con números arábigos estándar
- **Romano:** Números romanos (I, II, III, etc.)
- **Vintage:** Estilo Bulova retro con números arábigos
- **Decorativo:** Diseño sin marco con números arábigos

## 6. Requisitos Funcionales

### 6.1 Requisitos de Usuario
- **RF-001:** El sistema debe mostrar la hora actual en formato analógico
- **RF-002:** El usuario debe poder arrastrar las manecillas con el mouse
- **RF-003:** El sistema debe mantener la hora ajustada manualmente hasta reinicio
- **RF-004:** Presionar 'R' debe restaurar la hora del sistema
- **RF-005:** El usuario debe poder seleccionar país para cambiar zona horaria
- **RF-006:** El usuario debe poder seleccionar entre diferentes modelos de reloj
- **RF-007:** Los cambios de modelo deben aplicarse inmediatamente

### 6.2 Requisitos de Sistema
- **RS-001:** El sistema debe inicializar correctamente en zona horaria de Colombia (Bogotá)
- **RS-002:** La aplicación debe manejar eventos de mouse y teclado
- **RS-003:** El renderizado debe actualizarse a 60 FPS mínimo
- **RS-004:** Los datos del reloj deben almacenarse en lista doblemente enlazada circular

## 7. Requisitos No Funcionales

### 7.1 Rendimiento
- **RNF-001:** Tiempo de respuesta a eventos de mouse < 100ms
- **RNF-002:** Actualización visual fluida sin lag perceptible
- **RNF-003:** Memoria RAM utilizada < 100MB

### 7.2 Usabilidad
- **RNF-004:** Interfaz intuitiva sin necesidad de tutorial
- **RNF-005:** Selectores claramente identificables en la interfaz
- **RNF-006:** Feedback visual inmediato en interacciones

### 7.3 Compatibilidad
- **RNF-007:** Compatible con Python 3.11.9
- **RNF-008:** Funcional en Windows, macOS y Linux
- **RNF-009:** Dependencias: Pygame 2.5.2, pytz

### 7.4 Arquitectura
- **RNF-010:** Patrón MVC implementado correctamente
- **RNF-011:** Separación clara entre backend y frontend
- **RNF-012:** Código modular y extensible

## 8. Historias de Usuario

### 8.1 Como estudiante de estructuras de datos
Quiero ver una implementación práctica de lista doblemente enlazada circular
Para entender mejor los conceptos teóricos aprendidos en clase

### 8.2 Como usuario internacional
Quiero poder ver la hora de diferentes países
Para coordinar actividades con personas en otras zonas horarias

### 8.3 Como usuario con preferencias estéticas
Quiero elegir entre diferentes diseños de reloj
Para personalizar la apariencia según mi gusto

### 8.4 Como usuario interactivo
Quiero poder ajustar manualmente las manecillas
Para simular escenarios de hora o practicar lectura de relojes

## 9. Especificaciones Técnicas

### 9.1 Arquitectura
- **Backend:** Lógica de negocio, servicios de tiempo y zona horaria
- **Frontend:** Interfaz gráfica, manejo de eventos, renderizado
- **Config:** Configuraciones centralizadas de modelos y UI
- **Domain:** Modelos de datos (lista enlazada, tiempo)

### 9.2 Tecnologías
- **Lenguaje:** Python 3.11.9
- **GUI:** Pygame 2.5.2
- **Zonas Horarias:** pytz
- **Estructura de Datos:** Lista doblemente enlazada circular

### 9.3 Componentes Principales
- `ClockApp`: Punto de entrada y loop principal
- `UIService`: Orquestador de lógica de interfaz
- `Renderer`: Motor de renderizado gráfico
- `ClockState`: Estado de la aplicación
- `TimezoneService`: Gestión de zonas horarias
- `AnalogClockList`: Estructura de datos del reloj

## 10. Diseño de Interfaz

### 10.1 Layout Principal
- Reloj central circular con radio configurable
- Selector de país: Posición (10, 10), dimensión (150, 35)
- Selector de modelo: Posición (650, 15), dimensión (100, 35)
- Área de dibujo: 800x600 píxeles

### 10.2 Paleta de Colores
- Fondo: Blanco cálido (#FFF0F0)
- Cara del reloj: Variable por modelo
- Manecillas: Negro estándar
- Bordes: Variable por modelo

## 11. Consideraciones de Implementación

### 11.1 Estructura de Datos
La implementación utiliza una lista doblemente enlazada circular para representar los números del reloj, permitiendo navegación cíclica eficiente.

### 11.2 Gestión de Estado
El estado de la aplicación se mantiene centralizado en `ClockState`, incluyendo modelo seleccionado, hora actual y ajustes manuales.

### 11.3 Renderizado
El sistema de renderizado es configurable por modelo, permitiendo diferentes estilos visuales mientras mantiene la funcionalidad core.

## 12. Criterios de Aceptación

- [ ] La aplicación inicia correctamente mostrando la hora de Bogotá
- [ ] Las manecillas se mueven fluidamente en tiempo real
- [ ] El arrastre de manecillas funciona correctamente
- [ ] La tecla 'R' restaura la hora del sistema
- [ ] Todos los países listados muestran la hora correcta
- [ ] Los 4 modelos de reloj se renderizan correctamente
- [ ] Los selectores responden a clics del mouse
- [ ] La aplicación maneja errores gracefully
- [ ] El código sigue estándares de calidad y documentación

## 13. Riesgos y Mitigaciones

- **Riesgo:** Dependencia de Pygame para renderizado
  **Mitigación:** Versión específica en requirements.txt

- **Riesgo:** Precisión de zonas horarias
  **Mitigación:** Uso de biblioteca pytz probada

- **Riesgo:** Performance en sistemas antiguos
  **Mitigación:** Requisitos mínimos claros en documentación

## 14. Métricas de Éxito

- Tiempo de carga inicial < 2 segundos
- Uso de CPU < 5% durante operación normal
- Satisfacción del usuario en pruebas de usabilidad
- Cobertura de código > 80% (futuras expansiones)
- Mantenibilidad del código según estándares del curso

---

*Documento creado como parte del proyecto final del curso de Estructuras de Datos - Universidad Cooperativa de Colombia*
