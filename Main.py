#Semester Project By ZAIN ALI
#SP21-BCS-095
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
import tkinter.messagebox as tmsg
import os
import time
import smtplib as s
import pymysql
import mysql.connector as mysql
# from Forgot_Pass import Resig_ter1
from PIL import Image, ImageTk
from time import strptime
from datetime import datetime
class Login_page:
    def __init__(self,root):
        self.root=root 
        self.root.title("Hotel Mangement System")
        self.root.geometry('1550x800+0+0')
        self.bg = PhotoImage(file="3.png")
        lbl_1 = Label(self.root, image=self.bg)
        lbl_1.place(x=0, y=0)

        # =======================Login Button============================#

        # ==========================Frame==============================#
        frame = Frame(root, bg="black")
        frame.place(x=550, y=170, width=300, height=380)

        self.txtuser1 =ttk.Entry(root, font=("Arial", 12))
        self.txtuser1.place(x=615, y=300)
        self.txtpass1 = ttk.Entry(root, font=("Arial", 12,),show="*")
        self.txtpass1.place(x=615, y=360)
        # ========================Login====================================#
        log = Button(root, text="Login", command=self.login, font=("Montserrat SemiBold", 12, "bold"), bg="#F47F16",
                     fg="black", cursor="hand2", borderwidth=0,width=10, activebackground="#F47F16")
        log.place(x=642, y=405)
        # ===========================Get Started=====================================#
        Get_started = Label(root, text="Get Started", font=("Montserrat SemiBold", 15, "bold"), fg="white",
                            bg="black").place(x=645, y=230)
        # =============================Lable==========================================#
        User_name = Label(root, text="Username", font=("Montserrat light", 12, "bold"), fg="white", bg="black").place(
            x=615, y=272)
        Pass_word = Label(root, text="Password", font=("Montserrat light", 12, "bold"), fg="white", bg="black").place(
            x=615, y=330)
        # ===========================Forgot Password & Signup ============================
        New_Reg = Button(root, text="NEW REGISTRATION",command=self.regster_window,font=("Montserrat light", 8,), fg="white", bg="black", borderwidth=0,cursor="hand2",activebackground="black").place(x=582, y=467)

        For_got = Button(root, text="RESET PASSWORD?",command=self.for_gotten, font=("Montserrat light", 8,), fg="white", bg="black",activebackground="black",
                         borderwidth=0, cursor="hand2").place(x=585, y=485)
    #============================================Forgot  ====================================================#
    def for_gotten(self):
        if self.txtuser1.get()=="":
            messagebox.showerror("Error","Username is required to reset your password",parent=self.root)
        else:
            con= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
            my_cur=con.cursor()
            #print(self.txtpass1)
            my_cur.execute("select * from new_table where username=%s",self.txtuser1.get())  
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username")
            else:
                self.root2=Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('680x500+400+150')
                self.root2.focus_force()
                self.root2.grab_set()
                #====================================Gradient background====================================#
                j=0
                r=10
                for i in range(100):
                    c=str(333333+r)
                    Frame(self.root2,width=10,height=500,bg="black").place(x=j,y=0)   
                    j=j+10                                                  
                    r=r+1

                Frame(self.root2,width=500,height=400,bg='white').place(x=90,y=50)
                l1=Label(self.root2,text='Username',bg='white')
                l2=Label(self.root2,text='Forgot Password',bg='white')
                l=('Consolas',13)
                l1.config(font=l)
                l2.config(font=l)
                l1.place(x=250,y=200)
                l2.place(x=275,y=100)
                l3=Label(self.root2,text='New Password',bg='white')
                l=('Consolas',13)
                l3.config(font=l)
                l3.place(x=250,y=280)
                #======================Line===========================
                Frame(self.root2,width=180,height=2,bg='#141414').place(x=250,y=332)
                Frame(self.root2,width=180,height=2,bg='#141414').place(x=250,y=252)
                #=====================================Entry ============================================
                self.e1=Entry(self.root2,width=20,border=0)
                l=('Consolas',13)
                self.e1.config(font=l)
                self.e1.place(x=250,y=230)
                self.e2=Entry(self.root2,width=20,border=0,show='*')
                self.e2.config(font=l)
                self.e2.place(x=250,y=310)
            
                def bttn(x,y,text,ecolor,lcolor):
                    def on_entera(e):
                        myButton1['background'] = ecolor #ffcc66
                        myButton1['foreground']= lcolor  #000d33

                    def on_leavea(e):
                        myButton1['background'] = lcolor
                        myButton1['foreground']= ecolor
                    myButton1 = Button(self.root2,text=text,
                            width=20,
                            height=2,
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.for_got1,
                            cursor="hand2")        
                    myButton1.bind("<Enter>", on_entera)
                    myButton1.bind("<Leave>", on_leavea)
                    myButton1.place(x=x,y=y)
                bttn(270,375,'RESET PASSWORD','white','#994422')
                self.root2.mainloop()
    
    def for_got1(self):
        if self.e1.get()=="" and self.e2.get()=="":
            messagebox.showerror("Error","Please don't leave any field blank. All fields sre required!!!",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur1 = con.cursor()
                cur1.execute("select * from new_table where username=%s",self.e1.get())
                row2=cur1.fetchone()
                if row2==None:
                    messagebox.showerror("Error","Please Enter a valid username",parent=self.root2)
                else:
                    cur1.execute("update new_table set password=%s where username=%s",(self.e2.get(),self.e1.get())) 
                    messagebox.showinfo("success", "Password updated Successfully", parent=self.root2)
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root2)
        con.commit()
        con.close()

        # self.root4=Toplevel()
        # self.root4.title('WELCOME TO HOTEL MANGEMENT SYSTEM')
        # self.root4.geometry("1550x800+0+0")
#===============================================Register Window=====================================#
    def regster_window(self):         
        global render,img,load
        self.root3=Toplevel()
        self.root3.title("New Registration")
        self.root3.geometry('1550x800+0+0')
        load=Image.open("67.png")
        self.render=ImageTk.PhotoImage(load)
        img=Label(self.root3,image=self.render)
        img.place(x=0,y=0)
        #==============================frame==================================
        frame = Frame(self.root3, bg="black")
        frame.place(x=400, y=140, width=620, height=450)
        # global y
        # y=random.randint(1,100)
        # self.txtran1.set(str(y))

        # ===========================Varibales============================#

        Get_started = Label(self.root3, text="NEW REGISTRATION", font=("Montserrat SemiBold", 16, "bold"), fg="white",
                            bg="black", borderwidth=0).place(x=605, y=190)

        self.txtran = Entry(self.root3, text=2, font=("Arial", 12,), bg="white")

        self.txtran.place(x=632, y=444)
        self.txtname = Entry(self.root3, font=("Arial", 12,), bg="white")
        self.txtname.place(x=630, y=250)
        self.txtuser = Entry(self.root3, font=("Arial", 12,), bg="white")
        self.txtuser.place(x=630, y=300)
        self.txtpass = Entry(self.root3,show="*", font=("Arial", 12,), bg="white")
        self.txtpass.place(x=630, y=350)
        self.txtconf = Entry(self.root3,show="*",font=("Arial", 12,), bg="white")
        self.txtconf.place(x=630, y=400)

        Name = Label(self.root3, text="Name:", font=("Montserrat", 12), fg="white", bg="black").place(x=565,
                                                                                                                  y=250)
        User_name = Label(self.root3, text="Username:", font=("Montserrat", 12), fg="white",
                          bg="black").place(x=535, y=300)
        Password = Label(self.root3, text="Password:", font=("Montserrat", 12), fg="white",
                         bg="black").place(x=535, y=350)
        Confrim_Password = Label(self.root3, text="Confirm Password:", font=("Montserrat", 12), fg="white",
                                 bg="black").place(x=470, y=400)
        Name = Label(self.root3, text="ID Number:", font=("Montserrat", 12), fg="white", bg="black").place(
            x=525, y=440)

        log = Button(self.root3, text="Register", command=self.Reg, font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,
                     fg="black", cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black")
        log.place(x=655, y=492,width=135)
        
        #self.root.mainloop()

        #=================================Register Function=====================================================#

    def Reg(self):
        if self.txtname.get() == "" or self.txtuser.get() == "" or self.txtpass == "":
            messagebox.showerror("Error", "All Fields are required to fill",parent=self.root3)
        elif self.txtpass.get() != self.txtconf.get():
            messagebox.showerror("Error", "Password must be same.Your password is not matched!!!",parent=self.root3)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur = con.cursor()
                cur.execute("insert into new_table(Sr,name,username,password)values(%s,%s,%s,%s)",
                            (self.txtran.get(),
                             self.txtname.get(),
                             self.txtuser.get(),
                             self.txtpass.get()))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Register Successfull", parent=self.root3)
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root3)
    
    # def logout(self):
    #     self.root4.destroy
  #=============================================LOGIN FUNCTION======================================# 

    def login(self):
        if self.txtuser1.get() == "" or self.txtpass1.get() == "":
            messagebox.showerror("Error", "Please enter a correct Login Id")
        elif self.txtuser1.get() == "zain" and self.txtpass1.get() == "*":
            messagebox.showinfo("Sucess", "Only Admin has premession to access this page")
        else:
            con= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
            my_cur=con.cursor()
            #print(self.txtpass1)
            my_cur.execute("select * from new_table where username=%s and password=%s",(
                                                                        self.txtuser1.get(),
                                                                        self.txtpass1.get()))
            
            row=my_cur.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                open=messagebox.askyesno("Yes or No","This page is only accessbale by the Admin.Are you sure want to access this page?")
                if open>0:
                    messagebox.showinfo("Information", "You are directing towards our main Page ")

                    self.root4=Toplevel()
                    self.root4.title('WELCOME TO HOTEL MANGEMENT SYSTEM')
                    self.root4.geometry("1550x800+0+0")
                    global load,img
                    load=Image.open("25.png")
                    load=load.resize((1350,720),Image.ANTIALIAS)
                    self.render=ImageTk.PhotoImage(load)
                    img=Label(self.root4,image=self.render)
                    img.place(x=0,y=0)
                    self.logout_1=Button(self.root4,text="LOG OUT",command=self.logout,font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=1225,y=43)
                    self.custmor=Button(self.root4,text="CUSTOMERS",command=self.coust_win,font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=350,y=100)
                    self.booking=Button(self.root4,text="BOOKING",command=self.booking_win,font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=520,y=100)
                    # self.room=Button(self.root4,text="CUSTOMER BILLING DASHBOARD",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)
                    self.contact=Button(self.root4,text="REPORT AN ISSUE",command=self.reprt_issue,font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=830,y=100)
                    self.payment=Button(self.root4,text="FOOD ITEMS",command=self.details,font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)
                else:
                    messagebox.showinfo("Error","you have no premission to access this page. Thank you for visitng our page!")
                con.commit()
                con.close()
    def coust_win(self):
        self.root5=Toplevel()
        self.root5.title("CUSTOMER Dashboard")
        self.root5.geometry('1550x800+0+0')
        self.root5.configure(bg="#39065D")
        # self.bg = PhotoImage(file="77.png")
        # lbl_2= Label(self.root5, image=self.bg)
        # lbl_2.place(x=0, y=0)  
    
        self.txtid=StringVar()
        x=random.randint(1,100)
        self.txtid.set(str(x))


        self.txtname=StringVar()
        self.txtgender=StringVar()
        self.txtphone=StringVar()
        self.txtnationality=StringVar()
        self.txtemail=StringVar()

        
#====================================================== Frame ======================================================#        
        self.frame=Frame(self.root5,bg="white")
        self.frame.place(x=550,y=200,width=750,height=360)
        self.scroll_x=Scrollbar(self.frame,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(self.frame,orient=VERTICAL)
        self.details_1=ttk.Treeview(self.frame,column=("ref","zan","ali","pak","zun","mas"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.details_1.xview)
        self.scroll_y.config(command=self.details_1.yview)

        self.details_1.heading("ref",text="CUSTOMER ID")
        self.details_1.heading("zan",text="NAME")
        self.details_1.heading("ali",text="MOBILE NO.")
        self.details_1.heading("pak",text="GENDER")
        self.details_1.heading("zun",text="EMAIL")
        self.details_1.heading("mas",text="NATIONALITY")
        self.details_1["show"]="headings"
        self.details_1.pack(fill=BOTH,expand=1)
        self.fetch_data2()


        self.txtid =ttk.Entry(self.root5, font=("Arial", 12))
        self.txtid.place(x=250, y=180)
        self.txtname =ttk.Entry(self.root5, font=("Arial", 12))
        self.txtname.place(x=250, y=230)
        self.txtphone =ttk.Entry(self.root5, font=("Arial", 12))
        self.txtphone.place(x=250, y=280)
        self.search_txt=StringVar()
        self.txtsearch =ttk.Entry(self.root5,textvariable=self.search_txt,font=("Arial", 9))
        self.txtsearch.place(x=820, y=160)
        self.txtgender =ttk.Combobox(self.root5, font=("Arial", 12),width=18,state='readonly')
        self.txtgender['value']=("Male","Female")
        self.txtgender.current(0)
        self.txtgender.place(x=250, y=330)
        self.search_var=StringVar()
        self.search =ttk.Combobox(self.root5,textvariable=self.search_var, font=("Arial", 9),width=18,state='readonly')
        self.search['value']=("MOBILE")
        self.search.current(0)
        self.search.place(x=650, y=160)
        self.txtemail=ttk.Entry(self.root5, font=("Arial", 12))
        self.txtemail.place(x=250, y=380)
        self.txtnationality =ttk.Combobox(self.root5, font=("Arial", 12),width=18,state="readonly")
        self.txtnationality["value"]=("Pakistani","Indian","US","Others")
        self.txtnationality.current(0)
        self.txtnationality.place(x=250, y=430)
        self.details=Label(self.root5,text="CUSTOMER DETAILS:",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=100,y=130)
        self.id=Label(self.root5,text="CUSTOMER ID",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=120,y=180)
        self.custmor=Label(self.root5,text="NAME",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=180,y=230)
        self.room=Label(self.root5,text="MOBILE NO",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=130,y=280)
        self.gender=Label(self.root5,text="GENDER",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=155,y=330)
        self.email=Label(self.root5,text="EMAIL",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=165,y=380)
        self.national=Label(self.root5,text="NATIONALITY",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=110,y=430)
        self.dashboard=Label(self.root5,text="CUSTOMER DASHBOARD",font=('Consolas',28,"bold"),bg="#39065D",border=0,fg="white",activebackground="#39065D",activeforeground="#39065D").place(x=535,y=50)
        self.save =Button(self.root5, text="ADD",command=self.add_data2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=500,width=100)
        self.search =Button(self.root5, text="SEARCH",command=self.search_my2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=155,width=80)
        self.delete =Button(self.root5, text="DELETE",command=self.del_1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=500,width=100)
        self.showall =Button(self.root5, text="REFRESH LIST",command=self.fetch_data2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=155,width=115)
    def add_data2(self):
        if  self.txtname.get()=="" or self.txtid.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root5)
        else:
            try:
                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                my_cur=con_1.cursor()
                # print("yes")
                my_cur.execute("insert into custmors_1(custmor_id,name,mobile,gender,email,nationality)values(%s,%s,%s,%s,%s,%s)",(self.txtid.get(),
                                                                                                                    self.txtname.get(),
                                                                                                                    self.txtphone.get(),
                                                                                                                    self.txtgender.get(),
                                                                                                                    self.txtemail.get(),
                                                                                                                    self.txtnationality.get()))
                
                con_1.commit()
                self.fetch_data2()
                con_1.close()
                messagebox.showinfo("Success","CUSTOMER is Addded!!",parent=self.root5)
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root5)
    def fetch_data2(self):
        con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
        my_cur=con_1.cursor()
        my_cur.execute("select * from custmors_1")
        row_2=my_cur.fetchall()
        if len(row_2)!=0:
            self.details_1.delete(*self.details_1.get_children())
            for i in row_2:
                self.details_1.insert("",END,values=i)
            con_1.commit()
        con_1.close()

    def del_1(self):
        del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!",parent=self.root5)
        if del_my>0:
            con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
            cur_1=con_1.cursor()
            query="delete from custmors_1 where custmor_id=%s"
            value=(self.txtid.get(),)
            cur_1.execute(query,value)
        else:
            if not del_my:
                return
        con_1.commit()
        self.fetch_data2()
        con_1.close()
   
    def search_my2(self):
        con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
        cur_1=con_1.cursor()

        cur_1.execute("select * from custmors_1 where "+str(self.search_var.get())+ " LIKE '%" +str(self.search_txt.get())+"%'")
        row_2=cur_1.fetchall()
        if len(row_2)!=0:
            self.details_1.delete(*self.details_1.get_children())
            for i in row_2:
                self.details_1.insert("",END,values=i)
            con_1.commit()
        con_1.close()

    def logout(self):
        y=messagebox.askyesno("Sure","Are you Sure want to Logout",parent=self.root4)
        if y>0:
            messagebox.showinfo("Thank you","Thank you for using this application",parent=self.root4)
            self.root4.destroy()
        else:
            pass
#===========================================================Booking +===========================================
    def booking_win(self):
        self.root6=Toplevel()
        self.root6.title("Hotel Mangement System")
        self.root6.geometry('1550x800+0+0')
        self.root6.configure(bg="#39065D")
        # load=Image.open("77.png")
        # load=load.resize((1400,750),Image.ANTIALIAS)
        # self.render=ImageTk.PhotoImage(load)
        # img=Label(self.root6,image=self.render)
        # img.place(x=0,y=0)  
        # load_1=Image.open("254.png")
        # load_1=load_1.resize((255,220),Image.ANTIALIAS)
        # self.render=ImageTk.PhotoImage(load_1)
        # img1=Label(self.root6,image=self.render)
        # img1.place(x=225,y=0)  
        # def logout(self):
        #     self.root6.destory
        # x=random.randint(1,100)
        # self.cust_id.set(str(x))
            

        self.cust_id=StringVar()
        # x=random.randint(1,100)
        # self.cust_id.set(str(x))
        self.check_in=StringVar()
        self.check_out=StringVar()
        self.room_type=StringVar()
        self.room_no=StringVar()
        self.meal=StringVar()
        self.nofdays=StringVar()
        self.tax=StringVar()
        self.contact=StringVar()
        x=random.randint(1,100)
        self.cust_id.set(str(x))
        self.bill=StringVar()

        
#====================================================== Frame ======================================================#        
        self.frame=Frame(self.root6,bg="white")
        self.frame.place(x=550,y=350,width=750,height=300)
        self.scroll_x=Scrollbar(self.frame,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(self.frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(self.frame,column=("ref","zan","ali","pak","zun","mas","vii","hiv"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.room_table.xview)
        self.scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("ref",text="CUSTOMER ID")
        self.room_table.heading("zan",text="CHECK IN")
        self.room_table.heading("ali",text="CHECK OUT")
        self.room_table.heading("pak",text="ROOM TYPE")
        self.room_table.heading("zun",text="ROOM NO.")
        self.room_table.heading("mas",text="MEAL")
        self.room_table.heading("vii",text="NO OF DAYS")
        self.room_table.heading("hiv",text=" MOBILE")
        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch()


        self.txtid =ttk.Entry(self.root6,textvariable=self.contact, font=("Arial", 12))
        self.txtid.place(x=250, y=140)
        self.txtcontct =ttk.Entry(self.root6,textvariable=self.cust_id, font=("Arial",12))
        self.txtcontct.place(x=250, y=185)
        self.txtcheckin=ttk.Entry(self.root6,textvariable=self.check_in, font=("Arial", 12))
        self.txtcheckin.place(x=250, y=230)
        self.txtcheckout=ttk.Entry(self.root6,textvariable=self.check_out, font=("Arial", 12))
        self.txtcheckout.place(x=250, y=280)
        self.txtmeal=ttk.Combobox(self.root6,textvariable=self.meal, state="readonly",font=("Arial", 12),width=18)
        self.txtmeal["value"]=("Breakfast","Lunch","Dinner")
        self.txtmeal.current(0)
        self.txtmeal.place(x=250, y=575)
        self.search_txt=StringVar()
        self.txtsearch =ttk.Entry(self.root6,textvariable=self.search_txt,font=("Arial", 9))
        self.txtsearch.place(x=820, y=305)
        self.room_type =ttk.Combobox(self.root6, font=("Arial", 12),width=18,state='readonly')
        self.room_type['value']=("Luxury","High Luxury")
        self.room_type.current(0)
        self.room_type.place(x=250, y=330)
        self.search_var=StringVar()
        self.search =ttk.Combobox(self.root6,textvariable=self.search_var, font=("Arial", 9),width=18,state='readonly')
        self.search['value']=("cus_id")
        self.search.current(0)
        self.search.place(x=650, y=305)
        self.txtnofdays=ttk.Entry(self.root6, textvariable=self.nofdays,font=("Arial", 12))
        self.txtnofdays.place(x=250, y=380)
        self.txttax=ttk.Entry(self.root6, textvariable=self.tax,font=("Arial", 12))
        self.txttax.place(x=250, y=480)
        self.txttotal=ttk.Entry(self.root6, textvariable=self.bill,font=("Arial", 12))
        self.txttotal.place(x=250, y=530)
        self.txtavailableroom =ttk.Combobox(self.root6,textvariable=self.room_no, font=("Arial", 12),width=18,state="readonly")
        self.txtavailableroom["value"]=("101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120")
        self.txtavailableroom.current(0)
        self.txtavailableroom.place(x=250, y=430)
        self.details=Label(self.root6,text="CUSTOMER NUMBER:",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=90,y=140)
        self.id=Label(self.root6,text="CUSTOMER ID",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=130,y=180)
        self.custmor=Label(self.root6,text="CHECK IN DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=110,y=230)
        self.room=Label(self.root6,text="CHECK OUT DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=105,y=280)
        self.tax1=Label(self.root6,text="PAID TAX",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=150,y=480)
        self.total=Label(self.root6,text="TOTAL AMOUNT",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=120,y=530)
        self.meallbl=Label(self.root6,text="MEAL",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=170,y=575)
        
        self.gender=Label(self.root6,text="ROOM TYPE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=145,y=330)
        self.email=Label(self.root6,text="NO OF DAYS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=135,y=380)
        self.national=Label(self.root6,text="AVAILABLE ROOMS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=92,y=430)
        self.bkdash=Label(self.root6,text="BOOKING DASHBOARD",font=('Consolas',30,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=530,y=50)
        self.save =Button(self.root6, text="ADD",command=self.add_data1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=620,width=100)
        self.search =Button(self.root6, text="SEARCH",command=self.search_my1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=300,width=80)
        self.delete =Button(self.root6, text="DELETE",command=self.del_2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=620,width=100)
        self.bil=Button(self.root6, text="BILL",command=self.days_check,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=95, y=621,width=100)

        self.showall =Button(self.root6, text="REFRESH LIST",command=self.fetch,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=300,width=115)
        self.fetch_data =Button(self.root6, text="FETCH DATA",command=self.fetch_dataa,font=("Consolas", 11, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=450, y=140,width=100)
        self.email=Button(self.root6, text="Email Details",command=self.Emails,font=("Consolas", 10, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="#FFA726",activeforeground='#FFA726').place(x=520, y=305,width=110)
    def add_data1(self):
        if  self.contact.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root6)
        else:
            try:
                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                my_cur=con_1.cursor()
                # print("yes")
                my_cur.execute("insert into room_1(cus_id,check_in,check_out,roomtype,available,meal,noofdays,phone_nu)values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.cust_id.get(),
                                                                                                                    self.check_in.get(),
                                                                                                                    self.check_out.get(),
                                                                                                                    self.room_type.get(),
                                                                                                                    self.room_no.get(),
                                                                                                                    self.meal.get(),
                                                                                                                    self.nofdays.get(),
                                                                                                                    self.contact.get()))
                
                con_1.commit()
                # self.fetch_data3()
                con_1.close()
                messagebox.showinfo("Success","DATA IS INSERTED!!",parent=self.root6)
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root6)
    
    def fetch(self):
        con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
        my_cur=con_1.cursor()
        my_cur.execute("select * from room_1 ")
        row_2=my_cur.fetchall()
        if len(row_2)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row_2:
                self.room_table.insert("",END,values=i)
            con_1.commit()
        con_1.close()

    def del_2(self):
        del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!",parent=self.root6)
        if del_my>0:
            con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
            cur_1=con_1.cursor()
            query="delete from room_1 where cus_id=%s"
            value=(self.cust_id.get(),)
            cur_1.execute(query,value)
            messagebox.showinfo("Success","Entry has been deleted!!",parent=self.root6)
        else:
            if not del_my:
                return
        con_1.commit()
        # self.fetch_data3()
        con_1.close()

    def search_my1(self):
        con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
        cur_1=con_1.cursor()

        cur_1.execute("select * from room_1 where "+str(self.search_var.get())+ " LIKE '%" +str(self.search_txt.get())+"%'")
        row_2=cur_1.fetchall()
        if len(row_2)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row_2:
                self.room_table.insert("",END,values=i)
            con_1.commit()
        con_1.close()
        #============================= fetch data ===============================================
    def fetch_dataa(self):
        if self.contact.get()=="":
            messagebox.showerror("Error","Please Provide a valid Mobile number of the CUSTOMER!",parent=self.root6)
        else:
            con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
            cur_1=con_1.cursor()
            query=("select name from custmors_1 where mobile=%s")
            value=(self.contact.get(),)
            cur_1.execute(query,value)
            row4=cur_1.fetchone()
            # print(row4)

            if row4==None:
                messagebox.showerror("Error","Please Enter a Valid Number",parent=self.root6)
            else:
                con_1.commit()
                con_1.close()
                
                showdataframe=Frame(self.root6,bd=0,bg="#39065D")
                showdataframe.place(x=600,y=150,height=140,width=500)
                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur_1=con_1.cursor()
                query=("select name from custmors_1 where mobile=%s")
                value=(self.contact.get(),)
                cur_1.execute(query,value)
                row4=cur_1.fetchone()
                lbl1=Label(showdataframe,text="NAME:",font=("Consolas,5,bold"),bg="#39065D",fg="white")
                lbl1.place(x=120,y=15)
                lbl2=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,5,bold"))
                lbl2.place(x=190,y=15)

                #========================================= Gender =====================================
                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur_1=con_1.cursor()
                query=("select gender from custmors_1 where mobile=%s")
                value=(self.contact.get(),)
                cur_1.execute(query,value)
                row4=cur_1.fetchone()
                lblgender=Label(showdataframe,text="GENDER :",bg="#39065D",fg="white",font=("Consolas,8"))
                lblgender.place(x=100,y=40)
                lblgender=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,8"))
                lblgender.place(x=190,y=40)

                #======================================= Email ===========================================

                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur_1=con_1.cursor()
                query=("select email from custmors_1 where mobile=%s")
                value=(self.contact.get(),)
                cur_1.execute(query,value)
                row4=cur_1.fetchone()
                lblgender=Label(showdataframe,text="EMAIL :",bg="#39065D",fg="white",font=("Consolas,8"))
                lblgender.place(x=120,y=65)
                lblgender=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,8"))
                lblgender.place(x=190,y=65)

                #=================================== Nationality -==========================================
                con_1= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                cur_1=con_1.cursor()
                query=("select nationality from custmors_1 where mobile=%s")
                value=(self.contact.get(),)
                cur_1.execute(query,value)
                row4=cur_1.fetchone()
                lblnat=Label(showdataframe,text="NATIONALITY :",font=("Consolas,5,bold"),bg="#39065D",fg="white")
                lblnat.place(x=71,y=90)
                lblnat=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,5,bold"))
                lblnat.place(x=190,y=90)

            con_1.commit()
            con_1.close()

    def days_check(self):
        # pass
        # global 
        # x=random.randint(1,100)
        # self.cust_id.set(str(x))
        self.tax.set(5)
        self.bill.set(4)
        inDate=self.check_in.get()
        outdate=self.check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.nofdays.set(abs(outdate-inDate).days)
        
        if (self.meal.get()=="Breakfast" and self.room_type.get()=="Luxury"):
            print(self.meal.get())
            q1=float(5000)
            q2=float(7000)
            q3=float(5)
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.10))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.10)))
            self.tax.set(Tax)
            self.bill.set(TT)
        else:
            pass
    
    def Emails(self):
        ob=s.SMTP("smtp.gmail.com",587)
        ob.starttls()
        a=self.contact.get()
        b=self.cust_id.get()
        c=self.check_in.get()
        d=self.check_out.get()
        e=self.nofdays.get()
        f=self.room_no.get()
        g=self.room_type.get()

        ob.login("rana5542123@gmail.com","--------")
        subject="HOTEL MANGEMENT SYSTEM BY ZAIN ALI"
        body=f'''
        Dear CUSTOMER,
        Thank you for choosing our Hotel!

        You details are mentioned below:
        CUSTOMER NAME : ZAIN ALI
        CONTACT NUMBER: {a}
        CUSTOMER ID   : {b}
        CHECK IN DATE : {c}
        CHECK OUT ID  : {d}
        YOUR TOTAL STAY :{e} Days
        ALLOTTED ROOM : {f}
        ROOM TYPE     : {g}

        We're eagerly looking forward to your arrival at our hotel.
        Be assured of our best services during your stay here.

        Regards,
        Hotel Mangement System
        Designed and Programed by,
        ZAIN ALI

        '''
        message="Subject:{}\n\n{}".format(subject,body)
        ob.sendmail("rana5542123@gmail.com","SP21-BCS-0956329@pern.onmicrosoft.com",message)
        print('Yes')
        ob.quit()

    def details(self):
        menu_category = ["Tea & Coffee","DRINKS","Fast Food","Punjabi dishes","Starters","Main Course","Dessert"]

        menu_category_dict = {"Tea & Coffee":"1 Tea & Coffee.txt","Drinks":"2 Drinks.txt",
                        "Fast Food":"3 Fast Food.txt","Punjabi dishes":"4 Punjabi dishes.txt",
                        "Starters":"5 Starters.txt","Main Course":"6 Main Course.txt",
                        "Sweet Dishes":"7 Sweet Dishes.txt"}

        order_dict = {}
        for i in menu_category:
            order_dict[i] = {}

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        #====================Backend Functions===========================
        def load_menu():
            menuCategory.set("")
            menu_tabel.delete(*menu_tabel.get_children())
            menu_file_list = os.listdir("Menu")
            for file in menu_file_list:
                f = open("Menu\\" + file , "r")
                category=""
                while True:
                    line = f.readline()
                    if(line==""):
                        menu_tabel.insert('',END,values=["","",""])
                        break
                    elif (line=="\n"):
                        continue
                    elif(line[0]=='#'):
                        category = line[1:-1]
                        name = "\t\t"+line[:-1]
                        price = ""
                    elif(line[0]=='*'):
                        name = line[:-1]
                        price = ""
                    else:
                        name = line[:line.rfind(" ")]
                        price = line[line.rfind(" ")+1:-3]
                    
                    menu_tabel.insert('',END,values=[name,price,category])
                #menu_tabel.insert('',END,values=["Masala Dosa","50"])

        def load_order():
            order_tabel.delete(*order_tabel.get_children())
            for category in order_dict.keys():
                if order_dict[category]:
                    for lis in order_dict[category].values():
                        order_tabel.insert('',END,values=lis)
            update_total_price()

        def add_button_operation():
            name = itemName.get()
            rate = itemRate.get()
            category = itemCategory.get()
            quantity = itemQuantity.get()

            if name in order_dict[category].keys():
                tmsg.showinfo("Error", "Item already exist in your order",parent=root7)
                return
            if not quantity.isdigit():
                tmsg.showinfo("Error", "Please Enter Valid Quantity",parent=root7)
                return
            lis = [name,rate,quantity,str(int(rate)*int(quantity)),category]
            order_dict[category][name] = lis
            load_order()
            
        def load_item_from_menu(event):
            cursor_row = menu_tabel.focus()
            contents = menu_tabel.item(cursor_row)
            row = contents["values"]

            itemName.set(row[0])
            itemRate.set(row[1])
            itemCategory.set(row[2])
            itemQuantity.set("1")

        def load_item_from_order(event):
            cursor_row = order_tabel.focus()
            contents = order_tabel.item(cursor_row)
            row = contents["values"]

            itemName.set(row[0])
            itemRate.set(row[1])
            itemQuantity.set(row[2])
            itemCategory.set(row[4])

        def show_button_operation():
            category = menuCategory.get()
            if category not in menu_category:
                tmsg.showinfo("Error", "Please select valid Choice",parent=root7)
            else:
                menu_tabel.delete(*menu_tabel.get_children())
                f = open("Menu\\" + menu_category_dict[category] , "r")
                while True:
                    line = f.readline()
                    if(line==""):
                        break
                    if (line[0]=='#' or line=="\n"):
                        continue
                    if(line[0]=='*'):
                        name = "\t"+line[:-1]
                        menu_tabel.insert('',END,values=[name,"",""])
                    else:
                        name = line[:line.rfind(" ")]
                        price = line[line.rfind(" ")+1:-3]
                        menu_tabel.insert('',END,values=[name,price,category])

        def clear_button_operation():
            itemName.set("")
            itemRate.set("")
            itemQuantity.set("")
            itemCategory.set("")

        def cancel_button_operation():
            names = []
            for i in menu_category:
                names.extend(list(order_dict[i].keys()))
            if len(names)==0:
                tmsg.showinfo("Error", "Your order list is Empty",parent=root7)
                return
            ans = tmsg.askquestion("Cancel Order", "Are You Sure to Cancel Order?",parent=root7)
            if ans=="no":
                return
            order_tabel.delete(*order_tabel.get_children())
            for i in menu_category:
                order_dict[i] = {}
            clear_button_operation()
            update_total_price()

        def update_button_operation():
            name = itemName.get()
            rate = itemRate.get()
            category = itemCategory.get()
            quantity = itemQuantity.get()

            if category=="":
                return
            if name not in order_dict[category].keys():
                tmsg.showinfo("Error", "Item is not in your order list",parent=root7)
                return
            if order_dict[category][name][2]==quantity:
                tmsg.showinfo("Error", "No changes in Quantity",parent=root7)
                return
            order_dict[category][name][2] = quantity
            order_dict[category][name][3] = str(int(rate)*int(quantity))
            load_order()

        def remove_button_operation():
            name = itemName.get()
            category = itemCategory.get()

            if category=="":
                return
            if name not in order_dict[category].keys():
                tmsg.showinfo("Error", "Item is not in your order list",parent=root7)
                return
            del order_dict[category][name]
            load_order()

        def update_total_price():
            price = 0
            for i in menu_category:
                for j in order_dict[i].keys():
                    price += int(order_dict[i][j][3])
            if price == 0:
                totalPrice.set("")
            else:
                totalPrice.set("Rs. "+str(price)+"  /-")

        def bill_button_operation():
            customer_name = customerName.get()
            customer_contact = customerContact.get()
            names = []
            for i in menu_category:
                names.extend(list(order_dict[i].keys()))
            if len(names)==0:
                tmsg.showinfo("Error", "Your order list is Empty",parent=root7)
                return
            if customer_name=="" or customer_contact=="":
                tmsg.showinfo("Error", "Customer Details Required",parent=root7)
                return
            if not customerContact.get().isdigit():
                tmsg.showinfo("Error", "Invalid Customer Contact",parent=root7)
                return   
            ans = tmsg.askquestion("Generate Bill", "Are You Sure to Generate Bill?",parent=root7)
            ans = "yes"
            if ans=="yes":
                bill = Toplevel(root7)
                bill.title("Bill")
                bill.geometry("820x450+300+100")
                bill_text_area = Text(bill, font=("Montserrat", 12))
                st = "\t\t\t HOTEL MANGEMENT SYSTEM\n\t\t\t Designed and Programmed by\n"
                st += "\t\t\t\tMr. ZAIN ALI\n"
                st += "-"*61 + "BILL" + "-"*61 + "\nDate:- "

                #Date and time
                t = time.localtime(time.time())
                week_day_dict = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",
                                    6:"Sunday"}
                st += f"{t.tm_mday} / {t.tm_mon} / {t.tm_year} ({week_day_dict[t.tm_wday]})"
                st += " "*10 + f"\t\t\t\t\t\tTime:- {t.tm_hour} : {t.tm_min} : {t.tm_sec}"

                #Customer Name & Contact
                st += f"\nCustomer Name:- {customer_name}\nCustomer Contact:- {customer_contact}\n"
                st += "-"*130 + "\n" + " "*4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
                st += "-"*130 + "\n"

                #List of Items
                for i in menu_category:
                    for j in order_dict[i].keys():
                        lis = order_dict[i][j]
                        name = lis[0]
                        rate = lis[1]
                        quantity = lis[2]
                        price = lis[3]
                        st += name + "\t\t\t\t\t" + rate + "\t      " + quantity + "\t\t  " + price + "\n\n"
                st += "-"*130

                #Total Price
                st += f"\n\t\t\tTotal price : {totalPrice.get()}\n"
                st += "-"*130

                #display bill in new window
                bill_text_area.insert(1.0, st)

                #write into file
                folder = f"{t.tm_mday},{t.tm_mon},{t.tm_year}"
                if not os.path.exists(f"Bill Records\\{folder}"):
                    os.makedirs(f"Bill Records\\{folder}")
                file = open(f"Bill Records\\{folder}\\{customer_name+customer_contact}.txt", "w")
                file.write(st)
                file.close()

                #Clear operaitons
                order_tabel.delete(*order_tabel.get_children())
                for i in menu_category:
                    order_dict[i] = {}
                clear_button_operation()
                update_total_price()
                customerName.set("")
                customerContact.set("")

                bill_text_area.pack(expand=True, fill=BOTH)
                bill.focus_set()
                bill.protocol("WM_DELETE_WINDOW", close_window)

        def close_window():
            tmsg.showinfo("Thanks", "Thanks for using our service",parent=root7)
        #[name,rate,quantity,str(int(rate)*int(quantity)),category]
        #==================Backend Code Ends===============

        #================Frontend Code Start==============
        root7 = Toplevel()
        w, h = root7.winfo_screenwidth(), root7.winfo_screenheight()
        root7.geometry("%dx%d+0+0" % (w, h))
        root7.title("CUSTOMER BIILING SYSTEM")
        root7.configure(bg="#39065D")
        #root7.attributes('-fullscreen', True)
        #root7.resizable(0, 0)

        #================Title==============
        style_button = ttk.Style()
        style_button.configure("TButton",font = ("Montserrat",10,"bold"),
        background="#39065D")

        title_frame = Frame(root7, bg="#39065D", relief=GROOVE)
        title_frame.pack(side=TOP, fill="x")

        title_label = Label(root7, text="CUSTOMER  BILLING  DASHBOARD", 
                            font=("Montserrat SemiBold", 19, "bold"),bg = "#39065D", fg="white")
        title_label.place(x=455,y=30)

        #==============Customer=============
        customer_frame = LabelFrame(root7,text="Customer Details",font=("Montserrat", 14,),border=0,
                                    bg="#39065D",fg="white")
        customer_frame.place(x=0,y=70 ,width=800,height=100)

        customer_name_label = Label(customer_frame, text="Name", 
                            font=("Montserrat", 14),bg = "#39065D", fg="white")
        customer_name_label.grid(row = 0, column = 0)

        customerName = StringVar()
        customerName.set("")
        customer_name_entry = Entry(customer_frame,width=20,font="Montserrat",
                                        textvariable=customerName)
        customer_name_entry.grid(row = 0, column=1,padx=50)

        customer_contact_label = Label(customer_frame, text="Contact", 
                            font=("Montserra", 15, "bold"),bg = "#39065D", fg="white")
        customer_contact_label.grid(row = 0, column = 2)

        customerContact = StringVar()
        customerContact.set("")
        customer_contact_entry = Entry(customer_frame,width=20,font="Montserrat 12",bd=0,
                                        textvariable=customerContact)
        customer_contact_entry.grid(row = 0, column=3,padx=50)

        #===============Menu===============
        menu_frame = Frame(root7,bd=8, bg="#39065D")
        menu_frame.place(x=0,y=125,height=560,width=680)

        menu_label = Label(menu_frame, text="Available Products", 
                            font=("Montserrat SemiBold", 15, "bold"),bg = "#39065D", fg="white", pady=0)
        menu_label.pack(side=TOP,fill="x")

        menu_category_frame = Frame(menu_frame,bg="#39065D",pady=10)
        menu_category_frame.pack(fill="x")

        combo_lable = Label(menu_category_frame,text="Select Type", 
                            font=("Montserrat", 12, "bold"),bg = "#39065D", fg="white")
        combo_lable.grid(row=0,column=0,padx=10)

        menuCategory = StringVar()
        combo_menu = ttk.Combobox(menu_category_frame,values=menu_category,
                                    textvariable=menuCategory)
        combo_menu.grid(row=0,column=1,padx=30)

        show_button =Button(menu_category_frame, text="Show",font=("Montserrat",9,"bold"),width=10,bg="#FFA726",activebackground="#FFA726",
                                command=show_button_operation)
        show_button.grid(row=0,column=2,padx=60)

        show_all_button =Button(menu_category_frame, text="Show All",font=("Montserrat",9,"bold"),bg="#FFA726",activebackground="#FFA726",
                                width=10,command=load_menu)
        show_all_button.grid(row=0,column=3)

        ############################# Menu Tabel ##########################################
        menu_tabel_frame = Frame(menu_frame)
        menu_tabel_frame.pack(fill=BOTH,expand=1)

        scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
        scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading",font=("Montserrat",10,))
        style.configure("Treeview",font=("Montserrat",8,),rowheight=25)

        menu_tabel = ttk.Treeview(menu_tabel_frame,style = "Treeview",
                    columns =("name","price","category"),xscrollcommand=scrollbar_menu_x.set,
                    yscrollcommand=scrollbar_menu_y.set)

        menu_tabel.heading("name",text="Name")
        menu_tabel.heading("price",text="Price")
        menu_tabel["displaycolumns"]=("name", "price")
        menu_tabel["show"] = "headings"
        menu_tabel.column("price",width=50,anchor='center')

        scrollbar_menu_x.pack(side=BOTTOM,fill=X)
        scrollbar_menu_y.pack(side=RIGHT,fill=Y)

        scrollbar_menu_x.configure(command=menu_tabel.xview)
        scrollbar_menu_y.configure(command=menu_tabel.yview)

        menu_tabel.pack(fill=BOTH,expand=1)


        #menu_tabel.insert('',END,values=["Masala Dosa","50"])
        load_menu()
        menu_tabel.bind("<ButtonRelease-1>",load_item_from_menu)

        ###########################################################################################

        #===============Item Frame=============
        item_frame = Frame(root7, bg="#39065D")
        item_frame.place(x=680,y=125,height=230,width=680)

        item_title_label = Label(item_frame, text="Selected Product", 
                            font=("Montserrat Semibold", 15,),bg = "#39065D", fg="white")
        item_title_label.pack(side=TOP,fill="x")

        item_frame2 = Frame(item_frame, bg="#39065D")
        item_frame2.pack(fill=X)

        item_name_label = Label(item_frame2, text="Name",
                            font=("Montserrat", 12, "bold"),bg = "#39065D", fg="white")
        item_name_label.grid(row=0,column=0)

        itemCategory = StringVar()
        itemCategory.set("")

        itemName = StringVar()
        itemName.set("")
        item_name = Entry(item_frame2, font="arial 12",textvariable=itemName,state=DISABLED, width=25)
        item_name.grid(row=0,column=1,padx=10)

        item_rate_label = Label(item_frame2, text="Price", 
                            font=("arial", 12, "bold"),bg = "#39065D", fg="white")
        item_rate_label.grid(row=0,column=2,padx=40)

        itemRate = StringVar()
        itemRate.set("")
        item_rate = Entry(item_frame2, font="arial 12",textvariable=itemRate,state=DISABLED, width=10)
        item_rate.grid(row=0,column=3,padx=10)

        item_quantity_label = Label(item_frame2, text="Quantity", 
                            font=("Montserrat", 10, "bold"),bg = "#39065D", fg="white")
        item_quantity_label.grid(row=1,column=0,padx=30,pady=15)

        itemQuantity = StringVar()
        itemQuantity.set("")
        item_quantity = Entry(item_frame2, font="arial 12",textvariable=itemQuantity, width=10)
        item_quantity.grid(row=1,column=1)

        item_frame3 = Frame(item_frame, bg="#39065D")
        item_frame3.pack(fill=X)

        add_button =Button(item_frame3, text="Add Item",bg="#FFA726",activebackground="#FFA726"
                                ,command=add_button_operation)
        add_button.grid(row=0,column=0,padx=40,pady=30)

        remove_button =Button(item_frame3, text="Remove Item",bg="#FFA726",activebackground="#FFA726"
                                ,command=remove_button_operation)
        remove_button.grid(row=0,column=1,padx=40,pady=30)

        update_button =Button(item_frame3, text="Update Quantity",bg="#FFA726",activebackground="#FFA726",
                                command=update_button_operation)
        update_button.grid(row=0,column=2,padx=40,pady=30)

        clear_button =Button(item_frame3, text="Clear",bg="#FFA726",activebackground="#FFA726",
                                width=8,command=clear_button_operation)
        clear_button.grid(row=0,column=3,padx=40,pady=30)

        #==============Order Frame=====================
        order_frame = Frame(root7, bg="#39065D")
        order_frame.place(x=680,y=335,height=370,width=680)

        order_title_label = Label(order_frame, text="Your Products", 
                            font=("Montserrat", 15, "bold"),bg = "#39065D", fg="white")
        order_title_label.pack(side=TOP,fill="x")

        ############################## Order Tabel ###################################
        order_tabel_frame = Frame(order_frame)
        order_tabel_frame.place(x=0,y=40,height=260,width=680)

        scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

        order_tabel = ttk.Treeview(order_tabel_frame,
                    columns =("name","rate","quantity","price","category"),xscrollcommand=scrollbar_order_x.set,
                    yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("name",text="Name")
        order_tabel.heading("rate",text="Rate")
        order_tabel.heading("quantity",text="Quantity")
        order_tabel.heading("price",text="Price")
        order_tabel["displaycolumns"]=("name", "rate","quantity","price")
        order_tabel["show"] = "headings"
        order_tabel.column("rate",width=100,anchor='center', stretch=NO)
        order_tabel.column("quantity",width=100,anchor='center', stretch=NO)
        order_tabel.column("price",width=100,anchor='center', stretch=NO)

        order_tabel.bind("<ButtonRelease-1>",load_item_from_order)

        scrollbar_order_x.pack(side=BOTTOM,fill=X)
        scrollbar_order_y.pack(side=RIGHT,fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        order_tabel.pack(fill=BOTH,expand=1)

        # order_tabel.insert('',END,text="HEllo",values=["Masala Dosa","50","2","100"])
        ###########################################################################################

        total_price_label = Label(order_frame, text="Total Price", 
                            font=("Montserrat", 12, "bold"),bg = "#39065D", fg="white")
        total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=10)

        totalPrice = StringVar()
        totalPrice.set("")
        total_price_entry = Entry(order_frame, font="arial 12",textvariable=totalPrice,state=DISABLED, 
                                    width=10)
        total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=10)

        bill_button = Button(order_frame,font=("Montserrat",9,"bold"),text="Bill",width=10,bg="#FFA726",activebackground="#FFA726",
                                command=bill_button_operation)
        bill_button.pack(side=LEFT,anchor=SW,padx=80,pady=10)

        cancel_button =Button(order_frame, text="Cancel Order",font=("Montserrat",9,"bold"),width=12,command=cancel_button_operation,bg="#FFA726",fg="black",activebackground="#FFA726")
        cancel_button.pack(side=LEFT,anchor=SW,padx=20,pady=10)

    def reprt_issue(self):
        self.root8=Toplevel()
        self.root8.title("REPORT AN ISSUE")
        self.root8.geometry('1550x800+0+0')
        self.root8.configure(bg="#39065D")

        self.reort=Label(self.root8,text="REPORT AN ISSUE",font=('Montserrat Semibold',25),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=630,y=80)
        self.reort1=Label(self.root8,text='''
        If you're having trouble after using this application,
        you've come to the right place. Please use this form 
        to tell us about the issue you're experiencing.
        Please provide a detailed description of this issue,including:
        What you were doing when the problem occurred?
        What you expected to happend?
        What actually happened?
        ''',font=('Montserrat',10),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=575,y=120)
        self.reort2=Label(self.root8,text='''
        CONTACT US
        ''',font=('Montserrat',15,"bold"),bg="#39065D",border=0,fg="green",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=220,y=275)
        self.reort2=Label(self.root8,text='''
        Mailing Address:
        rana5542123@gmail.com
        HOTEL MANAGEMENT SYSTEM
        Designed and Programed by
        ZAIN ALI
        +923416778145
        ''',font=('Montserrat',12),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=175,y=330)
        self.txt54=StringVar()
        x=random.randint(1,100)
        self.txt54.set(str(x))
        print(x)

        self.txtreport=Entry(self.root8,textvariable=self.txt54,font=("Arial", 10))
        self.txtfield=Text(self.root8,font="Montserrat")
        self.txtfield.place(x=570,y=280,height=250,width=500)
        report_button =Button(self.root8, text="SUBMIT  REPORT",command=self.add_data5,font=("Montserrat bold",9,"bold"),width=18,bg="#FFA726",fg="black",activebackground="#FFA726",activeforeground="#FFA726",cursor="hand2")
        report_button.place(x=750,y=570)
    def add_data5(self):
        # print(self.txtfield.get("1.0",END))
        if  self.txtfield.get("1.0",END)=="":
            messagebox.showerror("Error","All field are required",parent=self.root8)
        else:
            try:
                con_8= pymysql.connect(host="localhost", user="root", password="zainhub123", database="register")
                my_cur=con_8.cursor()
                # print("yes")
                my_cur.execute("insert into report(ID_NO,Reports)values(%s,%s)",(self.txt54.get(),
                                                                                self.txtfield.get("1.0",END)))

                
                con_8.commit()
                con_8.close()
                messagebox.showinfo("Success",'''
                Thanks for reporting.
                Your Report has been sent your report to our 
                Database Engineer.
                This issue will be resolved shortly.
                Thanks!''',parent=self.root8)
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root8)

       
       
        # self.m1=ImageTk.PhotoImage(file="1.png")
        # self.m1.place(x=200,y=300)
        # load_1=Image.open("254.png")
        # load_1=load_1.resize((255,220),Image.ANTIALIAS)
        # self.render=ImageTk.PhotoImage(load_1)
        # img1=Label(self.root6,image=self.render)
        # img1.place(x=225,y=0)


if __name__ == "__main__":
    root=Tk()
    app=Login_page(root)
    root.mainloop()
