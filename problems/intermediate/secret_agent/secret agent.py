def crackCodeN(code):
   
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    
    result = list(adjacent[code[0]])
    
    
    for digit in code[1:]:
      
        current_possibilities = adjacent[digit]
        
       
        new_result = []
        for prefix in result:
            for possibility in current_possibilities:
                new_result.append(prefix + possibility)
        result = new_result
    
    return result