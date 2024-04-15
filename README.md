# Parcial_2_IA

### Informe de Avances: Método de Elementos Finitos en Ingeniería Digital

**Parte I: Fundamentos de Elementos Finitos**

#### Introducción a Python
En esta sección, desarrollamos un script en Python para generar y mostrar un arreglo tridimensional que representa un dominio estructural simple. Utilizamos `numpy` para crear un arreglo de ceros, que simula el espacio en el que se llevará a cabo el análisis estructural. Este arreglo tridimensional actúa como una representación básica del dominio estructural, donde cada elemento del arreglo puede representar un punto en el espacio tridimensional y ser usado para futuros cálculos de elementos finitos.

#### Introducción a Paraview
Proseguimos con el desarrollo de un script que exporta datos estructurales (presiones y desplazamientos) a un formato compatible con Paraview, concretamente usando la biblioteca `vtk`. Esta tarea implicó la conversión de un DataFrame de `pandas` a un conjunto de datos VTK, que luego se guardó en un archivo VTP. Este archivo puede ser fácilmente abierto y visualizado en Paraview, permitiendo una inspección detallada de los campos vectoriales y escalares asociados con el análisis estructural.

#### Funciones Auxiliares en Python
Implementamos una función para calcular el tensor de deformaciones para un elemento finito tetraédrico, basado en su matriz de desplazamientos nodales. Esta función usa métodos de álgebra lineal para calcular las derivadas parciales de las funciones de desplazamiento, esenciales para obtener las deformaciones en el elemento.

**Parte II: Pre-procesamiento y Análisis**

#### Pre-procesado de Datos
Diseñamos un script para generar un mallado de tetraedros a partir de una geometría básica, utilizando bibliotecas especializadas en malla como `meshpy`. El proceso implicó definir puntos y caras del modelo geométrico, configurar y generar la malla, y finalmente, verificar la calidad y la adecuación de los tetraedros generados según criterios de densidad y uniformidad.

#### Implementación de Función de Forma
Desarrollamos y validamos la función de forma para un elemento tetraédrico. La implementación se basó en interpolaciones lineales y se verificó calculando la función de forma en varios puntos dentro del dominio del elemento, asegurando su correcta implementación y su capacidad para interpolar desplazamientos y otras variables físicas dentro del elemento.

#### Ensamblaje de Matrices
Programamos el ensamblaje de la matriz de rigidez global para una estructura mallada con tetraedros. Este proceso incluyó la integración de matrices de rigidez locales de cada tetraedro en una matriz global, teniendo en cuenta las condiciones de contorno y asegurando la simetría de la matriz resultante, lo que es crucial para la estabilidad y precisión del modelo numérico.

**Parte III: Solución y Post-procesamiento**

#### Solución de Sistema de Ecuaciones
Implementamos un solver para resolver el sistema de ecuaciones lineales derivado del método de elementos finitos. Discutimos la selección del método numérico, optando por solucionadores iterativos o directos según el tamaño y las características del sistema, enfocándonos en la eficiencia y precisión de la solución.

#### Post-procesamiento
Generamos un script para calcular y visualizar las tensiones y deformaciones en la estructura analizada, integrando los resultados con Paraview para facilitar la visualización y la interpretación de los resultados en un contexto gráfico.

#### Caso de Estudio
Aplicamos todo el flujo de trabajo a un caso de estudio estructural proporcionado, desde el pre-procesamiento hasta el post-procesamiento. Discutimos cómo cada decisión tomada en cada etapa afectó el resultado final, proporcionando una comprensión integral de la interacción entre los datos de entrada, el modelo numérico y los resultados de análisis estructural.

