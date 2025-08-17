import tkinter as tk
window =tk.Tk()
window.title("My First GUI")
window.geometry("400x400")
l1=tk.Label(window,text="assd",font=("Arial", 12))
#l1.pack()
l1.grid(row=1,column=0)
l2=tk.Label(window,text="assd",font=("Arial", 12))
#l2.pack()
l2.grid(row=2,column=1)


bt=tk.Button(window,text="button1",bg="red",fg="white",command=lambda:print("button1 clicked"))
bt.grid(row=4,column=0)

txt=tk.Entry(window)
txt.grid(row=3,column=0)
txt.insert(0,"Enter text here")

frame = tk.Frame(window,bg="blue", width=200, height=100)
frame.grid(row=5,column=0,columnspan=2,pady=10)



    

window.mainloop()