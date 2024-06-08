from tkinter import *

def main():
    window = Tk()
    window.title = "PySQLui"
    window.geometry('720x720')
    initialForm(window)
    window.mainloop()

def initialForm(window):

    def mostrarInformacoes(user_input, psw_input, db_input):
        user = user_input.get()
        psw = psw_input.get()
        db = db_input.get()
        print(f"usuário: {user}\nsenha: {psw}\nbanco de dados: {db} ")
    
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
    
    #botão para confirmar as escolhas
    btn_enviar = Button(window, text="Enviar", command= lambda: mostrarInformacoes(entry_user, entry_password, entry_db))
    btn_enviar.grid(column=1, row=4, padx=10, pady=10)

if __name__ == "__main__":
    main()
