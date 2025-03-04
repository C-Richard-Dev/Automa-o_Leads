import pyautogui as auto 
import time
import pyperclip
import re
import pandas as pd  

auto.PAUSE = 1.5

site = str(input("Digite o nome do site: "))
produto = str(input("Digite o nome do produto: "))

auto.click(x=1375, y=1043)
query = f'site:{site}.com "{produto}" ("gmail.com" OR "hotmail.com") ("(91)" OR "+55")'
auto.sleep(1.5)
auto.write(query)
auto.press('enter')

auto.sleep(2)
auto.hotkey('ctrl', 'a')
auto.hotkey("ctrl", "c")
time.sleep(1)

# Pega o texto copiado para a área de transferência
texto = pyperclip.paste()

# Regex para extração
nome_regex = r"instagram\.com\s*›\s*(?P<nome>[a-zA-Z0-9_.]+)\s*›"
email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
telefone_regex = r"\(?\+?\d{2,3}\)?\s?\d{4,5}-?\d{4}"

nomes = re.findall(nome_regex, texto)
emails = re.findall(email_regex, texto)
telefones = re.findall(telefone_regex, texto)

# Garantir que todas as listas tenham o mesmo tamanho
max_length = max(len(nomes), len(emails), len(telefones))

nomes += [""] * (max_length - len(nomes))
emails += [""] * (max_length - len(emails))
telefones += [""] * (max_length - len(telefones))

# Criar DataFrame
df = pd.DataFrame({
    "Nome": nomes,
    "E-mail": emails,
    "Telefone": telefones
})

# Salvar como Excel
df.to_excel("dados_filtrados.xlsx", index=False)

print("\n✅ Dados salvos em 'dados_filtrados.xlsx'!")


