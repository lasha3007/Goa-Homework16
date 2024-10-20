def xo(s):
    countO = 0
    countX = 0
    for i in s:
        if i == 'o' or i == 'O':
            countO += 1
        elif i == 'x' or i == 'X':
            countX += 1
    
    if countO == countX : 
        return True
    elif countO != countX: 
        return False
    else:
        return True
    