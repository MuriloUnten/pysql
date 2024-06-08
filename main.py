from tkinter import *
from backend.Connector import MySQLConnector, PostgresConnector

def main():
    window = Tk()
    window.title = "PySQLui"
    window.geometry('720x720')
    initialForm(window)
    window.mainloop()

def initialForm(window):

    #primeira caixa de texto, inserir usuário
    lbl1 = Label(window, text="Nome do usuário:")
    lbl1.grid(column=0, row=0)
    entry_user = Entry(window, width=30)
    entry_user.grid(column=1, row=0, padx=10, pady=5)

    #segunda caixa de texto, inserir senha
    lbl2 = Label(window, text="Senha do banco de dados:")
    lbl2.grid(column=0, row=1)
    entry_password = Entry(window, width=30, show="*")
    entry_password.grid(column=1, row=1, padx=10, pady=5)

    #terceira caixa de texto, inserir o nome banco de dados usado 
    lbl3 = Label(window, text="Nome do banco de dados:")
    lbl3.grid(column=0, row=2)
    entry_db = Entry(window, width=30)
    entry_db.grid(column=1, row=2, padx=10, pady=5)

    #caixa para selecionar banco de dados utilizado
    choices = ['MySQL', 'PostGress']
    selected_db = StringVar(window)
    selected_db.set('Select Data Base')
    w = OptionMenu(window, selected_db, *choices)
    w.grid(column=1, row=3, padx=10, pady=5)
    
    # user = entry_user.get()
    # password = entry_password.get()
    # db_name = entry_db.get()
    # db_type = selected_db

    user = "root"
    password = "Db_12345678"
    db_name = "UniSystem"
    db_type = "MySQL"

    #botão para confirmar as escolhas
    btn_enviar = Button(window, text="Enviar", command= lambda: connect(user, password, db_name, db_type))
    btn_enviar.grid(column=1, row=4, padx=10, pady=10)

    def connect(user, password, db_name, db_type):
        if (db_type=="MySQL"):
            connector = MySQLConnector()
            connector.connect(database=db_name, user=user,password=password)
            print(connector.getTables())


if __name__ == "__main__":
    main()
