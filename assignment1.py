#+= operators to increase its value by 10
# a=10
# a+= 10
# print(a)

#marks and grad program
# marks = int(input('enter your marks'))
# print(marks)
# if(marks>=90):
#     print('your grad is A')
# elif(marks>=80):
#     print('your grad is B')
# elif(marks>=70):
#     print('your grad is C')
# elif(marks>=60):
#     print('your grad is D')
# else:
#     print('you re failed')
    #leap year or aleap year
year = int(input('enter a year: '))
if(year % 4 == 0 &  (year % 100 !=0 or year % 400 == 0)):
        print(f'{year} is a leap year')
else:
        print(f'{year} is not a leap year')
 