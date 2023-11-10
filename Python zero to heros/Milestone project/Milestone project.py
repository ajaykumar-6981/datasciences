
# print([1,2,3])

# print([1,2,3])
# print([4,5,6])
# print([7,8,9])

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

# example_row=[1,2,3]
# display([1,2,3],[4,5,6],[7,8,9])

# display(example_row,example_row,example_row)
row1=['','','']
row2=['','','']
row3=['','','']

display(row1,row2,row3)

def user_choice():
   choice='WRONG'
   acceptable_range=range(0,10)
   within_range=False
   # Two Condition to check
   while choice.isdigit()==False or within_range==False:
        choice=input("Please enter the value O-10:")
        if choice.isdigit()==False:
           print("Sorry that is not a digit!")
       # RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print("Sorry you are out of acceptable range")
                within_range=False

   return int(choice)


result=user_choice()


print(result)
row2[result]='X'
display(row1,row2,row3)


