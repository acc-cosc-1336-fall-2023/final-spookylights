def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    x = y = z = 0
    dna1 = len(dna_string1)
    dna2 = len(dna_string2)
    
    
    for i in range(dna1):
        if dna_string1[i:i+dna2] == dna_string2:
            if x == 0:
                x = i + 1
                
            elif y == 0:
                y = i + 1
                
            elif z == 0:
                z = i + 1

    return x, y, z               

    

