from Tkinter import *
root=Tk()
root.geometry('850x850')
Label(root,text='Project Title:PhoneBook',font=('verdana 24'),fg='black').grid(row=1,column=1)
Label(root,text='Project of Python & DataBase',font=('verdana 20')).grid(row=3,column=1)
Label(root,text='Developed By : Shashank Srivastava',font=('verdana 20'),fg='orange').grid(row=4,column=1)
Label(root,text='---------------------------------------------------------------------------------------------',).grid(row=5,column=1)
Label(root,text='Make mouse movement to clear the screen',fg='red').grid(row=6,column=1)


def close(e=1):
    root.destroy()
root.bind('<Motion>',close)


root.mainloop()
