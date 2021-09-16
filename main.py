import math

#Kinematics Equation solver (for NeoTech)
#Make more user friendly by making variables function-wise (should I?)

print ("Welcome to this Kinematics Equation solver!")
print("Please fill the parameters. You can fill the unknown one(s) with 0.")

'''
v=u+at 
V^2 = u^2 + 2as
S = ut+1/2 at^2
'''
warning = print("\nWarning: This program currently *does not* support units of measurement while solving equations\n")
u = float(input("Please enter the initial velocity: "))
v = float(input("Please enter the final velocity: "))
a = float(input("Please enter the acceleration: "))
t = float(input("Please enter the time: "))
s = float(input("Please enter the displacement: "))





def equation1():
    if v != 0:
        options = float(input("1. Initial velocity (u) \n2. Acceleration (a)\n3. Time (t)\nWhat do you want to solve for? "))
        if options == 1:
            ans = v - (a*t)
            print("The initial velocity is ",ans)

        elif options == 2:
            ans = (v-u)/t
            print("The acceleration is ",ans)

        elif options == 3:
            ans = (v-u)/a
            print("The time is ",ans)

        else:
            print("Invalid input")

    else:
        print("Invalid input")


def equation2():
    if v**2 != 0:
        options = float(input("1. Initial velocity (u) \n2. Acceleration (a)\n3. Displacement (s)\nWhat do you want to solve for? "))
        if options == 1:
            ans = math.sqrt(v**2 - (2*a*s))
            print("The initial velocity is ",ans)

        elif options == 2:
            ans = ((v**2 - u**2))/(2*s)
            print("The acceleration is ",ans)

        elif options == 3:
            ans = ((v**2 - u**2))/(2*a)
            print("The displacement is ",ans)

    else:
        print("Invalid input")

def equation3():
    if s != 0:
        options = float(input("1. Initial velocity (u) \n2. Acceleration (a)\n3. Time (t)\nWhat do you want to solve for? "))
        if options == 1:
            ans = (s-((1/2)*a*(t**2)))/t
            print("The initial velocity is ",ans)

        elif options == 2:
            ans = ((2*(s-(u*t))))/(t**2)
            print("The acceleration is ",ans)

        elif options == 3:
            ans = ((s-(1/2)*a*(t**2)))/u
            print("The time is ",ans)

    else:
        print("Invalid input")

choice = float(input("\n1. v=u+at\n2. v^2=u^2 + 2as\n3. S=ut+1/2 at^2 \nPlease enter the equation you want to solve for: "))

if choice == 1:
    equation1()
elif choice == 2:
    equation2()
elif choice == 3:
    equation3()

        


        





    

        







