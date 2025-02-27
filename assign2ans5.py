# THE USE OF CONTINUE STATEMENT
# for i in range(1,6):
#     if i == 3:
#         continue 
#     print(i)
      ##ANOTHER EXAMPLE##
# INSTEAD OF RESTRUCTING THE LOOPS

#LISTS
lst = [1,3,4,6,7,9,10,12,15,17,18]
#loop through the list
for num in lst:
    if num % 3 !=0:
        continue
    print(num)