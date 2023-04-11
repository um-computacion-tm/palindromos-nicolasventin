def palindrome(word):
    word = word.lower()
    a = 0             # 0 Es la primer letra de la palabra
    b = len(word)-1   # para buscar la ultima letra de la palabra busco el largo len() y le resto 1 lo cual me da la ultima letra
    
    for i in range(0, len(word)): 
        
        #creo un rango entre 0 y el largo de la palabra
        
        if word [a] == word [b]: 
            #verificamos si a es = a y b, es decir verificamos si la primer letra es igual a la ultima
           a += 1 
            #Si verifica la primer letra que pase a la siguiente
            
           b -= 1 
            #si verifica la ultima letra que pase a la penultima y asi hasta terminar la palabra
        
        else:
            return False
    return True