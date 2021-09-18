#Use las simulaciones de montecarlo para calcular la probabilidad de que salga un par, una tercia o un pokar en una baraja 
import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    full = 0
    poker = 0
    tercia = 0
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
            elif val == 3:
                tercia += 1
            elif val == 4:
                poker += 1
            elif val == 3 and val == 2:
                full += 1


    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es {probabilidad_par}')

    probabilidad_tercias = tercia / intentos
    print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} cartas es {probabilidad_tercias}')

    probabilidad_poker = poker / intentos
    print(f'La probabilidad de obtener un poker en una mano de {tamano_mano} cartas es {probabilidad_poker}')

    probabilidad_full = full / intentos
    print(f'La probabilidad de obtener un full en una mano de {tamano_mano} cartas es {probabilidad_full}')



if __name__ == '__main__':
    tamano_mano = int(input('De cuantas cartas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)