#Calc Circle and Rectangle formulas

import circle
import rectangle

def Menu():
    print ("\n Menu",
         "\n1) Area of a circle",
         "\n2) Circumfrence of a circle",
         "\n3) Area of a rectangle",
         "\n4) Permimeter of a rectangle",
         "\n5) Quit\n")
    data=int(input("Enter your choice: "))
    return data


data=Menu()


while data!=5:
    if data==1:
        r=float(input("Enter the circle's radius: "))
        print("The area of circle = ", circle.findCircleArea(r));
        break
    elif data==2:
        r=float(input("Enter the circle's radius: "))
        print("The circumfrence of the circle is ", circle.findCircumfrence(r))
        break
    elif data==3:
        w=float(input("Enter the rectangle's width: "))
        l=float(input("Enter the rectangle's length: "))
        print("The area of the rectangle is ", rectangle.findRecArea(l, w))
        break
    elif data==4:
        w=float(input("Enter the rectangle's width: "))
        l=float(input("Enter the rectangle's length: "))
        print("The permimeter of the rectangle is ", rectangle.findRecPerim(l, w))
        break
    elif user==5:
        print("\nExiting the program")
    else:
        print("Error! unknown option! Please Try again!")

print("Thanks for asking!")
