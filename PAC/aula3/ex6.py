def intersects(a1, b1, a2, b2):
    if a1 > b2 or a2 > b1:
        return False
    else:
        return True
    
print(intersects(1, 3, 2, 4))