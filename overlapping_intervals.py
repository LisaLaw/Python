#Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
#Example:
#Input: [[1, 2], [2, 3], [4, 5]]
#Output: [[1, 3], [4, 5]]
#Input: [[1, 5], [2, 3]]
# Output: [[1, 5]]

iv_list = [[1, 5], [2, 3]]
my_list = []

list_count = 0 #used to access indici of the outer list

for iv in iv_list:
    if list_count == (len(iv_list) - 1) : #break out of loop when we've reached last intervall
        break
    
    next_iv = iv_list[list_count+1] #next intervall that is being compared to curren item
    new_iv = [0, 0] #the overlapping intervall that will get put in the final list 

    if next_iv[0] > iv[1] : #if no overlap, go to next item
        continue
    
    if iv[0] <= next_iv[0] : #comparing first number of intervall; getting first number of new_iv
        new_iv[0] = iv[0]
    else :
        new_iv[0] = next_iv[0]
    
    if iv[1] <= next_iv[1] : #comparing second number of intervall; getting second number of new_iv
        new_iv[1] = next_iv[1]
    else:
        new_iv[1] = iv[1]

    my_list.append(new_iv)
    list_count = list_count + 1

print('for the input list of ', iv_list)
print('The final ivs are: ', my_list)

