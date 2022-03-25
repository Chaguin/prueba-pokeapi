#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_pokemons(url='https://pokeapi.co/api/v2/generation/1/'):#se toma esta liga porque pertenece a la generacion 1
    '''
    Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación 
    (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: 
    [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.
    '''

    response = requests.get(url)
    list_weight = []#crear una lista para almacenar los weight de los pokemos de tipo fighting
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('pokemon_species',[])

        if results:
            print("consultando datos...")#hacer una consulta de cada uno de los pokemos de ese tipo
            for pokemon in results: 
                name = pokemon['name']
                url_weight_by_pokemon = 'https://pokeapi.co/api/v2/pokemon/{}'.format(name)#concatenar liga de la api con el nombre para obtener peso de c/u
                #print (url_weight_by_pokemon)
                response = requests.get(url_weight_by_pokemon)
                payload = response.json()
                weight_by_pokemon = payload.get('weight',[])
                list_weight.append(weight_by_pokemon)#agregar en una lista cada peso
                #print(weight_by_pokemon)
        else:
            print(response.status_code)

    list_weight.sort(reverse = True)#para ordenar de mayor a menor
    res = [list_weight[0], list_weight[-1]]#obtener el primero mayor y el ultimo menor
    print(res)#impresion del formato solicitado

if __name__ == '__main__':
    get_pokemons()#llamar la funcion