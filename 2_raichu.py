#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_egg_group(url_group5, url_group6):
    '''¿Con cuántas especies de pokémon puede procrear raichu? 
    (2 Pokémon pueden procrear si están dentro del mismo egg group). 
    Tu respuesta debe ser un número. Recuerda eliminar los duplicados.
    egg-group/5/ => Campo/Field
    egg-group/6/ => Hada/Fairy
    '''

    response_eg5 = requests.get(url_group5)
    response_eg6 = requests.get(url_group6)

    if response_eg5.status_code and response_eg6.status_code == 200: #validar conexion
        #Json para las dos consultas
        payload_eg5 = response_eg5.json()
        pokemon_species_eg5 = payload_eg5.get('pokemon_species',[])
        payload_eg6 = response_eg6.json()
        pokemon_species_eg6 = payload_eg6.get('pokemon_species',[])

        if pokemon_species_eg5:
            #c = 0
            list_pokemon5 = []#creal lista vacia para 5
            for specie in pokemon_species_eg5:
                pokemon_specie = specie['name']
                list_pokemon5.append(pokemon_specie)#guardar nombres de todos los pokemon que pertenece al mismo egg group
                #c = c + 1
            #print ("total de especies del egg group 5: ",c)

        if pokemon_species_eg6:
            #c = 0
            list_pokemon6 = []#creal lista vacia para 6
            for specie in pokemon_species_eg6:
                pokemon_specie = specie['name']
                list_pokemon6.append(pokemon_specie)
                #c = c + 1
            #print ("total de especies del egg group 6: ",c)
            
        union_lists_pokemon = list(set(list_pokemon5 + list_pokemon6))
        print("El número de especies con los que puede procrear raichu es: ",(len(union_lists_pokemon))-2)#menos 2 porque se excluye a sí mismo de cada egg group
    
    else:
            print(response_eg5.status_code)

if __name__ == '__main__':
    #enviando vals/params
    get_egg_group(url_group5 = 'https://pokeapi.co/api/v2/egg-group/5/', url_group6 = 'https://pokeapi.co/api/v2/egg-group/6/')
