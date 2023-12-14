def find_sides(side):
    triplets = [
        [3, 4, 5],
        [5, 12, 13],
        [7, 24, 25],
        [8, 15, 17],
        [9, 40, 41],
        [11, 60, 61],
        [12, 35, 37]
    ]
    
    for triplet in triplets[::-1]:
        for i in range(3):
            if side % triplet[i] == 0:
                multiple = side // triplet[i]
                single_triplet = [z * multiple for z in triplet]
                
                a, b, c, unknown = single_triplet[0], single_triplet[1], single_triplet[2], single_triplet[i]
                
                if a != unknown and b != unknown:
                    return f"A right angle triangle has the sides {a} and {b}. Find c."
                elif a != unknown and c != unknown:
                    return f"A right angle triangle has the sides {a} and {c}. Find b."
                else:
                    return f"A right angle triangle has the sides {b} and {c}. Find a."
                
    return False
