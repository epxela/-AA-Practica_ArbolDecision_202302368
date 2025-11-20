# Práctica de Árbol de Decisión Simple

**Universidad Da Vinci de Guatemala**  
**Curso:** Análisis de Algoritmos  
**Práctica:** Implementación de Árbol de Decisión Binario  
**Estudiante:** Francisco Javier Rojas Santos
**Carnet:** 202302368  
**Fecha:** Noviembre 2025

## Objetivo General

Implementar un árbol de decisión simple para clasificar números en categorías "Alto" y "Bajo" según un umbral establecido, aplicando metodología Gitflow para el control de versiones.

## Objetivos Específicos

- Crear un sistema de clasificación binaria basado en umbral
- Generar y procesar archivos de datos con números aleatorios
- Medir tiempos de ejecución para análisis de rendimiento
- Aplicar flujo de trabajo Gitflow con ramas feature y hotfix
- Documentar el proceso completo con evidencias

## Descripción del Árbol

El proyecto implementa un árbol de decisión binario simple que funciona de la siguiente manera:

**Estructura del Árbol:**
```
        Número >= Umbral?
           /         \
         Sí           No
        /              \
    "Alto"           "Bajo"
```

**Componentes principales:**
- **decision_tree.py**: Contiene las funciones de clasificación
- **dataloader.py**: Maneja la carga y generación de datos
- **main.py**: Programa principal con menú interactivo

**Funcionamiento:**
1. El usuario puede configurar un umbral (por defecto 50)
2. Se generan números aleatorios entre 1 y 100
3. Cada número se compara con el umbral
4. Si número >= umbral → "Alto", sino → "Bajo"

## Metodología

### Pasos del Script

1. **Menú Principal**: Sistema interactivo con 4 opciones
   - Regenerar números aleatorios
   - Cambiar umbral de clasificación
   - Cambiar cantidad de números a procesar
   - Ejecutar programa principal

2. **Generación de Datos**: 
   - Crear archivo `data/numeros_1000.txt`
   - Usar semilla aleatoria para reproducibilidad
   - Generar números entre 1-100

3. **Clasificación**:
   - Cargar números desde archivo
   - Aplicar función de decisión simple
   - Contar resultados por categoría

4. **Resultados**:
   - Mostrar 10 ejemplos de clasificación
   - Conteo total de "Alto" y "Bajo"
   - Tiempo de ejecución medido

### Flujo Gitflow Usado

**Inicialización:**
```bash
git flow init
```

**Ramas Implementadas:**

1. **Feature Branch**: `feature/implementacion_arbol`
   - `[feature] Estructura base del proyecto`
   - `[feature] Generación de numeros_1000.txt`
   - `[feature] Implementación árbol (umbral) y clasificación`
   - `[feature] Impresión de resultados y tiempos`

2. **Hotfix Branch**: `hotfix/correccion_nombre`
   - Cambio de nombre del estudiante en README.md

**Versioning:**
- Tag final: `v1.0.0` después del merge
- Pull request implementado para revisión de código

## Resultados

### Conteos "Alto"/"Bajo" 

**Prueba con 1,000,000 números (umbral=50):**
- Altos: 509,607
- Bajos: 490,393
- Distribución: ~51% Alto, ~49% Bajo

**Prueba con 10,000,000 números (umbral=50):**
- Altos: 5,097,598
- Bajos: 4,902,402
- Distribución: ~51% Alto, ~49% Bajo

**Prueba con 1,000 números (umbral=20):**
- Altos: 818
- Bajos: 182
- Distribución: ~82% Alto, ~18% Bajo

### Tiempo Total de Ejecución

- 1,000,000 números: 0.3291 segundos
- 10,000,000 números: 5.0569 segundos
- Escalabilidad: aproximadamente linear

### 10 Ejemplos de Clasificación

**Con umbral = 50:**
```
80 → Alto
92 → Alto
97 → Alto
97 → Alto
55 → Alto
92 → Alto
78 → Alto
15 → Bajo
76 → Alto
23 → Bajo
```

**Con umbral = 20:**
```
78 → Alto
84 → Alto
89 → Alto
16 → Bajo
64 → Alto
22 → Alto
47 → Alto
58 → Alto
67 → Alto
66 → Alto
```

## Evidencias

### Capturas de Pantalla
- Menú principal funcionando
![Menú funcionando](/evidencia/1.jpg)
- Ejecución con diferentes configuraciones
![Prueba con 1000 numeros](/evidencia/2.jpg)
- Resultados con distintos tamaños de datos
![Prueba con 10000000 numeros](/evidencia/4.jpg)
- Error controlado al intentar procesar 1,000,000,000 números
![Error](/evidencia/3.jpg)

### Archivos de Evidencia
Ubicación: `docs/evidencias/`

### Pruebas Realizadas
- Funcionamiento con 1,000 números
- Funcionamiento con 1,000,000 números  
- Funcionamiento con 10,000,000 números
- Cambio de umbral dinámico
- Regeneración de archivos
- Limitación encontrada con 1,000,000,000 números (KeyboardInterrupt)

## Conclusiones

### Aprendizajes sobre el Árbol Simple

1. **Simplicidad y Eficiencia**: Un árbol de decisión de un solo nivel es muy rápido para clasificaciones binarias simples
2. **Escalabilidad**: El algoritmo escala linealmente con el tamaño de datos, procesando 10 millones de números en ~5 segundos
3. **Distribución Estadística**: Con umbral de 50 en números 1-100, la distribución es casi 50/50, como se esperaba matemáticamente
4. **Limitaciones**: El sistema tiene límites prácticos de memoria para datasets extremadamente grandes (>100 millones)

### Aprendizajes sobre Gitflow

1. **Organización del Código**: Gitflow ayuda a mantener un historial limpio con commits específicos por funcionalidad
2. **Separación de Responsabilidades**: Las ramas feature permiten desarrollar funcionalidades sin afectar la rama principal
3. **Hotfixes**: Las ramas hotfix son útiles para correcciones rápidas sin interrumpir el desarrollo
4. **Versionado**: Los tags proporcionan puntos de referencia claros para releases estables
5. **Pull Requests**: Facilitan la revisión de código antes de integrar cambios importantes
