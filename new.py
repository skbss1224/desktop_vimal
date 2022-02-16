from tkinter import*
from tkinter import font
from pymysql import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(host='localhost',password='',user='root',database='vimal')
cursor=mydb.cursor()

from sqlalchemy import column
vimal=Tk()
vimal.geometry("1080x700")
vimal.title("company")


        
def ins():
    qry = """insert into company2(number,org,comapany) values(%d,'%s','%s')""" % \
        (int(number_text.get()),org_text.get(),name_text.get)
    
    ack = cursor.execute(qry)
    mydb.commit()
    if ack != 0:
        messagebox.showinfo("ack", "inserted")
           
    else:
        messagebox.showinfo("ack", "did not inserted")

company=Label(vimal,text="company",font=('times',20,font.BOLD))
company.grid(row=0,column=0,padx=1,pady=1)
number=Label(vimal,text="number",font=('times',15,font.BOLD))
number.grid(row=1,column=5,padx=1,pady=1)
number_text=Entry(vimal,font=('times',15,font.BOLD))
number_text.grid(row=1,column=7,padx=1,pady=1)
org=Label(vimal,text="org",font=('times',15,font.BOLD))
org.grid(row=2,column=5,padx=1,pady=1)
org_text=Entry(vimal,font=('times',15,font.BOLD))
org_text.grid(row=2,column=7,padx=1,pady=1)
company_name=Label(vimal,text="name",font=('times',15,font.BOLD))
company_name.grid(row=3,column=5,padx=1,pady=1)
name_text=Entry(vimal,font=('times',15,font.BOLD),bg="green")
name_text.grid(row=3,column=7,padx=1,pady=1)
addbu=Button(vimal,text="submit",command=ins,bg="green")
addbu.grid(row=4,column=2)
    

vimal.mainloop()