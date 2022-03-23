from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import requests

GUI = Builder.load_file("teste.kv")

class MeuAplicativo(App):

    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["imagem1"].window = Image(source="logo.png")
        self.root.ids["caixa"].window = TextInput()
        self.root.ids["botao"].window = Button(text='Pesquisar', font_size=14)

    def btn_clk(self):
        print("You have been pressed")
        self.root.ids["my_label"].text = "You have been pressed"

    def process(self):
        text = self.root.ids.caixa.text
        return (text)

    def pegar_cep(self):

        text = self.root.ids.caixa.text

        def teste(text):
            p1 = '25901585'
            if len(p1) == len(text):
                teste = 'corrreto'
                return teste
            else:
                teste = 'erro'
                return teste

        if teste(text) == 'corrreto':

            link = f"https://cep.awesomeapi.com.br/json/{str(text)}"
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()

            if 404 in dic_requisicao.values():
                self.root.ids["my_label"].text = "Informe um cep valido!"
            else:
                um = dic_requisicao["address"]
                dois = dic_requisicao["district"]
                tres = dic_requisicao["city"]
                a = (str(um) + ', ' + str(dois) + ', ' + str(tres))
                self.root.ids["my_label"].text = f"{a}"

        else:
            self.root.ids["my_label"].text = "Informe um cep valido!"

MeuAplicativo().run()
