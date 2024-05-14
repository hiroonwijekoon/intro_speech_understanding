
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    output_dic = {}
    for i in range(len(input_list)):
        output_dic[i] = input_list[i]
    return output_dic




