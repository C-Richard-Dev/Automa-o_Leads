import pyautogui as auto 

auto.PAUSE = 1.5

class Open_Google():
    def __init__(self):
        self.abrir_navegador()


    def abrir_navegador(self):


        site = str(input("\n\nDigite o nome do site: "))
        produto = str(input("Digite o nicho desejado (ex: esportes, roupas, camisas...): "))

        auto.click(x=1375, y=1043)
        auto.sleep(1.5)
        query = f'site:{site}.com "{produto}" ("gmail.com" OR "hotmail.com") ("(91)" OR "+55")'
        auto.sleep(1.5)
        auto.write(query)
        auto.press('enter')
        auto.sleep(6)



