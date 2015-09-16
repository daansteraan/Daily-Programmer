'''
Author: Danie Strijdom 
Date: 160915
'''

# iteratively compare all points, 
# find y-distance and x-distance,
# create a dictionary taht stores the result
# return dict key that has the smallest value

# store best value is a result var
# update variable value if smaller result is found

text_file = open('number232.txt')
element_list = []

for line in text_file:
    element = line.strip('\n')
    element_list.append(element)
    
print float(element_list[1].strip(')' + '(').split(',')[1])
