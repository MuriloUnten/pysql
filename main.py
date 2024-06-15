from tkinter import *
from backend.Connector import MySQLConnector, PostgresConnector
from utils.formatting import *
from tkinter import ttk
from tkinter import filedialog
import json
import csv

def main():
    window = Tk()
    window.title = "PySQLui"
    window.geometry('720x720')
    initialForm(window)
    window.mainloop()

def initialForm(window):
    def connect(entry_user, entry_password, entry_db, selected_db):
        user = entry_user.get()
        password = entry_password.get()
        db_name = entry_db.get()
        db_type = selected_db.get()
        if db_type == "MySQL":
            connector = MySQLConnector()
        else:
            connector = PostgresConnector()
        connector.connect(database=db_name, user=user, password=password)
        tablesTree(window, connector)

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
    choices = ['MySQL', 'PostgreSQL']
    selected_db = StringVar(window, "Select Database")
    w = OptionMenu(window, selected_db, *choices)
    w.grid(column=1, row=3, padx=10, pady=5)

    #botão para confirmar as escolhas
    btn_enviar = Button(window, text="Enviar", command=lambda: connect(entry_user, entry_password, entry_db, selected_db))
    btn_enviar.grid(column=2, row=3, padx=10, pady=10)

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

def querieTable(window, connector):
    lbl1 = Label(window, text="Digite sua query")
    lbl1.grid(column=0, row=5)
    query = Entry(window, width=30)
    query.grid(column=1, row=5, padx=10, pady=5)
    tree = ttk.Treeview(window)
    btn_executar = Button(window, text="Executar", command=lambda: tabelaPreenchida(query.get()))
    btn_executar.grid(column=2, row=5, padx=10, pady=10)

    def clear_tree():
        for item in tree.get_children():
            tree.delete(item)

    def tabelaPreenchida(sql):
        clear_tree()
        result, cols = connector.execute(query=sql)
        tree["columns"] = cols
        tree["show"] = "headings"
        for col in cols:
            tree.column(col, width=100, minwidth=100)
            tree.heading(col, text=col)

        for row in result:
            tree.insert("", "end", text=row[0], values=row[0:])
        tree.grid(column=1, row=7, pady=20, padx=20)
        exportBtn = Button(window, text="Export", command=lambda: export(result, cols))
        exportBtn.grid(column=1, row=6)

def export(queryResult, cols):
    filePath = filedialog.asksaveasfilename(
        initialdir="~/",
        title="Save file",
        filetypes=(("JSON file", "*.json"), ("CSV file", "*.csv"))
    )

    with open(filePath, "w") as file:
        if filePath.endswith(".json"):
            json.dump(jsonFormat(queryResult, cols), file, indent=4)
        elif filePath.endswith(".csv"):
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(cols)
            for row in queryResult:
                writer.writerow(row)


def tablesTree(window, connector):

    tree = ttk.Treeview(window)

    tree["columns"] = ("name", "type", "null", "key", "default")

    tree.column("0", width=100, minwidth=150)
    tree.column("name", width=100, minwidth=100)
    tree.column("type", width=100, minwidth=100)
    tree.column("null", width=100, minwidth=100)
    tree.column("key", width=100, minwidth=100)
    tree.column("default", width=100, minwidth=100)

    tree.heading("#0", text="table")
    tree.heading("name", text="name")
    tree.heading("type", text="type")
    tree.heading("null", text="null")
    tree.heading("key", text="key")
    tree.heading("default", text="default")

    tables = connector.getTables()

    for table in tables:
        pai = tree.insert("", "end", text=table)
        items = connector.getTableInfo(table)
        for col in items.cols:
            tree.insert(pai, "end", values=(col.name, col.type, col.null, col.key, col.default))

    tree.grid(column=1, row=4, pady=20, padx=20)
    querieTable(window, connector)

if __name__ == "__main__":
    main()
