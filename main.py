import subprocess
from datetime import datetime, date

DATE = date.today()
FILE = f'post{DATE}.txt'

print()
print("> Qual o assunto do dia?")
prompt = """
    Bom dia.
    Baseado nas informações que vou passar a seguir, faça uma postagem para a rede social Linkedin utilizando-as.
    É importante levar em consideração que precisa ser informativa mas também interessante para o público.
    A sua resposta pode ser utilizando o idioma que você tem maior conhecimento.
    Imformação:
"""
prompt = input("")
print()

result = subprocess.run(['ollama', 'run', 'deepseek-r1:14b', prompt],
                        capture_output=True,
                        text=True
                        )

try:
    with open(FILE, 'w') as f:
        f.write(result.stdout)
    print(f"> Finish.")
    print()
except Exception as e:
    print(f"> Something wrong. - {e}")
    print()