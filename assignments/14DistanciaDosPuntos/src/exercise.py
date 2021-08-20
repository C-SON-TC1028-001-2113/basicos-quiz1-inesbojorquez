import math
def main():
    #escribe tu código abajo de esta línea
    x1 = float(input('Dame la x1:'))
    y1 = float(input('Dame la y1:'))
    x2 = float(input('Dame la x2:'))
    y2 = float(input('Dame la y1:'))
    r  = math.sqrt((x2 - x1)**2 + (y2-y1)**2 )
    print('El Resultado es: '+str(r))

if __name__ == '__main__':
    main()
