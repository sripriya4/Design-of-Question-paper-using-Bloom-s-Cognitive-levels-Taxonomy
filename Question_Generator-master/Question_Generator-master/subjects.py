from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title("Question adder")
root.geometry("800x200")  
K1=list(["define", "find", "how", "label", "match", "name", "omit", "recall","spell", 
"tell", "what", "when", "where", "which", "who", "why"])
K2=list(["demonstrate", "extend", "illustrate", "infer", 
"outline", "relate", "rephrase", "show", "summarize", "translate"])
K3=list(["apply","experiment with", "identify", "interview", 
"make use of model", "organize","utilize"])
K4=list(["analyze", "assume", "categorize", "classify", "compare", "conclusion", "contrast", "discover", "dissect", "distinguish", "divide", 
"examine", "function", "inference", "inspect" "list", "motive", "relationships", "simplify", "survey", "take part in", "theme"])
K5=list(["agree", "appraise", "assess", "award","conclude", "criteria", "criticize", "decide", "deduct", "defend", "determine", "disprove","evaluate", "explain", 
"importance", "influence", "interpret", "judge", "justify", "mark", "measure", "opinion", "perceive", "prioritize", "prove", "rate", 
"recommend", "rule on", "select", "support", "value"])
K6=list(["adapt", "build", "change", "choose", "combine", "compile", "compose", "construct", "create", "delete", 
"design", "develop",  "discuss", "elaborate", "estimate", "formulate", "happen", "imagine", "improve", "invent", "make up", "maximize", 
"minimize", "modify", "original", "originate", "plan", "predict", "propose", "solution", "solve", "suppose", "test", "theory"])

def ADD():
    global comp1
    quest=h.get()
    comp1=quest
    comp1=quest.split()
    for x in range(len(comp1)):
                if comp1[x].lower() in K1:
                        quest1=quest+"::K1\n"
                        file.write(quest1)
                        messagebox.showinfo("K-LEVEL","The question is a K1 level question")
                elif comp1[x].lower() in K2:
                        quest2=quest+"::K2\n"
                        file.write(quest2)
                        messagebox.showinfo("K-LEVEL","The question is a K2 level question") 
                elif comp1[x].lower() in K3:
                        quest3=quest+"::K3\n"
                        file.write(quest3)
                        messagebox.showinfo("K-LEVEL","The question is a K3 level question") 
                elif comp1[x].lower() in K4:
                        quest4=quest+"::K4\n"
                        file.write(quest4)
                        messagebox.showinfo("K-LEVEL","The question is a K4 level question") 
                elif comp1[x].lower() in K5:
                        quest5=quest+"::K5\n"
                        file.write(quest5)
                        messagebox.showinfo("K-LEVEL","The question is a K5 level question") 
                elif comp1[x].lower() in K6:
                        quest6=quest+"::K6\n"
                        file.write(quest6)
                        messagebox.showinfo("K-LEVEL","The question is a K6 level question") 
    myLabel3.grid_forget()
    h.grid_forget()
    mybutton2.grid_forget()
    question()

def choi():
    global choice,myLabel3,mybutton2
    choice=g.get().upper()
    myLabel2.grid_forget()
    g.grid_forget()
    mybutton1.grid_forget()
    if choice=="YES":
        myLabel3 = Label(root, text="Enter the Question.")
        myLabel3.grid(row=3, column=5, padx=250, pady=10)
        global h
        h = Entry(root, width=50)
        h.grid(row=4, column=5, padx=250, pady=10)

        mybutton2= Button(root, text="ok",width=25,command=ADD)
        mybutton2.grid(row=5, column=5, padx=10, pady=10)
    else:
        response = messagebox.showinfo("EXITING!","Questions created Successfully.")
        if response =="ok":
            root.quit()

def subjects():
    myLabel1.grid_forget()
    e.grid_forget()
    mybutton.grid_forget()
    global subject, file_name,file,data
    subject=e.get().upper()
    file_name="C:\\Users\\rohan\\Downloads\\New folder\\Question_Generator-master\\Question_Generator-master\\Subjects\\"+subject+".txt"
    file = open(file_name,'a')
    file.close()
    file =open(file_name,'a')
    question()

def question():
    global myLabel2,g,mybutton1
    myLabel2 = Label(root, text="Do you want to enter more questions? Yes/No")
    myLabel2.grid(row=3, column=5, padx=250, pady=10)
    global g
    g = Entry(root, width=50)
    g.grid(row=4, column=5, padx=250, pady=10)

    mybutton1= Button(root, text="ok",width=25,command=choi)
    mybutton1.grid(row=5, column=5, padx=10, pady=10)

myLabel1 = Label(root, text="Welcome To Automatic Question Paper Generation System\nEnter the Subject Name. eg: 'computer networks'")
myLabel1.grid(row=0, column=5, padx=250, pady=10)

e = Entry(root, width=50)
e.grid(row=1, column=5, padx=250, pady=10)

mybutton= Button(root, text="ok",width=25,command=subjects)
mybutton.grid(row=2, column=5, padx=250, pady=10)
root.resizable(False, False) 
root.mainloop()    
file.close()
