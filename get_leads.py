import pyautogui as auto
import time
import pyperclip
import re
import pandas as pd


class CaptureEmails:
    def __init__(self):
        self.get_emails()

    def get_emails(self):
        auto.hotkey('ctrl', 'a') #Selecionar tudo
        auto.hotkey("ctrl", "c")
        time.sleep(1)

        texto = pyperclip.paste()
        email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        emails = re.findall(email_regex, texto)

        df = pd.DataFrame({"E-mail": emails}) #Coluna do Excel
        df.to_excel("emails_filtrados.xlsx", index=False) #Salvando os emails na planilha

        print("\nDados salvos em 'emails_filtrados.xlsx'!")

