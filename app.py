import tkinter as tk
from tkinter import* 

def click(event):
    global value
    text=event.widget.cget("text")
    if text == "=":
        try:
            val1 = eval(value.get())
            value.set(val1)
        except Exception as e:
            value.set("Error")
        input.update()
    elif text =="C":
        value.set('')

    elif text=="Del":
         value.set(value.get()[:-1])
    else:
        value.set(value.get() + text)
        input.update()
        

root=Tk()
#root.geometry('500x600')
root.minsize(500,600)
root.maxsize(500,600)
root.title('Calculator')
root.config(bg="white")






'''Main Button Frame'''

main_frame=tk.Frame(root,width=500,height=450)
main_frame.pack(side=BOTTOM,anchor='sw')

'''Left Panel'''

left_frame= tk.Frame(main_frame,width=300,height=400)
left_frame.grid(row=1,column=0)



'''First Button Line'''

f=tk.Frame(left_frame,width=300,height=100,bd=0)
b=Button(f,text="7",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="8",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="9",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

f.pack()



'''Second Button Line'''

f=tk.Frame(left_frame,width=300,height=100)

b=Button(f,text="4",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="5",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="6",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

f.pack()


'''Third Button Line'''

f=tk.Frame(left_frame,width=300,height=100)

b=Button(f,text="1",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="2",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text="3",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)
f.pack()


'''Fourth Button Line'''

f=tk.Frame(left_frame,width=300,height=100)

b=Button(f,text="0",bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text='.',bg='White')
b.pack(side=LEFT,ipadx=30,ipady=30)
b.bind("<Button-1>",click)

b=Button(f,text='%',bg='White')
b.pack(side=LEFT,ipadx=27,ipady=30)
b.bind("<Button-1>",click)
f.pack()




'''Right Frame '''

right_frame=tk.Frame(main_frame,width=200,height=400)
right_frame.grid(row=1,column=2)

'''First Button Line'''

f=tk.Frame(right_frame,width=200,height=100)

b=Button(f,text='C',font=("Arial",15),bg='#F58C0F')
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind("<Button-1>",click)

b=Button(f,text='Del',font=("Arial",15),bg='#F58C0F')
b.pack(side=LEFT,ipadx=21,ipady=25)
b.bind("<Button-1>",click)

f.pack()



'''Second Button Line'''

f=tk.Frame(right_frame,width=200,height=100)

b=Button(f,text='*',bg='#080000',fg='white',font=("Arial",20))
b.pack(side=LEFT,ipadx=35,ipady=25)
b.bind("<Button-1>",click)

b=Button(f,text='/',bg='#080000',fg='white',font=("Arial",20))
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind("<Button-1>",click)

f.pack()



'''Third Button Line'''

f=tk.Frame(right_frame,width=200,height=100)

b=Button(f,text='+',bg='#080000',fg='white',font=("Arial",20))
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind("<Button-1>",click)

b=Button(f,text='-',bg='#080000',fg='white',font=("Arial",20))
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind("<Button-1>",click)

f.pack()




'''Fourth Button Line'''

f=tk.Frame(right_frame,width=200,height=100)

b=Button(f,text='=',bg='Green')
b.pack(side=LEFT,ipadx=80,ipady=25,pady=5,padx=0)
b.bind("<Button-1>",click)

f.pack()





output_frame=tk.Frame(root,width=500,height=80)


value=StringVar()
value.set('')
input=tk.Label(output_frame,textvar=value,font=("lucida 25 bold "),bg="white")
input.pack()


output_frame.pack(side=BOTTOM,anchor='sw')





root.mainloop()