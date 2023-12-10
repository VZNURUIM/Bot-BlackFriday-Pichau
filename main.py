import pyautogui as bot

escolha = int(input("Digite 1 para pix e 2 para boleto: \n[1] Pix\n[2] Boleto\nResponse: "))

while escolha == 1:
        try:
            image_location = bot.locateOnScreen('compra.png',
                                                confidence=0.7)

            if image_location is not None:
                bot.click(image_location)
                print('Clicked in Compra.')
            else:
                print('Nada encontrado')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location2 = bot.locateOnScreen('finalizar.png',
                                                 confidence=0.7)
            if image_location2 is not None:
                bot.click(image_location2)
                print('Clicked in Finalizar.')
            else:
                print('Nada encontrado.')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location3 = bot.locateOnScreen('continuar.png',
                                                 confidence=0.9)
            if image_location3 is not None:
                bot.click(image_location3)
                print('Clicked in Continuar.')
            else:
                print('Nada encontrado.')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location4 = bot.locateOnScreen('pix.png',
                                                 confidence=0.9)
            if image_location4 is not None:
                bot.click(image_location4)
                print('Clicked in Boleto.')
            else:
                print('Nada encontrado.')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location5 = bot.locateOnScreen('Revisao.png',
                                                 confidence=0.9)
            if image_location5 is not None:
                bot.click(image_location5)
                print('Clicked in Revisao.')
            else:
                print('Nada encontrado.')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location6 = bot.locateOnScreen('Check.png',
                                                 confidence=0.9)
            if image_location6 is not None:
                bot.click(image_location6)
                print('Clicked in Check')
            else:
                print('Nada encontrado')
        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

        try:
            image_location7 = bot.locateOnScreen('agora.png',
                                                 confidence=0.9)
            if image_location7 is not None:
                bot.click(image_location7)
                print("\n\n\n\n\nCreated By VzN!")
                break
            else:
                print('Nada encontrado')

        except bot.ImageNotFoundException:
            print('Imagem Não está na tela!')

while escolha == 2:
    try:
        image_location = bot.locateOnScreen('compra.png',
                                            confidence=0.7)

        if image_location is not None:
            bot.click(image_location)
            print('Clicked in Compra.')
        else:
            print('Nada encontrado')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location2 = bot.locateOnScreen('finalizar.png',
                                             confidence=0.7)
        if image_location2 is not None:
            bot.click(image_location2)
            print('Clicked in Finalizar.')
        else:
            print('Nada encontrado.')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location3 = bot.locateOnScreen('continuar.png',
                                             confidence=0.9)
        if image_location3 is not None:
            bot.click(image_location3)
            print('Clicked in Continuar.')
        else:
            print('Nada encontrado.')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location4 = bot.locateOnScreen('Boleto.png',
                                             confidence=0.9)
        if image_location4 is not None:
            bot.click(image_location4)
            print('Clicked in Boleto.')
        else:
            print('Nada encontrado.')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location5 = bot.locateOnScreen('Revisao.png',
                                             confidence=0.9)
        if image_location5 is not None:
            bot.click(image_location5)
            print('Clicked in Revisao.')
        else:
            print('Nada encontrado.')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location6 = bot.locateOnScreen('Check.png',
                                             confidence=0.9)
        if image_location6 is not None:
            bot.click(image_location6)
            print('Clicked in Check')
        else:
            print('Nada encontrado')
    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')

    try:
        image_location7 = bot.locateOnScreen('agora.png',
                                             confidence=0.9)
        if image_location7 is not None:
            bot.click(image_location7)
            print("\n\n\n\n\nCreated By VzN!")
            break
        else:
            print('Nada encontrado')

    except bot.ImageNotFoundException:
        print('Imagem Não está na tela!')
