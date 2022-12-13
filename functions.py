import PySimpleGUI as sg


def telalogin():
    layout = [
        [sg.Text("Email :", size=(10,1)),sg.Input(key="email", size=(25,1)) ],
        [sg.Text("Senha :", size=(10,1)),sg.Input(key="senha", size=(25,1)) ],
        [sg.Text()],
        [sg.Button("Sair"),sg.Push(),sg.Button("Login", size=(12,1)), sg.Push()],
        
    ]

    telal = sg.Window(title="Tela de Login", layout=layout, element_justification='c')

    while True:
        event, values = telal.read()
        if event == sg.WIN_CLOSED: 
            break
        print(values["email"])

    telal.close()


# telalogin()

def telacadastro():
    layout = [
        [sg.Text()],
        [sg.Text("Nome :", size=(12,1), justification="c"),sg.Input(key="nome", size=(25,1)) ],
        [sg.Text("Email :", size=(12,1), justification="c"),sg.Input(key="email", size=(25,1)) ],
        [sg.Text("Crie sua senha:",size=(12,1) ),sg.Input(key="senha0", size=(25,1), password_char="*")],
        [sg.Text("Confirmar senha:",size=(12,1) ),sg.Input(key="senha1", size=(25,1), password_char="*")],
        [sg.Text()],
        [sg.Text("Selecione o seu respectivo Team")],
        [sg.Push(),sg.Checkbox("Team Green", key="green"),sg.Push(),sg.Checkbox("Team Black", key="black"),sg.Push()],
        [sg.Checkbox("É coordenador ?", key="coord")],
        [sg.Text()],
        [sg.Button("Sair"),sg.Push(),sg.Button("Cadastrar", size=(12,1)), sg.Push()], 
    ]

    telac = sg.Window(title="Tela de Cadastro", layout=layout, element_justification='c')

    while True:
        event, values = telac.read()
        if event == sg.WIN_CLOSED: 
            break
        
        if values["senha0"] != values["senha1"]:
            sg.popup("Senhas Incoerentes...")    
        
        if values["senha0"] == values["senha1"]:
            sg.popup("Senhas Compatíveis...")     
        
    telac.close()

telacadastro()