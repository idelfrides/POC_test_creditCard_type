"""
 This medule recover the token generated by OAuth2 API
 and sent it to get_token2 view
"""

# import modules

import os
import json

class JsonModule(object):
    """ Json Module class 
        ==> used on solve_json_method  <==
        json.load(fp) - fp must be a text file or
        binary file containing a json document
        ------------------------------------------
        json.loads(s) - s must be a str, bytes or
        bytearray instance containing a json document.
        return a python dictionary
    """
    
    def __init__(self):
        """ init method does nothing """
        pass
    

    def solve_json_method(self, dir, jsonfile):
        """ Solve json method """
        
        os.chdir(dir) 
        mycontent = None

        try:
            myfile = open(jsonfile  , 'r')
            mycontent = myfile.read()
            file_name = myfile.name
            myfile.close()
            print('\n SUCCESS \n File {} was opened and read successfully.'.format(file_name))
        except Exception as error:
            print('\n ERROR \n Error try to open a file.\n Python said: {}'.format(error))

        self.show_info2user()
     
        new_content = json.loads(mycontent)

        return new_content


    def show_info2user(self):
        """ Show information of method used """
        info_sol = """
        ----------------------------------------
            THIS IS THE SOLUTION PERFORMED
            USING JSON METHOD - loads()
        ----------------------------------------
        """
        print('{}'.format(info_sol))
        print('\n')
