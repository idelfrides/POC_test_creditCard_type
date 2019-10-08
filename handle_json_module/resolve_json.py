from . import JsonModule as jm  
import random as ran


def main_solve_json():
    """ Main solve json file """
    
    jmo = jm.JsonModule()    
    
    start = 0
    end = 99
 
    directory = 'handle_json_module/utils/'
    json_file = 'card_data.json'

    list_content = jmo.solve_json_method(directory, json_file)

    ind = ran.randint(start, end)

    dict_content = list_content[ind]['data']['card']

    for i in dict_content:        
        print('\t', i, '-->', dict_content[i])

    list_values = list(dict_content.values())    

    print('\n')
    return list_values[1]

