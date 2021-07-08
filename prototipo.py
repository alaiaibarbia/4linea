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
	for celda in tablero[nro_fila-1]:
		fila.append(celda)
	return fila

def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range (6, 0, -1):
		if tablero [fila - 1] [columna - 1] == 0:
		   tablero [fila - 1] [columna - 1] = ficha
		   return

def completarTableroEnOrden(secuencia, tablero):
	ficha = 1
	for columna in secuencia: 
		soltarFichaEnColumna(ficha,columna,tablero)
		if ficha==1:
			ficha=2
		else:
			ficha=1
	return tablero 
 
def dibujarTablero(tablero):
	for fila in range(0,6):
	print("|",end="")
	for columna in range(0,7):
		if tablero[fila][columna]==0:
			print(" ", end="")
	else:
		 print(tablero[fila][columna],end="")
    print("|",end="")
    print();
  print("+-------+",end="")
  print();
  return 

def todasfilas(tablero):
	return tablero 

def secuenciaValida(secuencia):
	for columna in secuencia:
		if (columna < 1 or columna > 7):
		return False
	return True

def todascolumnas(tablero):
    for columna in range(0,6,1):
        for fila in range(0,6,1):
            celda=tablero[fila][columna]
            if(celda):
                print(celda,end='')
            else:
                print('0')
        print(" \n ")

secuencia = [1, 2, 3, 1]

tablero = []
if secuenciaValida(secuencia):
    tablero = completarTableroEnOrden(secuencia,tableroVacio())
    dibujarTablero(tablero)
else:
    print("Las columnas deberian ir de 1 al 7")

print(contenidoColumna(2, tablero))
# todascolumnas(tableroVacio())
# todasfilas(tableroVacio())