""" The robot is placed at point (0,0). From (x, y) the robot can move to (x+1,y), (x-1, y), (x, y+1), and (x, y-1). 
Some points are dangerous and contain EMP Mines. To know which points are safe, we check
whether the sum digits of abs(x) plus the sum of the digits of abs(y) are less than or equal to 23. 
For example, the point (59,75) is not safe because 5 + 9 + 7 + 5 = 26, which is greater than 23. 
The point (-51, -7) is safe because 5 + 1 + 7 = 13, which is less than 23 """
import re

#Function to split numbers  
def fn_split(stringList): 
    return re.findall("[0-9]",str(stringList))

#Function to do addition from list
def fn_safe(sumList):
    #return sum(list(map(int, myList)))   
    l = sum([abs(int(l)) for l in sumList]) 
    return l <= 23

list_allXYpoints = []
list_gather = []
Y_max = 11 #11111111111111111111111 #numero maximo sumando cada digito da  23
X_max = 11 #11111111111111111111111
Y_ini = 0
X_ini = 0

while Y_ini <= Y_max :
    
    while X_ini <= X_max: 
        list_gather = [X_ini , Y_ini]
        sumDigits  =  fn_split(list_gather) 
        if  fn_safe(sumDigits) : 
            list_allXYpoints.append([X_ini,Y_ini]) 

        X_ini = X_ini + 1
    print(list_allXYpoints)

    Y_ini = Y_ini + 1
    X_ini = 0
    X_max = X_max - 1
    



    