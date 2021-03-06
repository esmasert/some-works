def first_fit(board, sticks):
    not_fit = []
    for a in range (len(sticks)): 
        l = sticks[a] #it will take the values of sticks
        d = 0  #it is used to check if we put the sticks in matrix
        for b in range (len(board)):
            if d: #if d is true it will break because it means the sticks is placed
                break        
            for c in range (len(board)):
                if board[b][c] == 0 and len(board) - c >= l:#if the item is 0 and l is smaller than or equal to free place which means there is place, the item takes value
                    for i in range(l):   
                        board[b][c+i] = a+1 #item will be equal to the order of place which fit in the matrix
                    d = 1 #if there is place in matrix it will take a value and d become true
                    break
            
        if not d: #if d is false it means item does not fit and that value of sticks is appended into the not.fit list
            not_fit.append(l)
    return not_fit
            
board = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
sticks = [3,2,2,1,3,2,4,1]
print(first_fit(board, sticks))

for i in range (len(board)): #nested for is used to show the matrix clearly
    for j in range (len(board[i])):
        print (board[i][j], end=' ')
    print()
    