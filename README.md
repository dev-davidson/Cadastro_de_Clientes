# Cadastro_de_Clientes
Gerenciador de Clientes

#bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

#Abertura de Janela
janela = Tk()
janela.title("Cadastro de Usuario")
janela.geometry("700x400")
janela.configure(background="white")
janela.resizable(width=False, height=False)


#imagens
logo = PhotoImage(file="imagens/fundo-01.png")


#Formatação da Janela
LeftFrama = Frame(janela, width=200, height=400, bg="blue", relief="raise")
LeftFrama.pack(side=LEFT)

RightFrama = Frame(janela, width=496, height=400, bg="blue", relief="raise")
RightFrama.pack(side=RIGHT)

#Formatação logo
LogoLabel = Label(LeftFrama, image=logo, bg="blue")
LogoLabel.place(x=-1, y=-1)
LogoLabel = Label(RightFrama, image=logo, bg="blue")
LogoLabel.place(x=-1, y=-1)

#Caixa de texto
UserLabel = Label(LeftFrama, text="Olá. Faça seu login", font=("Century Gothic", 15),bg="blue", fg="white")
UserLabel.place(x=5, y=15)

CPFLabel = Label(RightFrama, text="CPF:", font=("Century Gothic", 10),bg="blue", fg="white")
CPFLabel.place(x=5, y=100)
CPFEntry = ttk.Entry(RightFrama, width=30)
CPFEntry.place(x=100, y=108)

SenhaLabel = Label(RightFrama, text="Senha:", font=("Century Gothic", 10),bg="blue", fg="white")
SenhaLabel.place(x=5, y=150)
SenhaEntry = ttk.Entry(RightFrama, width=30, show="*")
SenhaEntry.place(x=100, y=160)

def Login():
    CPF = CPFEntry.get()
    Senha = SenhaEntry.get()
    
    database.cursor.execute("""
    SELECT * FROM Usuario
    WHERE CPF = ? AND Senha = ?
    """,(CPF, Senha))
    print("Selecionado")
    VerifyLogin = database.cursor.fetchone()
    try:
        if (CPF in VerifyLogin and Senha in VerifyLogin):
            messagebox.showinfo(title="Login info", message="Acesso Confirmado. Bem Vindo")
    
    except:
        messagebox.showinfo(title="login Info", message="Acesso negado")   

#Botoes
LoginButton = ttk.Button(RightFrama, text="Login", width=30, command=Login)
LoginButton.place(x=125, y=225)

def Register():
    LoginButton.place(x=2000)
    RegisterButton.place(x=2000)

    # Caixa de texto
    NomeLabel = Label(RightFrama,text="Nome:", font=("Century Gothic",10), bg="blue", fg="white")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RightFrama, width=30)
    NomeEntry.place(x=60, y=4)

    TelLabel = Label(RightFrama,text="Telefone:", font=("Century Gothic",10), bg="blue", fg="white")
    TelLabel.place(x=5, y=28)
    TelEntry = ttk.Entry(RightFrama, width=28)
    TelEntry.place(x=80, y=30)

    DataLabel = Label(RightFrama,text="Data de nascimento:", font=("Century Gothic",10), bg="blue", fg="white")
    DataLabel.place(x=5, y=50)
    DataEntry = ttk.Entry(RightFrama, width=30)
    DataEntry.place(x=40, y=90)

    RGLabel = Label(RightFrama,text="RG:", font=("Century Gothic",10), bg="blue", fg="white")
    RGLabel.place(x=5, y=70)
    RGEntry = ttk.Entry(RightFrama, width=30)
    RGEntry.place(x=40, y=60)

    EndLabel = Label(RightFrama,text="Endereço:", font=("Century Gothic",10), bg="blue", fg="white")
    EndLabel.place(x=5, y=70)
    EndEntry = ttk.Entry(RightFrama, width=30)
    EndEntry.place(x=40, y=60)

    #Banco de dados
    def RegisterToDatabase():
        CPF = CPFEntry.get()
        Nome = NomeEntry.get()
        Data = DataEntry.get()
        RG = RGEntry.get()
        Senha = SenhaEntry.get()
        Tel = TelEntry.get()
        End = EndEntry.get()


        if (CPF == "" and Nome == "" and Data == "" and RG =="" and Senha =="" and Tel =="" and End ==""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")
        else:
            database.cursor.execute("""
            INSERT INTO Usuario (CPF, Nome, Data, RG, Senha, Tel, End) VALUES(?, ?, ?, ?, ?, ?, ?)
            """, (CPF, Nome, Data, RG, Senha, Tel, End))
            database.conn.commit()
            messagebox.showinfo(title="Register Info", Message=("Conta criada Com Sucesso"))

    Register = ttk.Button(RightFrama, text="Registrar", width=30, command=RegisterToDatabase)
    Register.place(x=125, y=260)

    def BackToLogin():
        NomeLabel.place(x=2000)
        NomeEntry.place(x=2000)
        CPFLabel.place(x=2000)
        CPFEntry.place(x=2000)
        Register.place(x=2000)
        Back.place(x=2000)
        LoginButton.place(x=100)
        RegisterButton.place(x=125)
    
    Back = ttk.Button(RightFrama, text="Voltar", width=30, command=BackToLogin)
    Back.place(x=125, y=225)

RegisterButton = ttk.Button(RightFrama, text="Cadastrar", width=30, command=Register)
RegisterButton.place(x=125, y=260)

janela.mainloop()
