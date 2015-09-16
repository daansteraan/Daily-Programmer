text_file = open('testa.txt')

def contig(text_file):
    rows = [line.split() for line in text_file]

    ascii_height = int(rows[0][0])
    ascii_length = int(rows[0][0])
    
    for lists in rows[1:]:
        for element in lists:
            if set(element) != set(['x']):
                lists.pop(lists.index(element))
    
    counter = 0
    
    for list_element in rows[1:ascii_height+1]:
        print list(list_element)
        for item in list_element:
            
            
            if (len(item) > 1) and (len(list(list_element)) <= ascii_length):
                counter += 1
    return counter
        
print contig(text_file)             
