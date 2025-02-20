import pyautogui
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d-%m-%Y - %H:%M:%S",
    filename="log/main.log",
)

prompt = " Bom dia. Baseado nas informacoes que vou passar a seguir, faça uma postagem para a rede social Linkedin utilizando-as. Importante levar em consideracao que precisa ser informativa mas tambem interessante para o publico. Prompt: "

print('> Utilizando o arquivo RESUME.TXT como base de informação da postagem de hoje.')

def main():

    ###    
    logging.info("> Navegador - BEGIN.")
    with pyautogui.hold('win'):
       pyautogui.press('a')
    
    time.sleep(0.5)
    buscaChrome = pyautogui.locateOnScreen('src/img/BuscaChrome.png', confidence=0.9)
    pyautogui.moveTo(buscaChrome)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.write('Chrome')

    time.sleep(0.5)
    chrom = pyautogui.locateOnScreen('src/img/Chrome.png', confidence=0.9)
    pyautogui.moveTo(chrom)
    pyautogui.click(button='left')
    logging.info("> Navegador - END.")
    ###

    ###
    logging.info("> Claude - BEGIN")
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('t')
    
    time.sleep(0.5)
    pyautogui.write('https://claude.ai/new')
    pyautogui.press('enter')
    time.sleep(10)
    if pyautogui.locateOnScreen('src/img/ChatClaude.png', confidence=0.9):
        chat = pyautogui.locateOnScreen('src/img/ChatClaude.png', confidence=0.9)
        pyautogui.moveTo(chat)
        pyautogui.click(button='left')
        time.sleep(2)
        pyautogui.write(prompt)
        time.sleep(0.3)
        with open('src/resume.txt', 'r') as r:
            pyautogui.write(r.readlines())
        time.sleep(1)    
        pyautogui.press('enter')
    else:
        pyautogui.moveTo(x=679, y=368)
        time.sleep(2)
        pyautogui.click(button='left')
        with pyautogui.hold('ctrlleft'):
            pyautogui.press('a')
        time.sleep(0.5)
        pyautogui.press('backspace')
        time.sleep(0.5)
        pyautogui.write(prompt)
        time.sleep(0.3)
        pyautogui.write(PROMPT)
        time.sleep(1)
        pyautogui.press('enter')
    logging.info("> Claude - END")
    ###

    ###
    logging.info("> Get Result - BEGIN")
    time.sleep(10)
    pyautogui.scroll(-20)
    if pyautogui.locateOnScreen('src/img/GetResult.png', confidence=0.9):
        result = pyautogui.locateOnScreen('src/img/GetResult.png', confidence=0.9)
        pyautogui.moveTo(result)
        time.sleep(0.5)
        pyautogui.click(button='left')
        time.sleep(0.5)
        logging.info("> Get Result - END")
        with pyautogui.hold('win'):
            pyautogui.press('a')
            time.sleep(0.5)
            buscaTextEditor = pyautogui.locateOnScreen('src/img/BuscaChrome.png', confidence=0.9)
            pyautogui.moveTo(buscaTextEditor)
            pyautogui.click(button='left')
            time.sleep(0.5)
            pyautogui.write('Text Editor')
    ###
    logging.info("> Paste Result - BEGIN")
    if pyautogui.locateOnScreen('src/img/TextEditor.png', confidence=0.9):
        textEditor = pyautogui.locateOnScreen('src/img/TextEditor.png', confidence=0.9)
        pyautogui.moveTo(textEditor)
        time.sleep(0.5)
        pyautogui.click(button='left')
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
            logging.info("> Paste Result - END")

if __name__ == "__main__":
    #pass
    main()