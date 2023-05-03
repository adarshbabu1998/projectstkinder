from tkinter import*
d=Tk()
d.geometry('700x700')
d.resizable(True,True)
d.title(' ')
d.configure(background='grey')

heading1=Label(d,text='STUDENT MARK SHEETS',bg='grey',fg='black',font=('Arial bold',18))
heading1.place(x=0)
heading2=Label(d,text='NAME:',bg='grey',fg='black',)
heading2.place(x=0,y=55)
name_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='black')
name_entry.place(x=40,y=55)


heading3=Label(d,text='ENROLL NO:',bg='grey',fg='black')
heading3.place(x=200,y=55)
enroll_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='black')
enroll_entry.place(x=270,y=55)

sub_heading1=Label(d,text='SUBJECTS',bg='brown',fg='white',font=('arial bold',10),width=30,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading1.place(x=10,y=100)
sub_heading2=Label(d,text='MARKS',bg='brown',fg='white',font=('arial bold',10),width=20,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading2.place(x=200,y=100)
sub_heading3=Label(d,text='GRADE',bg='brown',fg='white',font=('arial bold',10),width=15,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading3.place(x=350,y=100)

subject1=Label(d,text='ENGLISH',bg='GREY',fg='BLACK',font=('arial bold',8))
subject1.place(x=100,y=130)
subjectentry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
subjectentry.place(x=250,y=130,)
subjectgrade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
subjectgrade.place(x=380,y=130)


hindi=Label(d,text='HINDI',bg='GREY',fg='BLACK',font=('arial bold',8))
hindi.place(x=100,y=150)
hindi_ent=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
hindi_ent.place(x=250,y=150)
hind_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
hind_grade.place(x=380,y=150)

science=Label(d,text='SCIENCE',bg='GREY',fg='BLACK',font=('arial bold',8))
science.place(x=100,y=170)
science_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
science_entry.place(x=250,y=170)
science_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
science_grade.place(x=380,y=170)


maths=Label(d,text='MATHS',bg='GREY',fg='BLACK',font=('arial bold',8))
maths.place(x=100,y=190)
math_ent=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
math_ent.place(x=250,y=190)
math_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
math_grade.place(x=380,y=190)






def display():
    studname1=Label(d,text='STUD NAME',bg='GREY',fg='BLACK',font=('arial bold',8))
    studname1.place(x=10,y=260)
    enrollnum1=Label(d,text='ENROLL NO:',bg='GREY',fg='BLACK',font=('arial bold',8))
    enrollnum1.place(x=10,y=280)
    gradecard=Label(d,text='GRADE CARD',bg='GREY',fg='BLACK',font=('arial bold',10))
    gradecard.place(x=10,y=310)
    out=Label(d,text='OUT OF 400',bg='GREY',fg='BLACK',font=('arial bold',10))
    out.place(x=10,y=330)
    uname = Label(d,text=name_entry.get(),bg='grey',fg='black',font=('arial bold',8))
    uenroll=Label(d,text=enroll_entry.get(),bg='grey',fg='black',font=('arial bold',8),)
    uname.place(x=80,y=260,)
    uenroll.place(x=80,y=280)

    sub_heading1next=Label(d,text='SUBJECTS',bg='light blue',fg='red',font=('arial bold',10),width=30,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
    sub_heading1next.place(x=10,y=350)
    sub_heading2next=Label(d,text='MARKS',bg='light blue',fg='red',font=('arial bold',10),width=20,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
    sub_heading2next.place(x=200,y=350)
    sub_heading3next=Label(d,text='GRADE',bg='light blue',fg='red',font=('arial bold',10),width=15,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
    sub_heading3next.place(x=350,y=350)

    subject1next=Label(d,text='ENGLISH',bg='GREY',fg='BLACK',font=('arial bold',8))
    subject1next.place(x=100,y=375)
    subject2next=Label(d,text='HINDI',bg='GREY',fg='BLACK',font=('arial bold',8))
    subject2next.place(x=100,y=395)
    subject3next=Label(d,text='SCIENCE',bg='GREY',fg='BLACK',font=('arial bold',8))
    subject3next.place(x=100,y=415)
    subject4next=Label(d,text='MATHS',bg='GREY',fg='BLACK',font=('arial bold',8))
    subject4next.place(x=100,y=435)

    english = Label(d,text=subjectentry.get(),bg='grey',fg='black',font=('arial bold',8))
    english.place(x=260,y=375)
    hindi= Label(d,text=hindi_ent.get(),bg='grey',fg='black',font=('arial bold',8))
    hindi.place(x=260,y=395)
    science = Label(d,text=science_entry.get(),bg='grey',fg='black',font=('arial bold',8))
    science.place(x=260,y=415)
    maths = Label(d,text=math_ent.get(),bg='grey',fg='black',font=('arial bold',8))
    maths.place(x=260,y=435)

    englishgrade = Label(d,text=subjectgrade.get(),bg='grey',fg='black',font=('arial bold',8))
    englishgrade.place(x=380,y=375)
    hindigrade= Label(d,text=hind_grade.get(),bg='grey',fg='black',font=('arial bold',8))
    hindigrade.place(x=380,y=395)
    sciencegrade = Label(d,text=science_grade.get(),bg='grey',fg='black',font=('arial bold',8))
    sciencegrade.place(x=380,y=415)
    mathsgrade = Label(d,text=math_grade.get(),bg='grey',fg='black',font=('arial bold',8))
    mathsgrade.place(x=380,y=435)

    total=Label(d,text='TOTAL SCORE',bg='GREY',fg='BLACK',font=('arial bold',8))
    total.place(x=10,y=600)
    tgrade=Label(d,text='TOTAL GRADE',bg='GREY',fg='BLACK',font=('arial bold',8))
    tgrade.place(x=10,y=630)

   
    sum= int(subjectentry.get())+ int(hindi_ent.get())+int(science_entry.get())+int(math_ent.get())
    marks = Label(d,text=sum,bg='grey',fg='black',font=('arial bold',8))
    marks.place(x=120,y=600)
    grade=int(subjectgrade.get())+int(hind_grade.get())+int(science_grade.get())+int(math_grade.get()) *0.4
    grade = Label(d,text=grade,bg='grey',fg='black',font=('arial bold',8))
    grade.place(x=120,y=630)
    
b = Button(d,text='SUBMIT',bg='blue',command=display,fg='white') 
b.place(x=430,y=470)

d.mainloop()