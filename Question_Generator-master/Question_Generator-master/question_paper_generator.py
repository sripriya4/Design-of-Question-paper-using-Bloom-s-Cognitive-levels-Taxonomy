from tkinter import *
from tkinter import messagebox
import random
K1=list()
K2=list()
K3=list()
K4=list()
K5=list()
K6=list()
question1=list()
root = Tk()
root.title("Question paper generator using bloom texonomy")
root.geometry("500x700")  
def subjects():
    global mybutton
    mybutton['state'] = DISABLED
    global subject, file_name
    subject=e.get().upper()
    file_name="C:\\Users\\rohan\\Downloads\\New folder\\Question_Generator-master\\Question_Generator-master\\Subjects\\"+subject+".txt"
    #C:\Users\rohan\Downloads\New folder\Question_Generator-master\Question_Generator-master\Subjects\COMPUTER NETWORKS.txt
    print(file_name)
    try:
        with open(file_name,'r') as file:
                data = file.read().split("\n")#data contain single string seperated by \n
                data = data[:-1]
    except:
        messagebox.showerror("ERROR","File does not exists! Please make questions list of the subject first .")
        root.quit()
    file.close()
    for inputs in data:
        inp=inputs.split("::")
        question=inp[0]#contain question
        category=inp[1]#contain K1,K2,K3,K4,K5 OR K6
        if(category=='K1'):
                K1.append(question)#PUT IN LIST K1
        elif(category=='K2'):
                K2.append(question)#PUT IN LIST K2
        elif(category=='K3'):
                K3.append(question)#PUT IN LIST K3
        elif(category=='K4'):
                K4.append(question)#PUT IN LIST K4
        elif(category=='K5'):
                K5.append(question)#PUT IN LIST K5
        else:
                K6.append(question)#PUT IN LIST K6
    global output_text_name,mybutton1,myLabel2 
    output_text_name="C:\\Users\\rohan\\Downloads\\New folder\\Question_Generator-master\\Question_Generator-master\\Subjects\\"+subject+" Question Paper.txt"
    global f 
    f = open(output_text_name,'w')
    f.close()
    f =open(output_text_name,'r+')
    myLabel2= Label(root, text="Enter the SessionYear eg:2018-2019 ")
    myLabel2.pack()
    global a
    a = Entry(root, width=50)
    a.pack()
    mybutton1= Button(root, text="ok",width=25,command=session)
    mybutton1.pack()

def session():
    global mybutton1
    mybutton1['state'] = DISABLED
    global firstLine, sessionyear,mybutton2,myLabel3
    sessionyear = a.get().upper()
    firstLine="\t\t\t\t\t\t\t-----------------------BMS INSTITUTE OF TECHNOLOGY AND MANAGEMENT----------------------\n\t\t\t\t\t\t\t-----------------------------------------"+sessionyear+"---------------------------------------\n"
    f.write(firstLine)
    myLabel3= Label(root, text="Enter the Subject Code?")
    myLabel3.pack()
    global b
    b = Entry(root, width=50)
    b.pack()
    mybutton2= Button(root, text="ok",width=25,command=subject_code)
    mybutton2.pack()

def subject_code():
    global mybutton2
    mybutton2['state'] = DISABLED
    global secondLine,subjectcode,mybutton3,myLabel4
    subjectcode=b.get().upper()
    secondLine="\t\t\t\t\t\t\t------------------------------------"+subject+"|"+subjectcode+"|M.M=80-------------------------------------\n"
    f.write(secondLine)
    myLabel4= Label(root, text="Enter the Semester?")
    myLabel4.pack()
    global c
    c = Entry(root, width=50)
    c.pack()
    mybutton3= Button(root, text="ok",width=25,command=semester)
    mybutton3.pack()

def semester():
    global mybutton3
    mybutton3['state'] = DISABLED
    global thirdLine,sem
    sem=c.get().upper()
    thirdLine="\t\t\t\t\t\t\t---------------------------------------Semester-"+sem+"-----------------------------------------\n"
    f.write(thirdLine)
    f.write("\t\t\t\t\t\t\tPART A\n")#part a\
    levels()

def levels():
    myLabel1.pack_forget()
    e.pack_forget()
    mybutton.pack_forget()
    myLabel2.pack_forget()
    a.pack_forget()
    mybutton1.pack_forget()
    myLabel3.pack_forget()
    b.pack_forget()
    mybutton2.pack_forget()
    myLabel4.pack_forget()
    c.pack_forget()
    mybutton3.pack_forget()
    global cnt,myLabel5,g,mybutton4,g,button
    cnt=1
    count=cnt 
    myLabel5= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel5.pack()
    g = Entry(root, width=50)
    g.pack()
    mybutton4 = Button(root, text="ok",width=25,command=lambda: get1(1))
    mybutton4.pack()
    button=Button(root,text='next question',width=25,command=q2)
    button.pack()
def q2():
    global cnt,myLabel6,h,mybutton5,button1
    button.pack_forget()
    myLabel5.pack_forget()
    g.pack_forget()
    mybutton4.pack_forget()
    cnt=2
    count=cnt 
    myLabel6= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel6.pack()
    h = Entry(root, width=50)
    h.pack()
    mybutton5 = Button(root, text="ok",width=25,command=lambda: get2(2))
    mybutton5.pack()
    button1=Button(root,text='next question',width=25,command=q3)
    button1.pack()
def q3():
    global cnt,myLabel7,i,mybutton6,button2
    button1.pack_forget()
    myLabel6.pack_forget()
    h.pack_forget()
    mybutton5.pack_forget()
    cnt=3
    count=cnt 
    myLabel7= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel7.pack()
    i = Entry(root, width=50)
    i.pack()
    mybutton6 = Button(root, text="ok",width=25,command=lambda: get3(3))
    mybutton6.pack()
    button2=Button(root,text='next question',width=25,command=q4)
    button2.pack()
def q4():
    global cnt,myLabel8,j,mybutton7,button3
    button2.pack_forget()
    myLabel7.pack_forget()
    i.pack_forget()
    mybutton6.pack_forget()
    cnt=4
    count=cnt 
    myLabel8= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel8.pack()
    j = Entry(root, width=50)
    j.pack()
    mybutton7 = Button(root, text="ok",width=25,command=lambda: get4(4))
    mybutton7.pack()
    button3=Button(root,text='next question',width=25,command=q5)
    button3.pack()
def q5():
    global cnt,myLabel9,k,mybutton8,button4
    button3.pack_forget()
    myLabel8.pack_forget()
    j.pack_forget()
    mybutton7.pack_forget()
    cnt=5
    count=cnt 
    myLabel9= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel9.pack()
    k = Entry(root, width=50)
    k.pack()
    mybutton8 = Button(root, text="ok",width=25,command=lambda: get5(5))
    mybutton8.pack()
    button4=Button(root,text='next question',width=25,command=q6)
    button4.pack()
def q6():
    global cnt,myLabel10,l,mybutton9,button5
    button4.pack_forget()
    myLabel9.pack_forget()
    k.pack_forget()
    mybutton8.pack_forget()
    cnt=6
    count=cnt 
    myLabel10= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel10.pack()
    l = Entry(root, width=50)
    l.pack()
    mybutton9 = Button(root, text="ok",width=25,command=lambda: get6(6))
    mybutton9.pack()
    button5=Button(root,text='next question',width=25,command=q7)
    button5.pack()
def q7():
    global cnt,myLabel11,m,mybutton10,button6
    button5.pack_forget()
    myLabel10.pack_forget()
    l.pack_forget()
    mybutton9.pack_forget()
    cnt=7
    count=cnt 
    myLabel11= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel11.pack()
    m = Entry(root, width=50)
    m.pack()
    mybutton10 = Button(root, text="ok",width=25,command=lambda: get7(7))
    mybutton10.pack()
    button6=Button(root,text='next question',width=25,command=q8)
    button6.pack()
def q8():
    global cnt,myLabel12,n,mybutton11
    global mybutton12
    button6.pack_forget()
    myLabel11.pack_forget()
    m.pack_forget()
    mybutton10.pack_forget()
    cnt=8
    count=cnt 
    myLabel12= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel12.pack()
    n = Entry(root, width=50)
    n.pack()
    mybutton11 = Button(root, text="ok",width=25,command=lambda: get8(8))
    mybutton11.pack()
    mybutton12 = Button(root, text="exit",width=25,command=root.quit)
    mybutton12.pack()

def get1(num):
    global mybutton4
    mybutton4['state'] = DISABLED
    global level
    level=g.get().upper()
    choice(num)
    return


def get2(num):
    global mybutton5
    mybutton5['state'] = DISABLED
    global level
    level=h.get().upper()
    choice(num)
    print("hdjesbdkbskjdb")
    return


def get3(num):
    global mybutton6
    mybutton6['state'] = DISABLED
    global level
    level=i.get().upper()
    choice(num)
    return



def get4(num):
    global mybutton7
    mybutton7['state'] = DISABLED
    global level
    level=j.get().upper()
    choice(num)
    return


def get5(num):
    global mybutton8
    mybutton8['state'] = DISABLED
    global level
    level=k.get().upper()
    choice(num)
    return

def get6(num):
    global mybutton9
    mybutton9['state'] = DISABLED
    global level
    level=l.get().upper()
    choice(num)
    return

def get7(num):
    global mybutton10
    mybutton10['state'] = DISABLED
    global level
    level=m.get().upper()
    choices(num)
    return

def get8(num):
    global mybutton11
    mybutton11['state'] = DISABLED
    global level
    level=n.get().upper()
    choices(num)
    return

def choices(num):
    global mybutton11,mybutton10
    i=num
    while True:
        if level=="K1":
            ques=random.choice(K1)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K1\n"
                if (i % 2) != 0:
                     f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        elif level=="K2":
            ques=random.choice(K2)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K2\n"
                if (i % 2) != 0:
                    f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        elif level=="K3":
            ques=random.choice(K3)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K3\n"
                if (i % 2) != 0:
                        f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        elif level=="K4":
            ques=random.choice(K4)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K4\n"
                if (i % 2) != 0:
                        f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        elif level=="K5":
            ques=random.choice(K5)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K5\n"
                if (i % 2) != 0:
                        f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        elif level=="K6":
            ques=random.choice(K6)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]|K6\n"
                if (i % 2) != 0:
                        f.write("\t\t\t\t\t\t\tPARTB\n")
                f.write("\t\t\t\t\t\t\t"+temp_str)
                i=i+1
                break
        else:
            messagebox.showerror("ERROR","Enter only from K1-K6!!")
            mybutton10['state'] = ACTIVE
            mybutton11['state'] = ACTIVE
            break
    return
def choice(num):
    global mybutton4,mybutton5,mybutton6,mybutton7,mybutton8,mybutton9
    count=num
    while True:
        if level=="K1":
                ques=random.choice(K1)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]|K1\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        elif level=="K2":
                ques=random.choice(K2)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)   
                    temp_str=(str)(count)+")"+ques+"    [10M]|K2\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        elif level=="K3":
                ques=random.choice(K3)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]|K3\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        elif level=="K4":
                ques=random.choice(K4)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]|K4\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        elif level=="K5":
                ques=random.choice(K5)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]|K5\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        elif level=="K6":
                ques=random.choice(K6)
                if ques in question1:
                        continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]|K6\n"
                    f.write("\t\t\t\t\t\t\t"+temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\t\t\t\t\t\t\t----------------------------------------------------------------------------------------\n")
                        break
                    else:
                        OR="OR\n"
                        f.write("\t\t\t\t\t\t\t"+OR)
                        count=count+1
                        break
        else:
                messagebox.showerror("ERROR","Enter only from K1-K6!!")
                mybutton4['state'] = ACTIVE
                mybutton5['state'] = ACTIVE
                mybutton6['state'] = ACTIVE
                mybutton7['state'] = ACTIVE
                mybutton8['state'] = ACTIVE
                mybutton9['state'] = ACTIVE
                break
    return
        

    
myLabel1 = Label(root, text="Enter the Subject Name for which you want to generate question paper?")
myLabel1.pack()
e = Entry(root, width=50)
e.pack()
mybutton= Button(root, text="ok",width=25,command=subjects)
mybutton.pack()
root.mainloop()
f.close()