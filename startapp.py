import socket
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


pclog = socket.gethostbyname(socket.gethostname())
print("="*30)
print("Assesi Ponto".center(30))
print("="*30)
print("")

try:
    nome_arquivo = "ip.txt"
    arquivo = open(nome_arquivo, 'r+')
    for l in arquivo:
        if l == pclog:
            email = input("Email: ")
            senha = input("Senha: ")
   
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines(pclog)
    nome = input("Nome: ")
    email = input("Email: ")
    senha1 = input("Crie uma senha: ")
    senha2 = input("Confirme sua senha: ")
    checkbox = input("É coordenador ?")
    n = randint(000000, 999999)
    # validar usuario atraves do codigo por email 

    #   envio de código
    fromaddr = "atendimento@assesi.com"
    toaddr = email
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "aPonto"

    body = f"""
        <h2>Seja bem vindo {nome.capitalize()}! ao novo sistema de ponto da Assesi</h2>
        <h3>sua chave é : {n}</h3>
        <p>Copie a sua chave e preencha no sistema para validar seu usuario!</p>
       """
    msg.attach(MIMEText(body, 'html'))
    #   iniciando o servidor
    server = smtplib.SMTP('smtp.gmail.com', 587)    # setando conexçao com o host do gmail
    server.starttls()   # iniciando a conexão
    server.login(fromaddr, "yplqyqrmkvhzpfnp")  # logando com o email que vai enviar o email
    text = msg.as_string()  # codificando as informações pro formato de leitura do gmail
    server.sendmail(fromaddr, toaddr, text)  # enviando as informações
    server.quit()   # fechando conexçao com o servidor
    #   termino de envio 

    #input do codigo de validação
    while True:
        chave = input("Digite sua chave: ")
        if chave != str(n):
            print("Código incorreto, verifique seu email novamente...")
            continue
        else:
            break
    """dados = []
    dados.append(nome)
    dados.append(email)
    dados.append(senha2)
"""
arquivo.close()

# saber de qual maquina ele esta logando

# pclog = socket.gethostbyname(socket.gethostname())

# if cadastrar:

# cadastar user 

# saber a maquina que ele usou no cadastro