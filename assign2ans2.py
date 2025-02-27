## PASCALS TRIANGLE
def pascals_triangle(raws):
    for i in range(raws):
        number = 1
        print(" " * (raws - i -1),end="")
        ##nested loop for each element
        for j in range(i + 1):
            print(number, end=" ")
            ## update the number for the next element in the raws
            number = number * (i -j) // (j+1)
       
        print()

pascals_triangle(5)