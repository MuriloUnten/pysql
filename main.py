from tkinter import *
from backend.Connector import MySQLConnector, PostgresConnector
from tkinter import ttk
def main():
    window = Tk()
    window.title = "PySQLui"
    window.geometry('720x720')
    initialForm(window)
    # tree(window)
    window.mainloop()

def initialForm(window):

    # primeira caixa de texto, inserir usuário
    lbl1 = Label(window, text="Nome do usuário:")
    lbl1.grid(column=0, row=0)
    entry_user = Entry(window, width=30)
    entry_user.grid(column=1, row=0, padx=10, pady=5)

    # segunda caixa de texto, inserir senha
    lbl2 = Label(window, text="Senha do banco de dados:")
    lbl2.grid(column=0, row=1)
    entry_password = Entry(window, width=30, show="*")
    entry_password.grid(column=1, row=1, padx=10, pady=5)

    # terceira caixa de texto, inserir o nome banco de dados usado
    lbl3 = Label(window, text="Nome do banco de dados:")
    lbl3.grid(column=0, row=2)
    entry_db = Entry(window, width=30)
    entry_db.grid(column=1, row=2, padx=10, pady=5)

    # caixa para selecionar banco de dados utilizado
    choices = ['MySQL', 'PostGress']
    selected_db = StringVar(window, "Select Database")
    w = OptionMenu(window, selected_db, *choices)
    w.grid(column=1, row=3, padx=10, pady=5)

    def connect(entry_user, entry_password, entry_db, selected_db):
        user = entry_user.get()
        password = entry_password.get()
        db_name = entry_db.get()
        db_type = selected_db.get()
        if db_type == "MySQL":
            connector = MySQLConnector()
            connector.connect(database=db_name, user=user, password=password)
        table = connector.getTableInfo("app_user")
        tableDataView(window, table)

    #botão para confirmar as escolhas
    btn_enviar = Button(window, text="Enviar", command=lambda: connect(entry_user, entry_password, entry_db, selected_db))
    btn_enviar.grid(column=1, row=30, padx=10, pady=10)

def tree(window):

    # Criar o widget Treeview
    tree = ttk.Treeview(window)

    # Definir as colunas
    tree["columns"] = ("coluna1", "coluna2", "coluna3")

    # Configurar as colunas
    tree.column("#0", width=150, minwidth=150)
    tree.column("coluna1", width=100, minwidth=100)
    tree.column("coluna2", width=100, minwidth=100)
    tree.column("coluna3", width=100, minwidth=100)

    # Definir os cabeçalhos das colunas
    tree.heading("#0", text="Tabelas")
    tree.heading("coluna1", text="Campos")
    tree.heading("coluna2", text="Tipo")
    tree.heading("coluna3", text="Tamanho")

    # Inserir dados no Treeview
    tree.insert("", "end", text="Item 1", values=("Value 1-1", "Value 1-2"))
    tree.insert("", "end", text="Item 2", values=("Value 2-1", "Value 2-2"))

    # Exibir o Treeview
    tree.grid(column=1, row=4, pady=20, padx=20)


def tableDataView(window, table):
    tree = ttk.Treeview(window)

    tree["columns"] = ("type", "null", "key", "default")

    tree.column("0", width=150, minwidth=150)
    tree.column("type", width=100, minwidth=100)
    tree.column("null", width=100, minwidth=100)
    tree.column("key", width=100, minwidth=100)
    tree.column("default", width=100, minwidth=100)

    tree.heading("#0", text="name")
    tree.heading("type", text="type")
    tree.heading("null", text="null")
    tree.heading("key", text="key")
    tree.heading("default", text="default")

    for col in table.cols:
        tree.insert("", "end", text=col.name, values=(col.type, col.null, col.key, col.default))

    tree.grid(column=1, row=4, pady=20, padx=20)

if __name__ == "__main__":
    main()
