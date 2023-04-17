import PySimpleGUI as sg
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    senha = ''
    for i in range(tamanho):
        senha += random.choice(caracteres)
        
    return senha


def salvar_senha(senha):
        with open('senhas.tx', 'w') as arquivo:
            arquivo.write(senha)
        print('Sua senha foi salva!')
            
            
class TelaPython():
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Seja bem vindo ao gerador de senhas!!',)],
            [sg.Text('Qual o tamanho da senha?', size=(20, 0)),sg.Input(key='tamanho', size=(5,0))],
            [sg.Text('Deseja salvar a senha em um documento de texto?',)],
            [sg.Radio('Sim', 'group1', key='salvar'),sg.Radio('Não', 'group1')],
            [sg.Button('Gerar senha')],
            [sg.Output(size=(40, 10))]
            
        ]
        # janela
        self.janela = sg.Window('Gerador de senhas').layout(layout)
        # exportar informações
        self.button, self.values = self.janela.Read()
    
    def iniciar(self):
        while True:
            # exportar informações
            self.button, self.values = self.janela.Read()     
            tamanho = int(self.values['tamanho'])
            salvar = self.values['salvar']      
            
            a = gerar_senha(tamanho)
            print(a)
            if salvar:
                salvar_senha(a)
                salvar = False
            else:
                print('Sua senha não foi salva!')
           
            
tela = TelaPython()
tela.iniciar()