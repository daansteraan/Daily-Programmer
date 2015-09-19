<<<<<<< HEAD
import math
import time

start = time.time()
=======

import math
>>>>>>> origin/master

text_file = open('number232.txt').readlines()

element_list = []
element_dict = {}

<<<<<<< HEAD
result = float('inf')
=======
result = 100000000000000000
>>>>>>> origin/master

for line in text_file:
   
    element = line.strip('\n'+'('+')').split(',')
    element_list.append(element)
      
for i in range(int(element_list[0][0])):
    element_dict[i] = element_list[i+1]
        
for i in element_dict.values():
    i[0] = float(i[0])
    i[1] = float(i[1])
    
def dist(x1,y1,x2,y2):   
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
for i in element_dict.values():
    for j in element_dict.values():
        if i != j:
            x1 = i[0]        
            y1 = i[1]
            x2 = j[0]
            y2 = j[1]
            
            test = dist(x1,y1,x2,y2)
            
            if test < result:
                result = test
                winner = [(x1,y1),(x2,y2)]
<<<<<<< HEAD

end = time.time()
runtime = end - start
                
print result
print winner
print 'RUNTIME: %.5f' % runtime                
=======
                
print result
print winner
                
               
>>>>>>> origin/master
