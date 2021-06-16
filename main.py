import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import  *
# from matplotlib import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import messagebox, Tk, Label, Entry, Button
from tkinter import ttk

large_font = ('Ambit', 90, "bold",)
small_font = ('Bookman Old Style', 15,)
button_font = ('Ambit', 22, "bold")
extra_small = ('Ambit', 20, "bold")
bg_color = "#FFFFFF"
fg_color = "#FF7A01"


class VerticalScrolledFrame(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)


class Frames(object):
    def main_frame(self, root):
        root.title('Bisection algorithm')
        root.geometry('1920x1080')
        self.function = StringVar()
        self.function.set("x**3-x+1")
        self.a = StringVar()
        self.a.set("-2")
        self.b = StringVar()
        self.b.set("2")
        self.epsilon = StringVar()
        self.epsilon.set("0.0001")
        l3 = Label(root, text="Bisection algorithm", justify=CENTER, font=large_font)
        l3.configure(background=bg_color, foreground=fg_color)
        l3.place(relx=0.5,
                 rely=0.05,
                 anchor='center')
        l4 = Label(root, text="Function:", font=extra_small)
        l4.configure(background=bg_color, foreground="black")
        l4.place(relx=0.037,
                 rely=0.2,
                 anchor='center')
        e3 = Entry(root, font=extra_small, textvariable=self.function)
        e3.configure(background="#FFFFFF", foreground="black")
        e3.place(relx=0.21,
                 rely=0.2,
                 anchor='center', width="500", height="60")
        l5 = Label(root, text="a:", font=extra_small)
        l5.configure(background=bg_color, foreground="black")
        l5.place(relx=0.36,
                 rely=0.2,
                 anchor='center')
        e4 = Entry(root, font=extra_small, textvariable=self.a)
        e4.configure(background="#FFFFFF", foreground="black")
        e4.place(relx=0.43,
                 rely=0.2,
                 anchor='center', width="200", height="60")
        l6 = Label(root, text="b:", font=extra_small)
        l6.configure(background=bg_color, foreground="black")
        l6.place(relx=0.51,
                 rely=0.2,
                 anchor='center')
        e5 = Entry(root, font=extra_small, textvariable=self.b)
        e5.configure(background="#FFFFFF", foreground="black")
        e5.place(relx=0.59,
                 rely=0.2,
                 anchor='center', width="200", height="60")
        l7 = Label(root, text="\u03B5:", font=extra_small)
        l7.configure(background=bg_color, foreground="black")
        l7.place(relx=0.68,
                 rely=0.2,
                 anchor='center')
        e6 = Entry(root, font=extra_small, textvariable=self.epsilon)
        e6.configure(background="#FFFFFF", foreground="black")
        e6.place(relx=0.75,
                 rely=0.2,
                 anchor='center', width="200", height="60")
        b2 = Button(root, text="Submit", width="25", font=button_font, command=self.bisection)
        b2.configure(background="#FF7A01", foreground="#FFFFFF")
        b2.place(relx=0.7,
                 rely=0.3,
                 anchor='center')

    # def draw_plot(self):

    def func(self, x):
        try:
            evaluated = eval(self.function.get())
        except:
            evaluated = 0  # Returns the value of the function
        return evaluated

    def bisection(self):
        self.frame = VerticalScrolledFrame(root)
        self.frame.place(relx=0.22,
                         rely=0.62,
                         anchor='center', width="800", height="750")
        results = []
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            epsilon = float(self.epsilon.get())
            n = 0
            if self.func(a) * self.func(b) >= 0:
                results.append(
                    Label(self.frame.interior, text="You have not assumed\n right a and b",
                          font=('Bookman Old Style', 30), width="78", height="3", background="#FF7A01",
                          foreground="#FFFFFF"))
                results[-1].pack()
                return

            c = a
            while (b - a) >= epsilon:
                # Find middle point
                c = (a + b) / 2
                n = n + 1
                results.append(Label(self.frame.interior,
                                     text="Step " + str(n) + "\tThe value of root is : " + str(c),
                                     width="78", height="3", font=small_font, background="#FFFFFF", foreground="black"))
                results[-1].pack()

                # Check if middle point is root
                if abs(self.func(c)) <= epsilon:
                    break

                # Decide the side to repeat the steps
                if self.func(c) * self.func(a) < 0:
                    b = c
                else:
                    a = c
            n = n + 1
            results.append(Label(self.frame.interior,
                                 text="The final value of root is : " + str(c),
                                 width="78", height="3", font=('Bookman Old Style', 20, "bold"), background="#FF7A01",
                                 foreground="#FFFFFF"))
            results[-1].pack()
            x = np.linspace(float(self.a.get()), float(self.b.get()), 10000)
            y = eval(self.function.get())
            fig = Figure(figsize=(11, 7))
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.grid()
            ax.yaxis.set_ticks_position('left')
            ax.plot(x, y, 'r')
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.get_tk_widget().place(relx=0.73,
                                         rely=0.69,
                                         anchor='center')
            canvas.draw()
        except:
            results.append(Label(self.frame.interior,
                                 text="Invalid input",
                                 width="78", height="4", font=button_font, background="#FF7A01", foreground="#FFFFFF"))
            results[-1].pack()


root = Tk()
root.configure(bg=bg_color)
app = Frames()
app.main_frame(root)
root.mainloop()
