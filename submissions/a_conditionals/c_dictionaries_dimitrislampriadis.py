# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Soroush Garivani
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Soroush Garivani
# Email: soroush.garivani@iaac.net
# Status: development
##################################################

# End of header section


# dictionaries

# city_1_name = 'Barcelona'
# city_1_population = 5474482
# city_1_unemployment_rate = 17.24
# city_2_name = 'Lisbon'
# city_2_population = 2827514
# city_2_unemployment_rate = 7.4
# city_3_name = 'Amsterdam'
# city_3_population = 2431000
# city_3_unemployment_rate = 3.3
# city_4_name = 'Athens'
# city_4_population = 3753783
# city_4_unemployment_rate = 2.82

cities_names = {'city1_name':'Barcelona', 'city2_name':'Lisbon', 'city3_name':'Amsterdam', 'city4_name':'Athens'}
cities_population = {'city1_pop':5474482, 'city2_pop':2827514, 'city3_pop':2431000, 'city4_pop':3753783}
cities_unempl_rates = {'city1_un':17.24, 'city2_un':7.4, 'city3_un':3.3, 'city4_un':2.82}
city = cities_names.values()
population = cities_population.values()
unemployment_rates = cities_unempl_rates.values()

print(population)


if cities_population['city1_pop'] > cities_population['city2_pop']:
    print(population)


my_cities = {'a':'Barcelona','b':'Venice','c':'Athens'}
cities = my_cities.values()
print('I have been to:')
if cities in cities:
    print(cities)
