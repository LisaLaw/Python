#Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
#Example:
#Input: [[1, 2], [2, 3], [4, 5]]
#Output: [[1, 3], [4, 5]]
#Input: [[1, 5], [2, 3]]
# Output: [[1, 5]]

iv_list = [[1, 2], [4, 5], [2, 3]]
print('original list', iv_list)
my_list = []

list_count = 0 #used to access indici of the outer list

next_iv = iv_list[list_count+1] #next intervall that is being compared to current item



for iv in iv_list:
    
    if list_count == (len(iv_list) ) : #break out of loop when we've reached last intervall
        break

    new_iv = iv #the overlapping intervall that will get put in the final list 

    if iv[1] < next_iv[0] and iv[0] < next_iv [0]: #if no overlap, go to next item
        new_iv = iv
        print('iv', iv, 'new_iv', new_iv)

        print('iv list', iv_list)
    
    elif iv[0] > next_iv[1] and iv[1] > next_iv[1]:
        new_iv = iv
        print('whaat')

    elif iv[0] > next_iv[0] : #comparing first number of intervall; getting first number of new_iv
        new_iv[0] = next_iv[0]
        print('2')
        print('iv', iv, 'new_iv', new_iv)
    
    elif iv[1] <= next_iv[1] : #comparing second number of intervall; getting second number of new_iv
        new_iv[1] = next_iv[1]
        print('3')
        print('iv', iv, 'new_iv', new_iv)

    print('ivs are ', iv)
    my_list.append(new_iv)
    print('my list', my_list)
    list_count = list_count + 1

print('for the input list of ', iv_list)
print('The final ivs are: ', my_list)
