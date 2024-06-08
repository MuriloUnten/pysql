from tkinter import *

def main():
    window = Tk()
    window.title = "PySQLui"
    window.geometry('720x720')
    initialForm(window)
    window.mainloop()

def initialForm(window):
    lbl1 = Label(window, text="Nome do banco de dados:")
    lbl1.grid(column=0, row=0)
    entry_db = Entry(window, width=30)
    entry_db.grid(column=1, row=0, padx=10, pady=5)


    lbl2 = Label(window, text="Senha do banco de dados:")
    lbl2.grid(column=0, row=1)
    entry_password = Entry(window, width=30, show="*")
    entry_password.grid(column=1, row=1, padx=10, pady=5)

if __name__ == "__main__":
    main()
