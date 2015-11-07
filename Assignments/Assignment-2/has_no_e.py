def has_no_e (check):
    for letter in check:    
        if letter == 'e':
            result  = False
        else:
            result = True 
    
    return result 

reader = open('gadsby_stripped.txt', 'r')
contents = reader.readlines()
reader.close()
for line in contents:
    result = has_no_e (line)
    print(result)
