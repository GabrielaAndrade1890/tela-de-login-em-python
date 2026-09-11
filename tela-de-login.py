from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'gabi' and valores['senha'] == '1234':
            print('Bem-vindo ao programa!')