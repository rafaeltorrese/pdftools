<div class="header">
<p><strong>Materia:</strong> INVESTIGACIÓN DE OPERACIONES MODELOS MATEMÁTICOS</p>
<p><strong>Clave:</strong> IIND-4402</p>
<p><strong>Profesor:</strong> Dr. Rafael Torres-Escobar</p>
<p><strong>Fecha:</strong> Junio 2025</p>
</div>

# Información de Estudiantes

| **Nombre Completo** | **ID** |
|---------------------|--------|
| Nombre Completo 1   | 000012 |
| Nombre Completo 2   | 000013 |
| Nombre Completo 3   | 000014 |

# Planteamiento del Problema

Maximizar Z = 3x₁ + 5x₂  
Sujeto a:  
2x₁ + 3x₂ ≤ 8  
x₁ + x₂ ≤ 4  
x₁, x₂ ≥ 0

# Modelo Matemático en Contexto Logístico

Contexto: Una empresa de distribución desea maximizar sus ingresos por la asignación de productos a dos rutas logísticas diferentes. Cada ruta tiene una capacidad limitada y el beneficio por unidad enviada difiere.

# Resolución con el Algoritmo Simplex

Paso 1: Convertimos las restricciones en ecuaciones con variables de holgura:

- 2x₁ + 3x₂ + s₁ = 8  
- x₁ + x₂ + s₂ = 4  
- Z - 3x₁ - 5x₂ = 0

Paso 2: Tabla inicial, selección de variable de entrada ($x_2$) y salida ($s_1$), pivoteo correcto.  
Paso 3: Segunda tabla, nueva variable de entrada (x₁), pivoteo final.

**Solución óptima:** x₁ = 0, x₂ = 8/3, Z = 40/3

# Retroalimentación

Excelente trabajo. Has identificado correctamente el contexto del problema y formulado el modelo de programación lineal con precisión. Los pasos del algoritmo Simplex han sido aplicados correctamente, mostrando un sólido entendimiento del método.

# Rúbrica de Evaluación

| <span class="atributo"><strong>Atributo</strong></span> | <span class="excelente"><strong>Excelente (10)</strong></span>                               | <strong>Bueno (8)</strong>                         | <strong>Regular (6)</strong>            | <strong>Deficiente (5)</strong>      |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------|-----------------------------------------|--------------------------------------|
| Planteamiento del problema y función objetivo           | <span class="excelente">Identifica correctamente variables, restricciones y objetivo.</span> | Pequeños errores en función o restricciones.       | Errores evidentes en el planteamiento.  | Planteamiento incorrecto.            |
| Transformación a forma estándar                         | <span class="excelente">Incluye correctamente variables de holgura y forma estándar.</span>  | 1 error menor en transformación.                   | Errores múltiples pero comprensibles.   | Transformación incorrecta.           |
| Tablas simplex y pivoteo                                | <span class="excelente">Todas las tablas correctamente calculadas.</span>                    | Errores menores en tablas o selección de variable. | Errores frecuentes en cálculos.         | Procedimiento de pivoteo erróneo.    |
| Interpretación de la solución                           | <span class="excelente">Interpreta correctamente variables y valor óptimo.</span>            | Pequeños errores de interpretación.                | Interpreta parcialmente los resultados. | Conclusiones incorrectas o ausentes. |
