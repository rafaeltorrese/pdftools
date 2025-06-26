<div class="header">
<p><strong>Materia:</strong> INVESTIGACIÓN DE OPERACIONES: MODELOS MATEMÁTICOS</p>
<p><strong>Clave:</strong> IIND-3305</p>
<p><strong>Profesor:</strong> Dr. Rafael Torres-Escobar</p>
<p><strong>Fecha:</strong>19 de septiembre 2024</p>
</div>

# Información de Estudiantes

| **Nombre Completo** | **ID** |**Calificación**
|---------------------|--------|--------|
| Sousa*Alday, Clarissa   | 00363547 |8|
| Aranda*Claussen, Daniela   | 00369256 |8|


# Ejercicio del Algoritmo Simplex 

## Planteamiento del problema

Una empresa produce dos productos, **A** y **B**, utilizando dos recursos limitados: horas de trabajo y materia prima. Cada unidad de A genera una ganancia de **$3** y cada unidad de B una ganancia de **$5**.

Se dispone de:
- 4 horas de trabajo.
- 12 unidades de materia prima.

Cada unidad de A requiere 1 hora de trabajo y 2 unidades de materia prima.  
Cada unidad de B requiere 2 horas de trabajo y 1 unidad de materia prima.

**Maximizar la función objetivo**:


$$Z = -3x_1 + 5x_2$$


**Sujeto a**:

\[
\begin{aligned}
x_1 + 2x_2 &\leq 4 \quad \text{(Horas de trabajo)} \\
2x_1 + x_2 &\leq 12 \quad \text{(Materia prima)} \\
x_1, x_2 &\geq 0
\end{aligned}
\]

> **Error 1**: El coeficiente de $x_1$ en la función objetivo es negativo, lo cual contradice el planteamiento ("ganancia de $3").

---

## Transformación a forma estándar

Agregamos variables de holgura:

$$
\begin{aligned}
x_1 + 2x_2 + s_1 &= 4 \\\\
2x_1 + x_2 &= 12 \\\\
x_1, x_2, s_1, s_2 &\geq 0
\end{aligned}
$$

> **Error 2**: Falta agregar la variable de holgura $s_2$ en la segunda restricción.

---

## Tabla inicial del método Simplex

| Variable básica | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|------------------|-------|-------|--------|--------|------|
| $s_1$           | 1     | 2     | 1      | 0      | 4    |
| $s_2$           | 2     | 1     | 0      | 1      | 12   |
| Z               | -3    | -5    | 0      | 0      | 0    |

> **Error 3**: La fila Z está incorrecta. Dado que la función correcta sería $Z = 3x_1 + 5x_2$, la fila Z debería tener los signos opuestos.

---

## Interpretación de la solución (Provisional)

La tabla sugiere que la solución óptima se alcanzará cuando $x_1 = 0$ y $x_2 = 2$, lo que produce una ganancia de:

$$
Z = -3(0) + 5(2) = 10
$$

> Esta interpretación no es válida dado que la función objetivo tiene un signo erróneo en el coeficiente de $x_1$.

---

## Evaluación según rúbrica

| **Atributo**                                     | **Evaluación**   | **Justificación**                                                                 |
|--------------------------------------------------|------------------|-----------------------------------------------------------------------------------|
| Planteamiento del problema y función objetivo    | Regular (6)      | Error evidente en el signo del coeficiente de la función objetivo.               |
| Transformación a forma estándar                  | Regular (6)      | Faltó incluir la variable de holgura $s_2$ en la segunda restricción.            |
| Tablas simplex y pivoteo                         | Regular (6)      | Cálculo incorrecto de la fila Z; afecta el procedimiento de pivoteo.             |
| Interpretación de la solución                    | Bueno (8)        | Buena intención en la lectura de la tabla, pero basada en un planteamiento erróneo. |



# Rúbrica de Evaluación

| <span class="atributo"><strong>Atributo</strong></span> | <span class="excelente"><strong>Excelente (10)</strong></span>                               | <strong>Bueno (8)</strong>                         | <strong>Regular (6)</strong>            | <strong>Deficiente (5)</strong>      |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------|-----------------------------------------|--------------------------------------|
| Planteamiento del problema y función objetivo           | <span class="excelente">Identifica correctamente variables, restricciones y objetivo.</span> | Pequeños errores en función o restricciones.       | Errores evidentes en el planteamiento.  | Planteamiento incorrecto.            |
| Transformación a forma estándar                         | <span class="excelente">Incluye correctamente variables de holgura y forma estándar.</span>  | 1 error menor en transformación.                   | Errores múltiples pero comprensibles.   | Transformación incorrecta.           |
| Tablas simplex y pivoteo                                | <span class="excelente">Todas las tablas correctamente calculadas.</span>                    | Errores menores en tablas o selección de variable. | Errores frecuentes en cálculos.         | Procedimiento de pivoteo erróneo.    |
| Interpretación de la solución                           | <span class="excelente">Interpreta correctamente variables y valor óptimo.</span>            | Pequeños errores de interpretación.                | Interpreta parcialmente los resultados. | Conclusiones incorrectas o ausentes. |
