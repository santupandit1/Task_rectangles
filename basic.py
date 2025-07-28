#print("i love you baby girl, i want to kiss your tummy and eat you \"meow\"")
#🔹 
'''
1. Conditionals & Loops (Control Flow)
    1.    Print even numbers between 1 and 100.
    2.    Check if a number is divisible by both 3 and 5.
    3.    Print a multiplication table for any number.
    4.    Find all numbers between 1 to 100 that are divisible by 7 but not by 5.
    5.    Count how many numbers from 1 to N are prime (just use loops, not prime function).
    6.    Ask the user to enter a number and say whether it’s positive, negative, or zero.
    7.    Find the sum of all odd numbers from 1 to 100.
    8.    Print a right-angled triangle of stars with height n.
'''
#1
'''
def main():
    print(even())


def even():
    uni=[]
    for i in range(1,100):
        if(i%2==0):
            uni.append(i)
    return uni
    
main()
'''

#2
'''
def main():
    y= check()
    if(y==True):
        print("YES divisible by both")
    else:
        print("no")

def check():
    num = int(input("enter a number"))
    if(num%3==0 and num%5==0):
        return True
    else:
        return False

main()
'''
#3
'''
def main():
    table()

def table():
    num= int(input("Enter the number "))
    
    for i in range(1,11):
        mult = num*i
        print(mult)

main()
'''
#4
'''
def main():
    y= find()
    print(y)

def find():
    uni=[]
    for i in range(1,100):
        if(i%7==0 and i%5!=0):
            uni.append(i)
            #i=i+1
    return uni
            
main()
'''
#5
'''
def main():
    y= prime()  
    print(y)  



def prime():
    count=0
    x = int(input("enter a number"))
    for num in range(2,x+1):
        z=0
        for j in range(1,num+1):
            if(num%j==0):
                z=z+1
        if(z==2):
            count =count+1
    return count

main()
'''
#6
'''
num=int(input("Enter a number"))
if(num>0):
    print("The number is possitive")
elif(num<0):
    print("The number is negative")
elif(num==0):
    print("The num is zero")
    '''
#7
'''
def main():
    x=odd()
    print(f"The sum is:{x}")

def odd():
    sum=0
    for i in range(1,100):
        if(i%2!=0):
            sum=sum+i

    return sum

main()
'''
#8
'''
def main():
    triangle()

def triangle():
    h=int(input("Enter the  height of the desired triangle"))
    #b=int(input("Enter the  base of the desired triangle"))
    for i in range(1,h+1):
        y=0
        while(i != y):
            print("*",end="") #print on the same line
            y=y+1
        print()



main()
'''
#
'''
🔹 2. Functions & Exception Handling
    9.    Write a function to convert Celsius to Fahrenheit.
    10.    Write a function to divide two numbers and handle division by zero.
    11.    Write a function to calculate the area of a circle.
    12.    Ask the user for two inputs and add them. If the input is not a number, handle it gracefully.
    13.    Create a calculator function using if statements to support +, -, *, /.
    14.    Write a function that returns the max of 3 numbers without using built-in max.

🔹 3. Strings
    15.    Count the number of words in a sentence.
    16.    Find the number of times a character appears in a string.
    17.    Check whether a string contains only digits.
    18.    Convert all vowels in a string to uppercase.
    19.    Remove all special characters from a string.
    20.    Replace all spaces in a string with a hyphen (-).

🔹 4. Lists & Tuples
    21.    Find the average of a list of numbers.
    22.    Create a list of squares for numbers from 1 to 10 using a loop.
    23.    Swap the first and last elements of a list.
    24.    Count how many times each element appears in a list (without collections).
    25.    Print all elements in a tuple using a loop.
'''
#9
def main():
    x= convert()
    print(f"The farhen is:{x}")

def convert():
    c=float(input("Enter a temp in celsius"))
    z=(c*9)/5
    final = z+32
    return final

main()