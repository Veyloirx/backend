def valoresAlrededor(matriz, inicio, final, camino_actual=None):

    if camino_actual is None:
        camino_actual = []  # Inicializar camino_actual en la primera llamada

    j, k = inicio

    # Añadir la coordenada actual al camino
    camino_actual.append((j, k))

    # Verificar si se ha llegado al punto final y detener el algoritmo
    if (j, k) == final:
        print(f"Llegamos al punto final 'F' en {j, k}")
        encontrado = True  # Cambiar la bandera a True
        return camino_actual

    # Marcar la casilla actual como visitada
    matriz[j][k] = '*'  

    coordenadas = [(j-1, k), (j+1, k), (j, k-1), (j, k+1)]
    valores_minimos = []
    min_valor = None

    for pos in coordenadas:
        if encontrado:
            break  # Si ya encontramos la 'F', detenemos todo
        j, k = pos

        if not (0 <= j < len(matriz) and 0 <= k < len(matriz[0])):
            continue

        if matriz[j][k] == '*':
            continue

        valor = matriz[j][k]

        if isinstance(valor, (int, float)):
            if min_valor is None or valor < min_valor:
                min_valor = valor
                valores_minimos = [(j, k)]
            elif valor == min_valor:
                valores_minimos.append((j, k))
    
    if not encontrado and len(valores_minimos) == 1:
        nueva_coordenada = valores_minimos[0]
        return valoresAlrededor(matriz, nueva_coordenada, final, camino_actual[:])
    elif not encontrado and len(valores_minimos) > 1:
        mejor_coordenada = evaluar_valores_repetidos(matriz, valores_minimos, camino_actual, final)
        if mejor_coordenada:
            return valoresAlrededor(matriz, mejor_coordenada, final, camino_actual[:])

    return camino_actual  # Retornar el camino si no hay más movimientos posibles

def evaluar_valores_repetidos(matriz, valores_repetidos, camino_actual, final):
    mejor_coordenada = None
    mejor_costo = float('inf')

    for coordenada in valores_repetidos:
        if encontrado:
            break  # Si ya encontramos la 'F', detenemos todo
        matriz_copia = [row[:] for row in matriz]
        resultados = valoresAlrededor(matriz_copia, coordenada, final, camino_actual=[])
        if resultados:
            costo_total = sum(matriz[x][y] for x, y in resultados if isinstance(matriz[x][y], (int, float)))
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_coordenada = coordenada

    return mejor_coordenada

def encontrar_inicio(matriz):
    for j, fila in enumerate(matriz):
        for k, elemento in enumerate(fila):
            if elemento == 'I':
                return j, k

def encontrar_final(matriz):
    for j, fila in enumerate(matriz):
        for k, elemento in enumerate(fila):
            if elemento == 'F':
                return j, k

def main():
    global encontrado
    matriz = [
        [ 'I', -1,  0,  0,  0, -1],
        [ -3,   2, -3,  0,  0,  1],
        [ -3,   1, -3,  1, -2,  3],
        [  0,   0,  3, -3,  2,  0],
        [  1,   2, -1,  0, -2,  3],
        [ -2,   0,  1, 'F', 1, -1]
    ]
    inicio = encontrar_inicio(matriz)
    final = encontrar_final(matriz)
    camino_final = valoresAlrededor(matriz, inicio, final)
    print("Camino final:", camino_final)

if __name__ == "__main__":
    main()

