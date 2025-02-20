import pyautogui
import time
import logging
from pathlib import Path
from typing import Optional

class AutomationError(Exception):
    """Classe customizada para erros de automação"""
    pass

class LinkedinPostAutomation:
    def __init__(self):
        self.setup_logging()
        self.setup_pyautogui()
        
    def setup_logging(self):
        """Configura o logging com criação automática do diretório"""
        log_dir = Path("log")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%d-%m-%Y - %H:%M:%S",
            filename=log_dir / "main.log",
        )
    
    def setup_pyautogui(self):
        """Configura as configurações de segurança do PyAutoGUI"""
        pyautogui.PAUSE = 0.5  # Pausa entre ações
        pyautogui.FAILSAFE = True  # Permite interromper movendo o mouse para o canto
    
    def locate_and_click(self, image_path: str, confidence: float = 0.9, 
                        max_attempts: int = 3) -> Optional[tuple]:
        """Localiza e clica em uma imagem com tentativas múltiplas"""
        for attempt in range(max_attempts):
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    pyautogui.moveTo(location)
                    pyautogui.click()
                    return location
                time.sleep(1)
            except Exception as e:
                logging.error(f"Erro ao localizar {image_path}: {str(e)}")
        return None

    def open_chrome(self):
        """Abre o navegador Chrome"""
        logging.info("> Navegador - BEGIN")
        try:
            with pyautogui.hold('win'):
                pyautogui.press('a')
            
            if not self.locate_and_click('src/img/BuscaChrome.png'):
                raise AutomationError("Não foi possível encontrar a barra de busca")
            
            pyautogui.write('Chrome')
            
            if not self.locate_and_click('src/img/Chrome.png'):
                raise AutomationError("Não foi possível encontrar o ícone do Chrome")
                
            logging.info("> Navegador - END")
        except Exception as e:
            logging.error(f"Erro ao abrir Chrome: {str(e)}")
            raise

    def open_claude(self):
        """Abre e interage com Claude.ai"""
        logging.info("> Claude - BEGIN")
        try:
            with pyautogui.hold('ctrlleft'):
                pyautogui.press('t')
            
            pyautogui.write('https://claude.ai/new')
            pyautogui.press('enter')
            time.sleep(10)  # Espera página carregar
            
            self.handle_claude_interaction()
            logging.info("> Claude - END")
        except Exception as e:
            logging.error(f"Erro ao interagir com Claude: {str(e)}")
            raise

    def handle_claude_interaction(self):
        """Gerencia a interação com a interface do Claude"""
        prompt = """Bom dia. Baseado nas informacoes que vou passar a seguir, 
        faça uma postagem para a rede social Linkedin utilizando-as. 
        Importante levar em consideracao que precisa ser informativa 
        mas tambem interessante para o publico. Prompt:"""
        
        try:
            if self.locate_and_click('src/img/ChatClaude.png'):
                self.send_prompt(prompt)
            else:
                # Fallback para coordenadas fixas (não recomendado)
                pyautogui.moveTo(x=679, y=368)
                pyautogui.click()
                with pyautogui.hold('ctrlleft'):
                    pyautogui.press('a')
                pyautogui.press('backspace')
                self.send_prompt(prompt)
        except Exception as e:
            logging.error(f"Erro na interação com Claude: {str(e)}")
            raise

    def send_prompt(self, prompt: str):
        """Envia o prompt e o conteúdo do arquivo"""
        try:
            pyautogui.write(prompt)
            with open('src/resume.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                pyautogui.write(content)
            time.sleep(1)
            pyautogui.press('enter')
        except Exception as e:
            logging.error(f"Erro ao enviar prompt: {str(e)}")
            raise

    def get_and_save_result(self):
        """Obtém e salva o resultado"""
        logging.info("> Get Result - BEGIN")
        try:
            time.sleep(10)
            pyautogui.scroll(-20)
            
            if not self.locate_and_click('src/img/GetResult.png'):
                raise AutomationError("Não foi possível localizar o resultado")

            self.save_to_text_editor()
            logging.info("> Get Result - END")
        except Exception as e:
            logging.error(f"Erro ao obter resultado: {str(e)}")
            raise

    def save_to_text_editor(self):
        """Salva o resultado no editor de texto"""
        logging.info("> Paste Result - BEGIN")
        try:
            with pyautogui.hold('win'):
                pyautogui.press('a')
            
            if self.locate_and_click('src/img/BuscaChrome.png'):
                pyautogui.write('Text Editor')
                
                if self.locate_and_click('src/img/TextEditor.png'):
                    with pyautogui.hold('ctrl'):
                        pyautogui.press('v')
                    logging.info("> Paste Result - END")
                else:
                    raise AutomationError("Não foi possível encontrar o Text Editor")
        except Exception as e:
            logging.error(f"Erro ao salvar no editor: {str(e)}")
            raise

def main():
    automation = LinkedinPostAutomation()
    try:
        automation.open_chrome()
        automation.open_claude()
        automation.get_and_save_result()
    except Exception as e:
        logging.error(f"Erro na execução principal: {str(e)}")

if __name__ == "__main__":
    main()