def find_sides(side):
    triplets = [[3,4,5],
            [5,12,13],
            [7,24,25],
            [8,15,17],
            [9,40,41],
            [11,60,61],
            [12,35,37]]
    for i in triplets[::-1]:
        for y in range (0,3):
            if (side/i[y]).is_integer()==True:
                multiple = side/i[y]
                single_triplet = [z * multiple for z in i]
                    
                a,b,c,unkown = single_triplet[0],single_triplet[1],single_triplet[2],single_triplet[y]
                if a != unkown and b != unkown:
                    return ("a right angle triange has the sides ",a, "and",b, "\n Find c")
                
                elif a!=unkown and c!=unkown:
                    return ("a right angle triange has the sides ",a, "and",c, "\n Find b")
                else:
                    return ("a right angle triange has the sides ",b, "and",c, "\n Find a")
                
    return False

