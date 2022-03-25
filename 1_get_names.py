#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import requests

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon?limit=151/'):
    '''
    Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre,
    incluyendo la primera del “at”. Tu respuesta debe ser un número.
    '''

    response = requests.get(url)
    if response.status_code == 200:#validar conexion
        payload = response.json()#formato json
        results = payload.get('results',[])
    
        if results:#si no es vacia
            count = 0
            for pokemon in results:
                name = pokemon['name']#guaradr nombres
                str_pokemon = Counter(name)#contar caracteres

                if "at" in name: #buscar at
                    count = count + 1
                    #print(name)
                    #print("Pokemons con at: .format{}",count)

                if str_pokemon['a']>=2: #buscar aa
                    count2 = count + 1
                    #print(name)
                    #print("Pokemons con 2a: .format{}",count)

            print("Pokemons con at: ",count)#impresion de at
            print("Pokemons con aa: ",count2)#impresion de aa
            #print(count)

    else:
        print(response.status_code)

if __name__ == '__main__':
    get_pokemons()#llamar la funcion

