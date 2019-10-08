from managers.cc_help import get_type, CC_TYPE_CHOICES
from handle_json_module.resolve_json import main_solve_json
import random as ran


def use_ccmodule():
    """ CREDIT CARDS MODULE """

    information = """ CREDIT CARDS MODULE """
    print('\n\n {} \n\n\n'.format(information))
    
    cc_number = str(main_solve_json())
        
    code_cc_type = get_type(cc_number)

    tuple_lenght = len(CC_TYPE_CHOICES) 

    for index in range(tuple_lenght):
        single_tuple = CC_TYPE_CHOICES[index] # (x, 'type cc') x = number
        if code_cc_type == single_tuple[0]:
            code_cc_type = single_tuple[0]
            break    
    
    print('\n\n Credit card tuple: {}'.format(CC_TYPE_CHOICES[code_cc_type]))
    

def test_2index():
    """ TESTENDIG 2 INDEXS IN FOR LOOP WIHT list() """
    information = """ TESTENDIG 2 INDEXS IN FOR LOOP WIHT list() """
    print('\n\n {} \n\n\n'.format(information))

    list_values = []
    index = list()

    for i in range(10):
        x = ran.randint(1, 300)
        list_values.append(x)
        index.append(i)

    for index, value in enumerate(list_values, start=1):
        print('index: {} | value: {}'.format(index, value))


def main():
    """ Main method that controll execution of project """

    print('\n\n')

    # test_2index()
    use_ccmodule()
     
    print('\n\n\n')


if __name__ == "__main__":
    main()

