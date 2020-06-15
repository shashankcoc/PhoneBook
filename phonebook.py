import phone
import sqlite3
from Tkinter import *
from tkMessageBox import *
con=sqlite3.Connection('Emp1')
cur=con.cursor()
cur.execute("create table if not exists emp111(cid INTEGER PRIMARY KEY AUTOINCREMENT,f_name varchar(25),m_name varchar(25),l_name varchar(25),comp_name varchar(25),address varchar(25),city varchar(25),pincode number,website_url varchar(25),dob date,phonetype number(10),phno number(10),emailtype number(25),email varchar(20))")
root=Tk()
root.title('Phone Book')
a=PhotoImage(file="phone.gif")
lbl=Label(root,image=a).grid(row=4,column=4)
Label(root,text='PhoneBook',font=("verdana 14"),bg='white',fg='orange').grid(row=5,column=4)
Label(root,text='First Name').grid(row=6,column=3)
e1=Entry(root)
e1.grid(row=6,column=4)
Label(root,text='Middle Name').grid(row=7,column=3)
e2=Entry(root)
e2.grid(row=7,column=4)
Label(root,text='Last Name').grid(row=8,column=3)
e3=Entry(root)
e3.grid(row=8,column=4)
Label(root,text='Company Name').grid(row=9,column=3)
e4=Entry(root)
e4.grid(row=9,column=4)
Label(root,text='Address').grid(row=10,column=3)
e5=Entry(root)
e5.grid(row=10,column=4)
Label(root,text='City').grid(row=11,column=3)
e6=Entry(root)
e6.grid(row=11,column=4)
Label(root,text='Pincode').grid(row=12,column=3)
e7=Entry(root)
e7.grid(row=12,column=4)
Label(root,text='Website URL').grid(row=13,column=3)
e8=Entry(root)
e8.grid(row=13,column=4)
Label(root,text='Date Of birth').grid(row=14,column=3)
e9=Entry(root)
e9.grid(row=14,column=4)
Label(root,text='Select Phone Type :',font=('verdana 12'),fg='blue').grid(row=15,column=3)
v1=IntVar()
v2=IntVar()
r=Radiobutton(root,text='Office',variable=v1,value=1)
r.grid(row=15,column=4)
r1=Radiobutton(root,text='Home',variable=v1,value=2)
r1.grid(row=15,column=5)
r2=Radiobutton(root,text='Mobile',variable=v1,value=3)
r2.grid(row=15,column=7)
Label(root,text='Phone Number').grid(row=16,column=3)
e11=Entry(root)
e11.grid(row=16,column=4)


def phone():
    e11=Entry(root)
    e11.grid(row=17,column=4)
Button(root,text='+',command=phone).grid(row=16,column=5)


Label(root,text='Select Email type :',font=('verdana 12'),fg='blue').grid(row=18,column=3)
r3=Radiobutton(root,text='Office',variable=v2,value=4)
r3.grid(row=18,column=4)
r4=Radiobutton(root,text='Personal',variable=v2,value=5)
r4.grid(row=18,column=5)
Label(root,text='Email-id').grid(row=20,column=3)
e12=Entry(root)
e12.grid(row=20,column=4)
Button(root,text='+').grid(row=20,column=5)

def close():
    x=askyesnocancel('Closing','Really want to close')
    if(x==1):
        root.destroy()
Button(root,text='Close',command=close).grid(row=21,column=5)
def search():
    root1=Tk()
    root1.geometry('550x550')
    root1.title('Search')
    Label(root1,text='Searching Phone Book',font=('verdana 14'))
    Label(root1,text='Enter name').grid(row=1,column=2)
    e13=Entry(root1)
    e13.grid(row=1,column=3)
    Label(root1,text="Double Click To Open",fg='orange').grid(row=2,column=2)
    lb=Listbox(root1,font="times 15 bold")
    lb.grid(row=2,column=3,ipadx=100,ipady=100)
    def find(e=1):
        lb.delete(0,END)
        p=e13.get()
        cur.execute("select cid,f_name,l_name from emp111 where (f_name like (?)) or (f_name like (?)) or (f_name like (?))",(p+"%","%"+p+"%","%"+p))
        global x
        x=cur.fetchall()
        for i in range(len(x)):
            lb.insert(END,str(x[i][1])+" "+str(x[i][2]))
        

    root1.bind("<Key>",find)

    def write(e=1):
        index=int(lb.curselection()[0])
        name=str(lb.get(ANCHOR))
        fname=str(name.partition(" ")[0])
        global cid
        cid=x[index][0]        
        cur.execute("select * from emp111 where cid=?",(cid,))
        j=cur.fetchall()
        if(int(j[0][10])==0):
            s="None"
        elif(int(j[0][10])==1):
            s="Office"
        elif(int(j[0][10])==2):
            s="Home"
        elif(int(j[0][10])==3):
            s="Mobile"
        if(j[0][12]==0):
            s1="None"
        elif(int(j[0][12])==4):
            s1="Office"
        else:
            s1="Personal"
        lb.delete(0,END)
        lb.insert(END,"First Name:"+str(j[0][1]))
        lb.insert(END,"Middle Name:"+str(j[0][2]))
        lb.insert(END,"Last Name:"+str(j[0][3]))
        lb.insert(END,"Company Name:"+str(j[0][4]))
        lb.insert(END,"Address:"+str(j[0][5]))
        lb.insert(END,"City:"+str(j[0][6]))
        lb.insert(END,"Pincode:"+str(j[0][7]))
        lb.insert(END,"Website Url:"+str(j[0][8]))
        lb.insert(END,"Date of Birth:"+str(j[0][9]))
        lb.insert(END,"Phone type:"+s)
        lb.insert(END,"Phone number:"+str(j[0][11]))
        lb.insert(END,"Email type:"+s1)
        lb.insert(END,"Email:"+str(j[0][13]))
        
        
        def edit():
            
            cur.execute("delete from emp111 where cid=?",(cid,))
            e1.insert(0,str(j[0][1]))
            e2.insert(0,str(j[0][2]))
            e3.insert(0,str(j[0][3]))
            e4.insert(0,str(j[0][4]))
            e5.insert(0,str(j[0][5]))
            e6.insert(0,str(j[0][6]))
            e7.insert(0,str(j[0][7]))
            e8.insert(0,str(j[0][8]))
            e9.insert(0,str(j[0][9]))
            e11.insert(0,str(j[0][11]))
            e12.insert(0,str(j[0][12]))
            root1.destroy()
        def delete():
            cur.execute("delete from emp111 where cid=?",(cid,))
            con.commit()
            y=askyesno('Deleted','Really Want to Delete')
            if(y==1):
                root1.destroy()
        Button(root1,text='Edit',command=edit).grid(row=4,column=3)
        Button(root1,text='Delete',command=delete).grid(row=6,column=3)
        root1.mainloop()
    lb.bind("<Double-Button-1>",write)  
        
Button(root,text='Search',command=search).grid(row=21,column=4)


def insert():
    s="Not Available"
    
    cur.execute("insert into emp111 (f_name,m_name,l_name,comp_name,address,city,pincode,website_url,dob,phonetype,phno,emailtype,email) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),v1.get(),e11.get(),v2.get(),e12.get()))
    cur.execute("select * from emp111")
    k=cur.fetchall()
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)

    x=showinfo('Saved',"Saved")
Button(root,text='Save',command=insert).grid(row=21,column=3)

root.mainloop()
