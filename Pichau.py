import keyboard
import pyautogui as bot
from time import sleep as t

def on_key_event(e):
    if e.name == 'k':
        position_comprar = bot.locateOnScreen('Comprar.png', confidence=0.7)

        if position_comprar is not None:
            bot.click(position_comprar)

        t(1.6)
        position_finali = bot.locateOnScreen('Finalizar.png', confidence=0.7)
        if position_finali != None:
            bot.click(position_finali)
            
    elif e.name == 'l':  # Use elif para verificar se a tecla pressionada é 'l' após verificar 'k'
        t(0.4)
        position_continuar = bot.locateOnScreen('Continuar.png', confidence=0.7)

        if position_continuar != None:
            bot.click(position_continuar)
            
        t(.4)

        position_pague = bot.locateOnScreen('Pague.png', confidence=0.7)

        if position_pague != None:
            bot.click(position_pague)
            
        t(1.5)

        position_revisao = bot.locateOnScreen('Revisao.png', confidence=0.7)

        if position_revisao != None:
            bot.click(position_revisao)
            
        t(.3)

        position_termos = bot.locateOnScreen('Termos.png', confidence=0.7)

        if position_termos != None:
            bot.click(position_termos)

        t(.1)

        position_agora = bot.locateOnScreen('Agora.png', confidence=0.7)
        if position_agora != None:
            bot.click(position_agora)

# Registra o manipulador de eventos
keyboard.on_press(on_key_event)

# Mantém o script em execução para que possa detectar as teclas
keyboard.wait('esc')
