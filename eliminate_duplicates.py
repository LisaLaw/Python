def eliminate_dup(list1):
    count = 1 #count starts at 1 because we need to check the second item against the first item in the first instance.
    while count < len(list1): #we only need to go through the lenght of the list.
        for item in list1:
            if item in list1[count:] : #count: shortens the list to the index item we're on at the moment until the end of the list
                list1.remove(item) #removes an item of the list if the item is a duplicate.
                count += 1  #increases the list index by one.
            else:
                count += 1  #increases the list index by one.
        
    return ''.join(list1) #puts all left-over numbers back together to a list.

my_list = input('Escribe una lista: ') #user-input for a list of numbers.
my_list = list(my_list)

print(eliminate_dup(my_list))