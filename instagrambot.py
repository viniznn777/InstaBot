# Script simples que fica comentando em sorteios do Instagram com pyautogui e webbrowser
import time
import webbrowser
import pyautogui
import datetime

hora = datetime.datetime.now()
cont = 0
# Mensagem de alerta da execução  e confirmação do código
confirmar = pyautogui.confirm('AUTOMATION OF COMMENTS FOR SWEEPSTAKES ON INSTAGRAM (OK TO EXECUTE SCRIPT)', 'INSTAGRAM'
                                                                                                            'BOT',
                              ['Ok', 'Cancel'])
if confirmar == 'Cancel':
    print('\033[31mCÓDIGO NÃO EXECUTADO! FECHANDO SCRIPT...\033[m')
    quit()
elif confirmar == 'Ok':
    print(f'\033[36mEXECUTANDO CÓDIGO AGORA EM: \033[34m{hora.hour}h:{hora.minute}m\033[m', end=' ')
    print(f'\033[36mDATA:\033[m \033[34m{hora.date()}\033[m')
    time.sleep(1)
    while True:
        # Abrir o link do sorteio (Abrirá através do seu navegador padrão)
        webbrowser.open('Link do Sorteio aqui') # Link do sorteio nesta linha
        time.sleep(5)
        carregamento = pyautogui.locateOnScreen('reload.PNG')
        if carregamento:
            time.sleep(6)
        else:
            pass
        # Posição do campo de comentário
        pyautogui.click('CAPTURA.PNG')
        time.sleep(2)
        # Comentário
        pyautogui.write('Eu quero!', interval=0.08) # Comentário a ser escrito no campo
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(5)
        erro = pyautogui.locateOnScreen('erro.png')
        if erro:
            print('\033[31mHOUVE O ERRO DE EXCESSO DE COMENTÁRIOS! AGUARDANDO\033[m \033[34m5min...\033[m')
            time.sleep(300)
        else:
            pass
        time.sleep(3)
        # Fecha a página aberta
        pyautogui.keyDown('ctrl')
        pyautogui.press(['f4'])
        pyautogui.keyUp('ctrl')
        # Contador de quantas vezes o código foi executado
        cont += 1
        print(f'\033[32mCompleto {cont}\033[m')
        time.sleep(5)

# Vinicius Kauã
# Instagram (viniznn.444)