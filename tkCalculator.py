import tkinter as tk # import tkinker

window = tk.Tk()

window.title("tkCalculator by caybue")

magicArray = []
magicString = ""
#Funcions



def writeDown(x):
     magicArray.append(x)

def writeResult():
    global resultOut
    magicString = ''.join(str(e) for e in magicArray)
    result = eval(magicString)
    resultOut.destroy()
    resultOut = tk.Label(window, text=result, font=("Arial", 15))
    resultOut.place(x= 0, y = 0)
    print(result)

def clearArray():
    global resultOut
    global magicArray
    magicArray.clear()
    magicString = ""
    resultOut.destroy()
    resultOut = tk.Label(window, text="Cleaned", font=("Arial", 15))
    resultOut.place(x= 0, y = 0)
    print(magicArray)
    print(magicString)

# Label
hr = tk.Label(window, text = "", height=3)
hr.grid(row=0)

resultOut = tk.Label(window, text= "Null", font=("Arial", 15))
resultOut.place(x= 0, y = 0)



#Buttons

btn7 = tk.Button(window, text="7", command = lambda: writeDown(7))
btn7.grid(row=1, column=0)

btn8 = tk.Button(window, text="8", command = lambda: writeDown(8))
btn8.grid(row=1, column=1)

btn9 = tk.Button(window, text="9", command = lambda: writeDown(9))
btn9.grid(row=1, column=2)

btnc = tk.Button(window, text="C", command = clearArray)
btnc.grid(row=1, column=3)

# Row 2
btn4 = tk.Button(window, text="4", command = lambda: writeDown(4))
btn4.grid(row=2, column=0)

btn5 = tk.Button(window, text="5", command = lambda: writeDown(5))
btn5.grid(row=2, column=1)

btn6 = tk.Button(window, text="6", command = lambda: writeDown(6))
btn6.grid(row=2, column=2)

btnmultiple = tk.Button(window, text="*", command = lambda: writeDown("*"))
btnmultiple.grid(row=2, column=3)

# Row 3

btn1 = tk.Button(window, text="1", command = lambda: writeDown(1))
btn1.grid(row=3, column=0)

btn2 = tk.Button(window, text="2", command = lambda: writeDown(2))
btn2.grid(row=3, column=1)

btn3 = tk.Button(window, text="3", command = lambda: writeDown(3))
btn3.grid(row=3, column=2)

btndivide = tk.Button(window, text="/", command = lambda: writeDown("/"))
btndivide.grid(row=3, column=3)

#Row 4

btn0 = tk.Button(window, text="0", command = lambda: writeDown(0))
btn0.grid(row=4, column=0)

btnplus = tk.Button(window, text="+", command = lambda: writeDown("+"))
btnplus.grid(row=4, column=1)

btnminus = tk.Button(window, text="-", command = lambda: writeDown("-"))
btnminus.grid(row=4, column=2)

btnequal = tk.Button(window, text="=", command = writeResult)
btnequal.grid(row=4, column=3)





window.mainloop()

