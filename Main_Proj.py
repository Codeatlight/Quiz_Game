from tkinter import *
from tkinter import messagebox as mb
import tkinter.font as font
import json
import random

def main():
    root1.destroy()
    root = Tk()
    root.geometry("1440x820")
    root.title("Thought Rattle")
    root.wm_iconbitmap('E:/Python/Python_files/1.My_Project/Reference_Proj/Resources&Samples/icon.ico')
    root.resizable(0,0)

    n_but = PhotoImage(file = 'E:/Python/Python_files/\
1.My_Project/Reference_Proj/Resources&Samples/next_but1.png')
    e_but = PhotoImage(file = 'E:/Python/Python_files/\
1.My_Project/Reference_Proj/Resources&Samples/nexit.png')
    f1 = PhotoImage(file = 'E:/Python/Python_files/1.My_Project/\
Reference_Proj/Resources&Samples/BG.png')
    f2 = PhotoImage(file = 'E:/Python/Python_files/1.My_Project/\
Reference_Proj/Resources&Samples/time1.png')

    l = Label(root,image=f1,width = 1500)
    l.pack()

    l2 = Label(root,image=f2,)
    l2.place(x= 1175,y = 75)
    
    
    with open('quiz.json') as f:
        obj = json.load(f)
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])
    z = zip(q,options,a)
    l = list(z)
    random.shuffle(l)
    q,options,a=zip(*l)


    def countdown(time, msg='Time Left : '):
        time-=1
        status.config(text=f'{msg}{time}seconds',font = ("Times", 16,'bold underline'))
        if time != 0:
            root.after(1000, countdown, time)
        else:
            obj = Quiz()
            obj.display_result()

    status = Label(root)
    status.place(x=1192 , y = 90)
    countdown(900)


    class Quiz:
        def __init__(self):
            self.qn = 0
            self.qno = 1
            self.quest = StringVar()
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0


        def question(self, qn):
            t = Label(root, text="Thought Rattle", width=50, bg="gray7", fg="deep pink", font=("times", 40, "bold"))
            t.place(x= -90 , y = 5)
            self.quest.set(str(self.qno)+"."+q[qn])
            qn = Label(root, bg = 'gray7',fg = 'white',textvariable = self.quest, width=38, \
                       font=("Lucida Handwriting", 22, "bold underline"), anchor="w")
            qn.place(x=350, y=230)
            return qn
        
        def radiobtns(self):
            val = 0
            b = []
            while val < 4:
                btn = Radiobutton(root, text="", bg = 'LightBlue3',fg = 'black' ,\
                                  variable=self.opt_selected,\
                                  value=1, font=("Lucida Handwriting", 14,'bold'))
                b.append(btn)
                btn.place(x=190, y=455)

                btn1 = Radiobutton(root, text="", bg = 'LightBlue3',fg = 'black' ,\
                                  variable=self.opt_selected,\
                                  value=2, font=("Lucida Handwriting", 14,'bold'))
                b.append(btn1)
                btn1.place(x=810, y=455)

                btn2 = Radiobutton(root, text="", bg = 'LightBlue3',fg = 'black' ,\
                                  variable=self.opt_selected,\
                                  value=3, font=("Lucida Handwriting", 14,'bold'))
                b.append(btn2)
                btn2.place(x=190, y=600)

                btn3 = Radiobutton(root, text="", bg = 'LightBlue3',fg = 'black' ,\
                                  variable=self.opt_selected,\
                                  value=4, font=("Lucida Handwriting", 14,'bold'))
                b.append(btn3)
                btn3.place(x=810, y=600)
                
                val += 1
            return b


        def display_options(self, qn):
            val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                  self.opts[val]['text'] = op
                  val += 1

        def buttons(self):
            frame1_btn = Button(root,command=self.nextbtn,image = n_but,\
                           height = 65,width = 225,borderwidth = 4 ,cursor = 'hand2')
            frame1_btn.place(x = 1095,y = 725)

            frame2_btn = Button(root,command=self.display_result,image = e_but,\
                           height = 65,width = 225,borderwidth = 4,cursor = 'hand2')
            frame2_btn.place(x = 110,y = 725)

        def checkans(self, qn):
            if self.opt_selected.get() == a[qn]:
                 return True
            
        def nextbtn(self):
            if self.checkans(self.qn):
                self.correct += 1
            self.qn += 1
            self.qno += 1
            if self.qn == len(q):
                self.display_result()
            else:
                self.quest.set(str(self.qno)+". "+q[self.qn])
                self.display_options(self.qn)

        def disable_event(self):
            pass

        def display_result(self):
            score = int(self.correct / len(q) * 100)
            result = "Score: " + str(score) + "%"
            wc = len(q) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            pop = Toplevel(root)
            pop.title("Thought Rattle")
            pop.geometry("350x325")
            pop.resizable(0,0)
            pop.protocol("WM_DELETE_WINDOW", self.disable_event)
            pop.config(bg="MediumOrchid4")
            pop.wm_iconbitmap('E:/Python/Python_files/1.My_Project/Reference_Proj/Resources&Samples/icon.ico')
            
            my_frame = Frame(pop)
            my_frame.pack()

            pop_label0 = Label(pop, text="Test Results", fg="black", font=("Times", 22,"bold underline"))
            pop_label0.place(x =90, y = 30)
            
            
            pop_label1 = Label(pop, text=result, fg="black", font=("helvetica", 16))
            pop_label1.place(x = 102 , y = 100)
            
            pop_label2 = Label(pop, text=correct, fg="black", font=("helvetica", 16))
            pop_label2.place(x = 47 , y= 150)
            
            pop_label3 = Label(pop, text=wrong, fg="black", font=("helvetica", 16))
            pop_label3.place(x = 47 , y=200)

            no = Button(pop, height = 1 , width = 7 ,text="Exit", command=root.destroy, \
                        bg="black",fg = "white",borderwidth = 5)
            no.place(x = 130 , y = 270)
            
    quiz=Quiz()
    root.mainloop()



#____main____

root1 = Tk()

root1.title('Thought Rattle')

root1.wm_iconbitmap('E:/Python/Python_files/1.My_Project/Reference_Proj/Resources&Samples/icon.ico')

root1.geometry('600x400')                   #----------------------------->>>>>>>Window Sizing
root1.resizable(0,0)
root1.eval('tk::PlaceWindow . center')                     #------------------------>>>>>Placing tkinter window near center


f1st = PhotoImage(file = 'E:/Python/Python_files/1.My_Project/Reference_Proj/Resources&Samples/NBack.png') #------------>>>>Attaching BG

c = Canvas(root1)                               #--------------------->>>>Canvas Object 
c.create_image(0,0,image = f1st,anchor = NW)
c.create_text(300,100,text = 'Welcome To ',font = ('Times',22,'bold underline'),\
                   fill = 'deep pink',activefill = 'white')                                      #----------------------->>>>>Writing Text On Canvas Object
c.create_text(297,140,text = 'Thought Rattle!!!!',font = ('Times',22,'bold underline'),\
                   fill = 'deep pink',activefill = 'white')
c.create_text(288,205,text = 'Instructions',font = ('Times',22,'bold underline'),\
                   fill = 'yellow')                                      
c.create_text(280,260,text = 'This Game consists of 15 questions with \n time limit of 15 min(900s).',font = ('Times',20),\
                   fill = 'yellow')

c.pack(fill = 'both',expand = True)


fnt = font.Font(family='Lucida Handwriting', size=17,weight = 'bold')     #----------------------->>>>>>Font Adjustment for Button

f1but = PhotoImage(file = 'E:/Python/Python_files/1.My_Project/Reference_Proj/\
Resources&Samples/image2.png')                                            #--------->>>Image for Button
bt = Button(root1,command =main,height = 60,\
width = 295,image = f1but,\
borderwidth = 2,cursor = 'hand2')   #---------------->>>>>Button Customisation

bt.place(x = 160, y = 330)         #---------------->>>>>Button Placement

root1.mainloop()  









