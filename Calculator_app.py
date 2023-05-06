from tkinter import *
import Math_function as mf
import inner_files_calculator as fc

root = Tk()
# root.geometry("500x500")
e = Entry(root, width=50, bg="white", fg="blue",
          borderwidth=5, font=("Helvetica", 20))
e.grid(row=0, column=0, columnspan=4)

# Give functionality to the button
def func(fun):
    def inner_func():
        s = fun(e.get())
        fc.save(s)
        mylebel = Label(root, text=s, font=("Helvetica", 30))
        mylebel.grid(row=1, column=0, columnspan=4)
    return inner_func

# Creating a Math function Button Widget
def func_button(fun, r, c, t):
    sum_button = Button(root, text=t, command=fun,
                        fg="#0000cc", bg="#ccffff", height=2, width=20)
    sum_button.grid(row=r, column=c)


sum_func = func(mf.sum)
sub_func = func(mf.sub)
mul_func = func(mf.mul)
div_func = func(mf.div)
pow_func = func(mf.pow)
sqrt_func = func(mf.sqrt)
log_func = func(mf.log)

func_button(sum_func, 2, 0, "Sum")
func_button(sub_func, 2, 1, "Sub")
func_button(mul_func, 2, 2, "Mul")
func_button(div_func, 2, 3, "Div")
func_button(pow_func, 3, 0, "Pow")
func_button(sqrt_func, 3, 1, "Sqrt")
func_button(log_func, 3, 2, "Log")


root.mainloop()
