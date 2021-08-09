from tkinter import * 
from tkinter import ttk,messagebox

def calculate():
	input1 = int(value1.get())
	input2 = int(value2.get())
	res = input1 + input2
	result.set(f'คำตอบ {res:,d}')

def circle():
	input1 = int(rad.get())
	res = 3.1412 * (input1**2)
	Result.set(f'คำตอบ{res:f}')

def add():
	messagebox.showerror('Error','ตัวอย่าง1+1=2')

def newfile():
	GUI2 = Tk()
	GUI2.title('Calculate Program')
	GUI2.geometry('500x500')

	L1 = Label(GUI2,text='hello i am newtab',font=FONT)
	L1.pack(pady=50)

	GUI2.mainloop()

GUI = Tk()

GUI.title('Calculation Program')
GUI.geometry('500x500')

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

F1=Frame(Tab)
F2=Frame(Tab)

Tab.add(F1,text='พื้นฐานการคำนวณ')
Tab.add(F2,text='วงกลม')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='Close',command=GUI.quit)
file.add_command(label='New File',command=newfile)
menubar.add_cascade(label='file',menu=file)

calc = Menu(menubar,tearoff=0)
calc.add_command(label='การบวก')
calc.add_command(label='การลบ')
calc.add_command(label='การคูณ')
calc.add_command(label='การหาร')
menubar.add_cascade(label='การคำนวณ',menu=calc)

FONT = ('Angsana New',18)

L1 = Label(F1,text='โปรแกรมคำนวณ',font=FONT)
L1.pack(pady=50)

value1 = StringVar()
value2 = StringVar()
result = StringVar()
result.set('------')

E1 = ttk.Entry(F1,textvariable=value1)
E1.pack(ipady=30,ipadx=50)

E2 = ttk.Entry(F1,textvariable=value2)
E2.pack(ipady=30,ipadx=50,pady=50)

B1 = ttk.Button(F1,text='คำนวณ',command=calculate)
B1.pack()

LResult = Label(F1,textvariable=result,font=FONT)
LResult.pack(pady=20)

####F2#####################

L1F2 = Label(F2,text='คำนวณพื้นที่วงกลม',font=FONT)
L1F2.pack(pady=50)

rad = StringVar()
Result = StringVar()
Result.set('-------คำนวณพื้นที่ทรงกลม-------')

E1F2 = ttk.Entry(F2,textvariable=rad)
E1F2.pack(ipady=30,ipadx=50)

B1F2 = ttk.Button(F2,text='คำนวณ',command=circle)
B1F2.pack()

LResultF2 = Label(F2,textvariable=Result,font=FONT)
LResultF2.pack()



GUI.mainloop()