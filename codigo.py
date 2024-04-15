from paraview.simple import *

# Carga el archivo VTK.
viga = OpenDataFile("viga.vtu")

# Aplicar un filtro 'Warp By Vector' para simular la deformación
warpByVector = WarpByVector(Input=viga)
warpByVector.Vectors = ['POINTS', 'vector_de_desplazamientos']  # cambiar 'vector_de_desplazamientos' por el nombre real del vector 

# Ajustar la escala de deformación si es necesario
warpByVector.ScaleFactor = 1.0

# Crear un mapa de colores basado en alguna magnitud física
# 'tensiones': datos que quieres visualizar
ColorBy(warpByVector, ('POINTS', 'tensiones'))

# Opciones adicionales para mejorar la visualización
Show(warpByVector)
Render()

# Guardar la imagen resultante, si se desea
SaveScreenshot("deformacion_y_tensiones.png")
