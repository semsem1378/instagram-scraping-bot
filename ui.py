from math import floor
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import app


# // show progression
def showProgression(perc):
    wait_lb.configure(text="{:.2f}".format(perc))
    wait_lb.update()
    if floor(perc) == 100:
        wait_lb.configure(background='#00FF00')
        


# // reseting form variables
def reset_entry():
    hash_tf.delete(0,'end')
    username_tf.delete(0, 'end')
    password_tf.delete(0, 'end')
    amount_tf.delete(0, 'end')


# // checking variables and starting main proccess
def start_proccess():
    if username_tf.get() == '':
        messagebox.showwarning('enter username !!',' username is empty!!')
        return
    elif password_tf.get() == '':
        messagebox.showwarning('enter password !!',' password is empty!!')
        return
    elif hash_tf.get() == '':
        messagebox.showwarning('enter hashtag !!', ' hashtag is empty!!')
        return
    elif amount_tf.get() == '':
        messagebox.showwarning('enter posts number !!',' posts number is empty!!')
        return
    else:
        
        try:
            amount = int(amount_tf.get())
            hashtag = hash_tf.get().replace(' ', '_')
        except :
            messagebox.showerror('not a number !', 'tedad post ha bayad adad bashad')
            return
        messagebox.showinfo('please wait...','please wait...')
        app.main(user_name=username_tf.get(), pass_word=password_tf.get(), 
             hash_tag= hashtag.encode('utf-8'),posts_number=amount)
    
ws = Tk()
ws.title('instagram bot')
ws.geometry('400x300')
ws.config(bg='#686e70')



var = IntVar()


# // form appereance
frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)


hash_lb = Label(
    frame,
    text="Enter Hashtag:"
)
hash_lb.grid(row=1, column=1)


hash_tf = Entry(
    frame, 
)
hash_tf.grid(row=1, column=2, pady=5)


username_lb = Label(
    frame,
    text='Enter Username:'
)
username_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

username_tf = Entry(
    frame2,
)
username_tf.grid(row=2, column=2, pady= 5)

password_lb = Label(
    frame,
    text="Enter password:  "
)
password_lb.grid(row=3, column=1)

amount_lb = Label(
    frame,
    text="tedad post:  ",

)
amount_lb.grid(row=4, column=1)

password_tf = Entry(
    frame,
    show='*'
)
password_tf.grid(row=3, column=2, pady=5)

amount_tf = Entry(
    frame,
)
amount_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Start',
    command=start_proccess
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

newFrame = Frame(
    ws,
    padx=10, 
    pady=10
)
newFrame.pack(expand=True)

wait_lb = Label(
    newFrame,
    text=f'percent completed:0 %'
)
wait_lb.pack()


ws.mainloop()