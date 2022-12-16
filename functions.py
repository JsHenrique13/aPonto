import PySimpleGUI as sg
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sg.theme('BlueMono')


def telalogin():
    layout = [
        [sg.Text("Email :", size=(10, 1)), sg.Input(key="email", size=(25, 1))],
        [sg.Text("Senha :", size=(10, 1)), sg.Input(key="senha", size=(25, 1))],
        [sg.Text()],
        [sg.Button("Sair"), sg.Push(), sg.Button("Login", size=(12, 1)), sg.Push()],
        
    ]

    telal = sg.Window(title="Tela de Login", layout=layout, element_justification='c')

    while True:
        event, values = telal.read()
        if event == sg.WIN_CLOSED: 
            break
        print(values["email"])

    telal.close()


    # telalogin()

def telachave(key):
    layout = [
        [sg.Text("Digite a sua Chave", justification="c")],
        [sg.Input(key="chave", size=(10, 1))],
        [sg.Text()],
        [sg.Button("Voltar", s=6, button_color="red"), sg.Push(), sg.Button("Validar", size=(12, 1)), sg.Push()],
        
    ]

    telak = sg.Window(title="Validação", layout=layout, element_justification='c', resizable=True, )

    while True:
        event, values = telak.read()
        if event in (sg.WIN_CLOSED, "Voltar"): 
            telak.disappear()
        if event == "Validar":
            if values["chave"] != key:
                sg.PopupOK("Chave inválida")
            else:
                break

    telak.close()


def telacadastro():
    layout = [
        [sg.Text()],
        [sg.Text("Nome :", size=(12, 1), justification="c"), sg.Input(key="nome", size=(25, 1))],
        [sg.Text("Email :", size=(12, 1), justification="c"), sg.Input(key="email", size=(25, 1))],
        [sg.Text("Crie sua senha:", size=(12, 1)), sg.Input(key="senha0", size=(25, 1), password_char="*")],
        [sg.Text("Confirmar senha:", size=(12, 1)), sg.Input(key="senha1", size=(25, 1), password_char="*")],
        [sg.Text()],
        [sg.Text("Selecione o seu respectivo Team: ")],
        [sg.Push(), sg.Checkbox("Team Green", key="green"), sg.Push(), sg.Checkbox("Team Black", key="black"), sg.Push(), sg.Checkbox("Team Blue", key="blue"), sg.Push()],
        [sg.Text()],
        [sg.Checkbox("É coordenador ?", key="coord")],
        [sg.Text()],
        [sg.Button("Sair", s=6, button_color="tomato"), sg.Push(), sg.Button("Cadastrar", size=(12, 1)), sg.Push()],
    ]

    telac = sg.Window(title="Tela de Cadastro", layout=layout, element_justification='c', size=(400, 350))
    send = 0
    while True:

        event, values = telac.read()
        if event == sg.WIN_CLOSED or event == "Sair": 
            break
        if values["senha0"] != values["senha1"]:
            sg.popup("Senhas Incoerentes...")              
        if "@" not in values["email"] and ".com" not in values["email"]:
            sg.popup("Email Inválido") 
        if event == "Cadastrar":
            for v in values:
                while values[f"{v}"] == '':
                    
                    # print(f"campo {v} está vazio!")
                    sg.popup_ok(f"Preencha o campo {v}!")

        print(send)
        if event == "Cadastrar" and send == 4:
            try:
                # sg.popup_ok("Email enviado!")
                n = str(randint(000000, 999999))
                # validar usuario atraves do codigo por email

                #   envio de código
                envio = "atendimento@assesi.com"
                destino = values["email"]
                msg = MIMEMultipart()

                msg['From'] = envio
                msg['To'] = destino
                msg['Subject'] = "aPonto"

                body = f"""
                        <h2>Seja bem vindo {values["nome"].capitalize()}! Ao novo sistema de ponto da Assesi</h2>
                        <h3>sua chave é : {n}</h3>
                        <p>Copie a sua chave e preencha no sistema para validar seu usuario!</p>
        
                            """
                msg.attach(MIMEText(body, 'html'))
                #   iniciando o servidor
                server = smtplib.SMTP('smtp.gmail.com', 587)  # setando conexçao com o host do gmail
                server.starttls()  # iniciando a conexão
                server.login(envio, "yplqyqrmkvhzpfnp")  # logando com o email que vai enviar o email
                text = msg.as_string()  # codificando as informações pro formato de leitura do gmail
                server.sendmail(envio, destino, text)  # enviando as informações
                server.quit()  # fechando conexçao com o servidor
                #   termino de envio
                sg.popup_ok("Email enviado!")

                telachave(n)
                print(values)
                break

            except:
                continue

    telac.close()


# telacadastro()


def telamain():

    layout = [
        [sg.Text()],
        [sg.Text("Nome :", size=(12,1), justification="c"),sg.Input(key="nome", size=(25,1)) ],
        [sg.Text("Email :", size=(12,1), justification="c"),sg.Input(key="email", size=(25,1)) ],
        [sg.Text("Crie sua senha:",size=(12,1) ),sg.Input(key="senha0", size=(25,1), password_char="*")],
        [sg.Text("Confirmar senha:",size=(12,1) ),sg.Input(key="senha1", size=(25,1), password_char="*")],
        [sg.Text()],
        [sg.Text("Selecione o seu respectivo Team: ")],
        [sg.Push(),sg.Checkbox("Team Green", key="green"),sg.Push(),sg.Checkbox("Team Black", key="black"),sg.Push(),sg.Checkbox("Team Blue", key="blue"),sg.Push()],
        [sg.Text()],
        [sg.Checkbox("É coordenador ?", key="coord")],
        [sg.Text()],
        [sg.Button("Sair"),sg.Push(),sg.Button("Cadastrar", size=(12,1)), sg.Push()], 
    ]

    telam = sg.Window(title="Tela de Cadastro", layout=layout, element_justification='c', size=(800,450))

    while True:
        event, values = telam.read()
        if event == sg.WIN_CLOSED: 
            break
        
        
    telam.close()

    """
                    for v in values:
                    if v == "":

                        # sg.PopupAutoClose(f"Campo {v} esta vazio!")
                    else:

                        n = str(randint(000000, 999999))
                        # validar usuario atraves do codigo por email 

                        #   envio de código
                        envio = "atendimento@assesi.com"
                        destino = values["email"]
                        msg = MIMEMultipart()

                        msg['From'] = envio
                        msg['To'] = destino
                        msg['Subject'] = "aPonto"

                        body = f"""
    # <h2>Seja bem vindo {values["nome"].capitalize()}! ao novo sistema de ponto da Assesi</h2>
    # <h3>sua chave é : {n}</h3>
    # <p>Copie a sua chave e preencha no sistema para validar seu usuario!</p>

    """
    msg.attach(MIMEText(body, 'html'))
    #   iniciando o servidor
    server = smtplib.SMTP('smtp.gmail.com', 587)    # setando conexçao com o host do gmail
    server.starttls()   # iniciando a conexão
    server.login(envio, "yplqyqrmkvhzpfnp")  # logando com o email que vai enviar o email
    text = msg.as_string()  # codificando as informações pro formato de leitura do gmail
    server.sendmail(envio, destino, text)  # enviando as informações
    server.quit()   # fechando conexçao com o servidor
    #   termino de envio 

    telachave(n)
    break
    """

telacadastro()