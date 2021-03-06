def contain_sublist(l1, l2):
    index = -1 #index is defined -1, because the smallest value of index can be 0
    for j in range (len(l2)): #first j is defined because, l2 will check according to the values of l1
        found = False  #found is defined to check whether l2's values have same order with the same values of l1 
        for i in range (len(l1)):
            if l1[i] == l2[j]: #first the items are checked to lists have same values
                if i > index:  #here we are looking for orders
                    found = True  
                    index = i  #if the item of l2 has a index in l1, then the next item of l2 has to get bigger index than the previous one in l1
                    break
        if not found: # if found is false, it means there is something wrong in list2 and the function will return automaticly to false 
            return False
    return True # if found is still true function will return to true
            
l1=[2, 'a',9, 5, 9, 0]
l2=['a',2, 9]

print(contain_sublist(l1, l2))