# TRIPLETS (A,B,C) WHERE A^2 B^2 = C^2

triplets = [(a,b,c)for a in range(1,51)for b in range(a,51)
            for c in range(b,51)if a**2 + b**2 == c**2]

#print the triplets
print(triplets)