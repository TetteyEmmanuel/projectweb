# modified function name
def confidenceDaakye(list):
#Make changes and delete odd numbers from the list
    for value in list:
        if value % 2 ==0:
            list.remove(value)
    return list


def confi_add_even(even_list):
    add = 0
    for even_num in even_list:
        add += even_num
    return add


even_list = confidenceDaakye([1,2,3,4,5,6,7,8,9])
print(confi_add_even(even_list))