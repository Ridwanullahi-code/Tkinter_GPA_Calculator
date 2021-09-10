from tkinter import*
#<-------------- create window  ----------->
root = Tk()
root.geometry("900x600")
root.resizable(width=NO,height=NO)

#<----------------- function to display student information when enter button clicked ----------->
def Enter_button_click():
	dis_name = Label(sub_frame5,text= (name_entry.get()).upper(),fg="black", bg ="white",font ="serief 9 bold")
	dis_name.place(x=60,y=60)
	dept_name = Label(sub_frame5,text= (matric_entry.get()).upper(),fg="black", bg ="white",font ="serief 9 bold")
	dept_name.place(x=90,y=100)
	dis_level = Label(sub_frame5,text= (level_entry.get()).upper()+"L",fg="black", bg ="white",font ="Roboto 9 bold")
	dis_level.place(x=60,y=140)

#<----------------- function to display total grade point when total button clicked ----------->
def total_gradePoint():
	list1 = [int(c1.get()),int(c2.get()),int(c3.get()),int(c4.get()),
	int(c5.get()),int(c6.get()),int(c7.get()),int(c8.get()),int(c9.get())
	,int(c10.get()),int(c11.get())]
	total_grade_entry.insert(0,sum(list1))

#<----------------- function to display student information when total button clicked ----------->
def total_units():
	global list2
	list2 = [int(u1.get()),int(u2.get()),int(u3.get()),int(u4.get()),
	int(u5.get()),int(u6.get()),int(u7.get()),int(u8.get()),int(u9.get())
	,int(u10.get()),int(u11.get())]
	total_unit_entry.insert(0,sum(list2))

#<----------------- function to display student information on screen when total button clicked ----------->
def display():
	list3 = [int(c1.get())*int(u1.get()),int(c2.get())*int(u2.get()),int(c3.get())*int(u3.get()),
		int(c4.get())*int(u4.get()),int(c5.get())*int(u5.get()),int(c6.get())*int(u6.get()),
		int(c7.get())*int(u7.get()),int(c8.get())*int(u8.get()),int(c9.get())*int(u9.get()),
		int(c10.get())*int(u10.get()),int(c11.get())*int(u11.get())]

	result = round(sum(list3)/sum(list2),2)
	dis_gp = Label(sub_frame5,text=str(result),fg="black", bg ="white",font ="Roboto 9 bold")
	dis_gp.place(x=58,y=180)

#<----------------- function to handle all the calculation annd display when total button clicked ----------->
def total_cal():
	total_gradePoint()
	total_units()
	display()

#<----------------- label widget for project title  ----------->
project_name = Label(root,text= "GPA / CGPA CALCULATOR",bd=4,fg="white",bg="#003151",font="Roboto 17 bold",relief=GROOVE).place(x=0,y=0,width=959,height=40)
#<------------------ frame widget to hold other widget or parent widget ---------->
main_frame = Frame(root)
main_frame.place(x=0,y=41,width=899,height=600)

#<--------------- another frame inside main frame or children frame ------------> 
student_info = Frame(main_frame,bg="#003151",bd=6,relief=GROOVE)
student_info.place(x=0,y=1,width=899,height=60)

#<--------------- label and entry widgets for student details ------------------>
name_label = Label(student_info,text="Student Name",fg="white", bg ="#003151",font="Serif 10 bold")
name_label.place(x=0,y=13)
name_entry = Entry(student_info,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
name_entry.place(x=100,y=13)
matric_labe = Label(student_info,text="Matric No",fg="white", bg ="#003151",font="Serif 10 bold")
matric_labe.place(x=289,y=13)
matric_entry = Entry(student_info,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
matric_entry.place(x=370,y=13)
level_labe = Label(student_info,text="Level",fg="white", bg ="#003151",font="Serif 10 bold")
level_labe.place(x=549,y=13)
level_entry = Entry(student_info,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
level_entry.place(x=600,y=13)

#<---------------------  enter button to display student information ------------------>
enter_button = Button(student_info,text="Enter",padx=12,pady=2,relief=GROOVE,bd=3,
			bg="#003151",fg="white",font="Roboto 10 bold",command = Enter_button_click)
enter_button.place(x=800,y=8)

#<--------------- specify grade point area ----------------->
grade_area = Label(root,text="Grade Point",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
grade_area.place(x=4,y=90)

#<----------------- another childreen frame ----------->
sub_frame2 = Frame(main_frame,bg="#003151",bd=6,relief=GROOVE)
sub_frame2.place(x=0,y=63,width=300,height=420)

#<----------------- label widget for course units  ----------->
for course in range(1,12):
	label = Label(sub_frame2,text="Course"+str(course),fg="white", bg ="#003151",font="Serif 13 bold")
	label.grid(row=course-1,column=0,padx=18,pady=6)

#<----------------- entry widget for course unit  ----------->
c1 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c1.place(x=130,y=5)
c2 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c2.place(x=130,y=45)
c3 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c3.place(x=130,y=80)
c4 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c4.place(x=130,y=115)
c5 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c5.place(x=130,y=151)
c6 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c6.place(x=130,y=190)
c7 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c7.place(x=130,y=225)
c8 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c8.place(x=130,y=261)
c9 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c9.place(x=130,y=300)
c10 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c10.place(x=130,y=337)
c11 = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
c11.place(x=130,y=375)


#<----------------- childreen frame for unit courses ------------------------------>
sub_frame3 = Frame(main_frame,bg="#003151",bd=6,relief=GROOVE)
sub_frame3.place(x=301,y=63,width=300,height=420)
unit_area = Label(root,text="Unit course",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
unit_area.place(x=301,y=93)

#<----------------- label widget for unit courses  ------------------------------>
for course in range(1,12):
	label = Label(sub_frame3,text="Course Unit",fg="white", bg ="#003151",font="Serif 13 bold")
	label.grid(row=course-1,column=0,padx=18,pady=6)

#<----------------- entry widget for unit courses  ------------------------------>
u1 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u1.place(x=130,y=5)
u2 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u2.place(x=130,y=45)
u3 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u3.place(x=130,y=80)
u4 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u4.place(x=130,y=115)
u5 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u5.place(x=130,y=151)
u6 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u6.place(x=130,y=190)
u7 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u7.place(x=130,y=225)
u8 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u8.place(x=130,y=261)
u9 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u9.place(x=130,y=300)
u10 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u10.place(x=130,y=337)
u11 = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=17)
u11.place(x=130,y=375)

#<----------------- childreen frame for total grade point and total unit  ------------------------------>
sub_frame4 = Frame(main_frame,bg="#003151",bd=6,relief=GROOVE)
sub_frame4.place(x=0,y=484,width=899,height=76)

#<----------------------- label widget for total grade point and total unit course --------------------->
total_grade_point = Label(sub_frame4,text="Total Grade Point",fg="white", bg ="#003151",font="Roboto 10 bold")
total_grade_point.place(x=10,y=5)
total_unit = Label(sub_frame4,text="Total Unit Course",fg="white", bg ="#003151",font="Roboto 10 bold")
total_unit.place(x=10,y=35)
#<----------------------- entry widget for total grade point and total unit course --------------------->
total_grade_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14,justify=CENTER)
total_grade_entry.place(x=140,y=2)
total_unit_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14,justify=CENTER)
total_unit_entry.place(x=140,y=35)
#<----------------------- button widget for total grade point and total unit course --------------------->
cal_button = Button(sub_frame4,text="Calculate",padx=16,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=total_cal)
cal_button.place(x=350,y=15)
exit_button = Button(sub_frame4,text="Exit",padx=15,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=root.quit)
exit_button.place(x=500,y=15)

#<----------------- childreen frame for student information, total grade point and total unit course  ------------------------------>
sub_frame5 = Frame(main_frame,bg="white",bd=6,relief=GROOVE)
#<----------------- label widget  ------------------------------>
sub_frame5.place(x=603,y=63,width=300,height=420)
display_area = Label(sub_frame5,text="Display Area",bg="white",font="Roboto 14 bold",bd=4,relief=GROOVE,width=30)
display_area.pack(side=TOP)
department =Label(sub_frame5,text="NAME : ",font="Serif 10 bold",bg="white")
department.place(x=0,y=60)
matric_no =Label(sub_frame5,text="MATRIC NO : ", font="Serif 10 bold",bg="white")
matric_no.place(x=0,y=100)
level_ =Label(sub_frame5,text="LEVEL : ",font="Serif 10 bold",bg="white")
level_.place(x=0,y=140)
gpa = Label(sub_frame5,text="GPA : ",font="Serif 10 bold",bg="white")
gpa.place(x=0,y=180)
root.mainloop()
