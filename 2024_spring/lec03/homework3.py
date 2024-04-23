

def cancellation(input_list, stop_word):
    output_list = []
    for x in input_list:
        if x == stop_word:
            break
        output_list.append(x)
    return output_list
    

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for x in input_list:
        if x!=skip_word:
            output_list.append(x)
    return output_list

def my_average(input_list):
    sum = 0
    for x in input_list:
        sum+=x
    return sum/len(input_list)

