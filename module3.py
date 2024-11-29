import tkinter as tk

def change_color():
    match var.get():
        case 0:
            button['bg'] = 'red'
        case 1:
            button['bg'] = 'green'
        case 2:
            button['bg'] = 'orange'
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("250x250")
    var = tk.IntVar()
    var.set(0)
    tk.Radiobutton(text='red', variable=var, value=0).pack()
    tk.Radiobutton(text='green', variable=var, value=1).pack()
    tk.Radiobutton(text='blue', variable=var, value=2).pack()
    button = tk.Button(text='Изменить', command=change_color, width=10, height=5)
    button.pack()
    root.mainloop()