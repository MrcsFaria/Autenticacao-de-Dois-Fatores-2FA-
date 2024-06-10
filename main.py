#pip install sqlite3
import sqlite3
#pip install tkinter
import tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter import messagebox
#pip install customtkinter
from customtkinter import *
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#pip install pillow
from PIL import Image
#pip install python-dotenv
from dotenv import load_dotenv

#Carregando o .env e coletando as variáveis e-mail e senha de quem irá enviar o email
load_dotenv()
email_env=os.getenv('EMAIL')
senha_env=os.getenv('SENHA')

#Obtém o diretório
diretorio = os.getcwd()

#Constrói o caminho completo
db_path = os.path.join(diretorio, "Banco_de_dados", "usuarios.db")
img_lat_path = os.path.join(diretorio, "assets", "side-img.png")
user_icon_path = os.path.join(diretorio, "assets", "user-icon.png")
email_icon_path = os.path.join(diretorio, "assets", "email-icon.png")
senha_icon_path = os.path.join(diretorio, "assets", "password-icon.png")

#Função para Encerrar programa ao clicar no X da interface gráfica
def confirmar():
    ans = askyesno(title='Sair', message='Tem certeza que quer Sair?')
    if ans:
        sys.exit()

#Criando a Tela da Interface Gráfica
app = CTk()
app.title("Tela Inicial")
app.geometry("600x600")
app.configure(bg="#DCDCDC")

#Função para inserir o cadastro no Banco de Dados
def inserir_cad_banco():
    try:
        nome_user = nome.get()
        email_user = email.get()
        senha_user = senha.get()
        if not all([nome_user, email_user, senha_user]): 
            messagebox.showwarning("Aviso!", "Preencha todos os campos")
        else:
            dados = (nome_user,email_user,senha_user)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)", dados)
            conn.commit()
            conn.close()

            messagebox.showinfo("Aviso!","Usuário cadastrado com sucesso!")

            tela_cad.withdraw()
            app.deiconify()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao Cadastrar usuário: {str(e)}")

#Criação da Tela de Cadastro
def cadastro():
    global nome, email, senha, tela_cad
    app.withdraw()
    
    tela_cad = CTkToplevel()
    tela_cad.title("Cadastro")
    tela_cad.geometry("600x600")
    tela_cad.configure(bg="#DCDCDC")
    CTkLabel(master=tela_cad, text="", image=img_lat).pack(expand=True, side="left")

    frame_cad = CTkFrame(master=tela_cad, width= int(0.6 * largura_tela), height=int(altura_tela), fg_color="#ffffff")
    frame_cad.pack_propagate(0)
    frame_cad.pack(expand=True, side="right")

    CTkLabel(master=frame_cad, text="Cadastre-se", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))

    CTkLabel(master=frame_cad, text=" Nome:", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(30, 0), padx=(60, 0))
    nome = CTkEntry(master=frame_cad, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000")
    nome.pack(anchor="w", padx=(60, 0))

    CTkLabel(master=frame_cad, text=" E-mail:", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(30, 0), padx=(60, 0))
    email = CTkEntry(master=frame_cad, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000")
    email.pack(anchor="w", padx=(60, 0))

    CTkLabel(master=frame_cad, text=" Senha:", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), image=senha_icon, compound="left").pack(anchor="w", pady=(20, 0), padx=(60, 0))
    senha = CTkEntry(master=frame_cad, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000", show="*")
    senha.pack(anchor="w", padx=(60, 0))

    CTkButton(master=frame_cad, text="Cadastre-se", fg_color="#00009C", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=inserir_cad_banco).pack(anchor="w", pady=(15, 0), padx=(60, 0))

    tela_cad.protocol("WM_DELETE_WINDOW", confirmar)

#Função para verificar se o login e senha estão cadastrados no banco de dados
def verificar_usuario(user, senha):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consultar a tabela de usuários
    cursor.execute('SELECT email FROM users WHERE nome = ? AND senha = ?', (user, senha))
    usuario = cursor.fetchone()

    conn.close()
    
    # Retornar True se o usuário foi encontrado, caso contrário, False
    return usuario[0] if usuario else None

#Função para Enviar o código de autenticação para o email de cadastro do usuário
def enviar_cod_verif(email, codigo):
    # Configuração do servidor SMTP
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    remetente_email = email_env
    remetente_senha = senha_env

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente_email
    msg['To'] = email
    msg['Subject'] = "Código de verificação para login"
    body = "Seu código de verificação é: {}".format(codigo)
    msg.attach(MIMEText(body, 'plain'))

    # Enviando o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(remetente_email, remetente_senha)
        server.send_message(msg)

#Função para gerar o codigo de Autenticação
def gerar_cod_verif():
    return str(random.randint(100000, 999999))

#Função para verificar se o codigo inserido é o mesmo que o código enviado por e-mail
def verificar_codigo():
    codigo_inserido = cod.get()
    if codigo_verificacao == codigo_inserido:
        messagebox.showinfo("Aviso!","Usuário autenticado com sucesso!")
        tela_aut.withdraw()

        tela_suc = CTkToplevel()
        tela_suc.title("Sucesso")
        tela_suc.geometry("600x600")
        tela_suc.configure(bg="#DCDCDC")

        CTkLabel(master=tela_suc, text="", image=img_lat).pack(expand=True, side="left")

        frame_suc = CTkFrame(master=tela_suc, width= int(0.6 * largura_tela), height=int(altura_tela), fg_color="#ffffff")
        frame_suc.pack_propagate(0)
        frame_suc.pack(expand=True, side="right")

        CTkLabel(master=frame_suc, text="Sucesso!", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))
        tela_suc.protocol("WM_DELETE_WINDOW", confirmar)

    else:
        messagebox.showinfo("Aviso!","Código Incorreto!")

#Criação da tela de Login
def login():
    global codigo_verificacao, cod, tela_aut
    usuario_lgn = logn.get()
    senha_lgn = passw.get()
    email_lgn = verificar_usuario(usuario_lgn, senha_lgn)
    if email_lgn:
        codigo_verificacao = gerar_cod_verif()
        enviar_cod_verif(email_lgn, codigo_verificacao)
        app.withdraw()
    
        tela_aut = CTkToplevel()
        tela_aut.title("Autenticação")
        tela_aut.geometry("600x600")
        tela_aut.configure(bg="#DCDCDC")

        CTkLabel(master=tela_aut, text="", image=img_lat).pack(expand=True, side="left")

        frame_aut = CTkFrame(master=tela_aut, width= int(0.6 * largura_tela), height=int(altura_tela), fg_color="#ffffff")
        frame_aut.pack_propagate(0)
        frame_aut.pack(expand=True, side="right")

        CTkLabel(master=frame_aut, text="Autenticação", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))
        CTkLabel(master=frame_aut, text="Insira o código de autenticação enviado por e-mail", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        cod = CTkEntry(master=frame_aut, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000")
        cod.pack(anchor="w", padx=(60, 0))

        CTkButton(master=frame_aut, text="Confirmar", fg_color="#00009C", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=verificar_codigo).pack(anchor="w", pady=(15, 0), padx=(60, 0))
        tela_aut.protocol("WM_DELETE_WINDOW", confirmar)

    else:
        print("E-mail ou senha incorretos.")

#Função para mostrar senha
def mostrar_senha():
    stat = check_var.get()
    if stat == "on":
        passw.configure(show='')
    else:
        passw.configure(show='*')

check_var = tkinter.StringVar(master=app)

img_lat_data = Image.open(img_lat_path)
email_icon_data = Image.open(email_icon_path)
user_icon_data = Image.open(user_icon_path)
senha_icon_data= Image.open(senha_icon_path)

largura_tela = 600
altura_tela = 600

img_lat = CTkImage(dark_image=img_lat_data, light_image=img_lat_data, size=(int(0.4*largura_tela),altura_tela))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
senha_icon = CTkImage(dark_image=senha_icon_data, light_image=senha_icon_data, size=(17,17))
user_icon = CTkImage(dark_image=user_icon_data, light_image=user_icon_data, size=(20,20))

CTkLabel(master=app, text="", image=img_lat).pack(expand=True, side="left")

frame = CTkFrame(master=app, width= int(0.6 * largura_tela), height=int(altura_tela), fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Bem Vindo(a)!", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))
CTkLabel(master=frame, text="Realize o Login", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text=" Login:", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(30, 0), padx=(60, 0))
logn = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000")
logn.pack(anchor="w", padx=(60, 0))

CTkLabel(master=frame, text=" Senha:", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), image=senha_icon, compound="left").pack(anchor="w", pady=(20, 0), padx=(60, 0))
passw = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#00009C", border_width=1, text_color="#000000", show="*")
passw.pack(anchor="w", padx=(60, 0))

checkbox = CTkCheckBox(master=frame, text=" Mostrar Senha:", text_color="#00009C", font=("Arial Bold", 12),command=mostrar_senha, variable=check_var, onvalue="on", offvalue="off").pack(anchor="w", pady=(35, 0), padx=(60, 0))

CTkButton(master=frame, text="Login", fg_color="#00009C", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=login).pack(anchor="w", pady=(30, 0), padx=(60, 0))

CTkLabel(master=frame, text=" Ainda não tem conta?", text_color="#00009C", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(30, 0), padx=(60, 0))
CTkButton(master=frame, text="Cadastre-se", fg_color="#00009C", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=cadastro).pack(anchor="w", pady=(15, 0), padx=(60, 0))


app.protocol("WM_DELETE_WINDOW", confirmar)
app.mainloop()