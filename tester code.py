def cofindenceDaakye(list):

#Make changes and delete odd numbers from the list
    for value in list:
        if value % 2 ==0:
            list.remove(value)
    return list


print(cofindenceDaakye([1,2,3,4,5,6,7,8,9]))