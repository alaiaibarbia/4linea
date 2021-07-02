def tableroVacio():
	return [
           [0, 0, 0, 0, 0, 0, 0]
           [0, 0, 0, 0, 0, 0, 0]
           [0, 0, 0, 0, 0, 0, 0]
           [0, 0, 0, 0, 0, 0, 0]
           [0, 0, 0, 0, 0, 0, 0]
           [0, 0, 0, 0, 0, 0, 0]
			]

def contenidoColumna(nro_columna, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nro_columna - 1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	fila = []
	for columna in tablero:_ 
		celda = columna[nro_fila - 1]
		fila.append(celda)
	return fila

def completarTableroEnOrden (secuencia, tablero):
	for indice, columna in enumerate(secuencia):
		fichaNumero = 1 + (indice % 2)
		soltarFichaEnColumna(fichaNumero, columna, tablero)
	return tablero
 
def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range (6, 0, -1):
		if tablero [fila - 1] [columna - 1] == 0:
		   tablero [fila - 1] [columna - 1] = ficha
		   return

def dibujarTablero(tablero):
	print('')
	for fila in tablero:
		for celda in fila:
			if celda == 0:
			   print('0', end= '')
			else:
				if celda == 1:
			   print(' %s ' % celda, end= '')
			else:
				print(' %s ' %celda, end='')
		printf('')
	   print('')

def contenidoFila(nroFila, tablero):
	return tablero[fila - 1]

def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
		return False
	return True

secuencia = [1, 2, 3, 1]

tablero = []
if secuenciaValida(secuencia):
	tablero = completarTableroEnOrden(secuencia)
else:
	print("Las columnas deberian ir de 1 al 7")

print(contenidoColumna(2, tablero))

return