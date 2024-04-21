
from tkinter import *
from pygame import mixer # this module helps to play sounds
import speech_recognition
mixer.init()

root =Tk()#objecct to tkinter class
root.title("smart calculator")#putting title
root.config(bg="dodgerblue3")#giving colour
root.geometry('680x486+100+100')#giving width and height,coordinates (100,100)


logoImage = PhotoImage(file='logo.png')#adding casio logo
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = square_root(eval(ex))#eval function converts int string,float string into int ,float respectively.

        elif value == 'π':
            answer =calculate_pi()

        elif value == 'cosθ':
            answer = calculate_cos(eval(ex))

        elif value == 'tanθ':
            answer = calculate_sin(eval(ex))/calculate_cos(eval(ex))

        elif value == 'sinθ':
            answer = calculate_sin(eval(ex))

        elif value == '2π':
            answer = 2 * calculate_pi()
            
        elif value == 'cosh':
            answer = calculate_cosh(eval(ex))

        elif value == 'tanh':
            answer = calculate_sinh(eval(ex))/calculate_cosh(eval(ex))

        elif value == 'sinh':
            answer = calculate_sinh(eval(ex))

        elif value == chr(8731):#cube root
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = ln(eval(ex))

        elif value == 'deg':
            answer = radians_to_degrees(eval(ex))

        elif value == "rad":
            answer = degrees_to_radians(eval(ex))#passing degrees to get answer in radians

        elif value == 'e':
            answer = e=calculate_e()
            print(e)
        

        elif value == 'log₁₀':
            answer = calculate_log10(eval(ex))

        elif value == 'x!':
            answer=factorial(eval(ex))
           
                
                
             
            

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

        


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
def square_root(number, epsilon=1e-6):#newton raphson method and babylonain method can get square root ,here i use babylonain method
    if number < 0:
        raise ValueError("Square root is not defined for negative numbers.")

    guess = number  # Initial guess
    while True:
        new_guess = 0.5 * (guess + number / guess)  # Babylonian formula
        if abs(new_guess - guess) < epsilon:
            return new_guess
        guess = new_guess


def calculate_pi():#Bailey-Borwein-Plouffe (BBP) formula.to calculate pi value.
    pi = 0
    k = 0

    while True:
        numerator = (1 / 16**k) * ((4 / (8*k + 1)) - (2 / (8*k + 4)) - (1 / (8*k + 5)) - (1 / (8*k + 6)))
        pi += numerator
        k += 1

        if abs(numerator) < 1e-15:#1e-15 (which is scientific notation for 1 multiplied by 10 to the power of -15,
            break

    return pi

def exponent(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

def degrees_to_radians(degrees):
    pi = 3.141592653589793  # Approximation of pi
    radians = (degrees * pi) / 180
    return radians

def radians_to_degrees(radians):
    pi = 3.141592653589793
    degrees=(radians*180)/pi
    return degrees

def calculate_sin(angle, terms=10):#calculating sin value using taylors series
    angle_rad = degrees_to_radians(angle)
    sin_val = 0

    for n in range(terms):
        numerator = (-1) ** n * angle_rad ** (2 * n + 1)
        denominator = factorial(2 * n + 1)
        term = numerator / denominator
        sin_val += term

    return sin_val

def calculate_cos(angle, terms=10):# cos using taylor series expansion
    angle_rad = degrees_to_radians(angle)
    cos_val = 0

    for n in range(terms):
        numerator = (-1) ** n * angle_rad ** (2 * n)
        denominator = factorial(2 * n)
        term = numerator / denominator
        cos_val += term

    return cos_val

def calculate_e(terms=10):
    e_val = 1
    factorial = 1

    for n in range(1, terms):
        factorial *= n
        e_val += 1 / factorial

    return e_val

e = calculate_e(10)

def ln(x):
    if x <= 0:
        return float('-inf')

    n = 100  # Number of terms in the Taylor series
    result = 0.0

    for i in range(1, n + 1):
        term = (-1) ** (i + 1) * ((x - 1) ** i) / i
        result += term

    return result

# Test the ln() function
x = 2.0
ln_x = ln(x)
print(f"ln({x}) = {ln_x}")


def calculate_log10(x):# we use the concept of repeated division
    if x <= 0:
        return float('nan')  # Return NaN for invalid input

    count = 0
    while x >= 10:
        x /= 10
        count += 1

    return count





def calculate_sinh(x):
    return (e**(x) - e**(-x)) / 2

def calculate_cosh(x):
    return(e**(x)+e**(-x))/2



entryField=Entry(root,font=('Arial',20,'bold'),bg='dodgerblue3',fg='white',bd=10,relief=SUNKEN,width=30)#entry field features
entryField.grid(row=0,column=0,columnspan=8)

micImage = PhotoImage(file='microphone.png')#adding microphone logo
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3')
micButton.grid(row=0, column=7)


button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",#chr(8731) is cube root,chr(247) is division symbol in unicode
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue=1
columnvalue=0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()#object of tkinter class to loop everytime
