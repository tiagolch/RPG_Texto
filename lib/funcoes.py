from random import choice
from time import sleep

from .itens import espadas, escudos, armaduras, pocao_de_vida, pocao_de_mana
from .usuario import usuario, clear
from .inimigos import floresta, caverna, selva, Inimigo


def menu_principal():
    """Função para chamar o menu principal"""
    print('Menu principal')
    print('__________________')
    print('| 1 Novo jogo     |')
    print('| 2 Carregar jogo |')
    print('------------------')
    opcao = input('Digite uma das opções: ').strip(" ").lower()
    clear()

    if opcao in ('novo jogo', '1'):
        print('Novo jogo iniciado!')
        menu_opcoes()

    elif opcao in ('carregar jogo', '2'):
        try:
            usuario.load()
            menu_opcoes()

        except FileNotFoundError:
            print('Arquivo de save não encontrado.')

    else:
        print('Opção inválida.')

    sleep(2)
    menu_principal()


def menu_opcoes():
    """Função para chamar o menu de opções"""
    metodos_usuario = {
        '2' or 'status': usuario.status, 
        '5' or 'equips': usuario.equips, 
        '6' or 'inventario': usuario.invent,
        '3' or 'salvar': usuario.save
    }

    print('Menu de opções')
    print('_________________________')
    print('| 1 Viajar  4 Descansar  |')
    print('| 2 Status  5 Equips     |')
    print('| 3 Salvar  6 Inventário |')
    print('|           7 Sair       |')
    print('-------------------------')
    opcao = input('Digite uma das opções do menu: ').strip(" ").lower()
    clear()

    if opcao in ('viajar', '1'):
        viajar()

    elif opcao in ('descansar', '4'):
        usuario.vida_atual, usuario.mana_atual = usuario.vida, usuario.mana
        print('Você monta uma tenda para descansar um pouco...')
        print('Descansando, você recupera sua vida e mana!')

    elif opcao in metodos_usuario:
        metodos_usuario.get(opcao)()

    elif opcao in ('sair', '7'):
        print('Programa finalizado.')
        exit()

    else:
        print('Opção inválida')

    sleep(2)
    menu_opcoes()


def viajar():
    """Função para viajar para alguns lugares"""
    # Dicionário de todos lugares com inimigos
    lugares_inimigos = {
        '1' or 'floresta': floresta, 
        '3' or 'caverna': caverna, 
        '4' or 'selva': selva
    }

    print('Locais disponíveis')
    print('_________________________')
    print('| 1 Floresta  3 Caverna  |')
    print('| 2 Vila      4 Selva    |')
    print('|             5 Sair     |')
    print('-------------------------')
    local = input('Digite uma opção, ou sair para voltar ao menu de opções: ').strip(" ").lower()

    if local in lugares_inimigos:
        inimigo = Inimigo(*choice(lugares_inimigos.get(local)))
        usuario.batalha(inimigo)

    elif local in ('vila', '2'):
        vila()

    elif local in ('sair', '5'):
        menu_opcoes()

    else:
        print('Local inválido.')
        sleep(2)

    # Verificando se o usuário subiu de nível
    if usuario.barra_de_xp >= usuario.levelup:
        usuario.lvlup()

    clear()
    viajar()


def vila():
    print('Ao entrar na vila, você vê diversas tavernas e lojas')
    print('________________________')
    print('| 1 Apotecário  3 Sair  |')
    print('| 2 Ferreiro            |')
    print('------------------------')
    local = input('Digite uma das opções, ou sair: ').strip(" ").lower()

    if local in ('apotecario', 'apotecário', '1'):
        apotecario()

    elif local in ('ferreiro', '2'):
        ferreiro()     

    elif local in ('sair', '3'):
        viajar()

    else:
        print('Opção inválida')
        sleep(2)

    clear()
    vila()


def apotecario():
    dinheiro = str(usuario.dinheiro).ljust(4)
    print('Apotecário')
    print('_____________________________')
    print('| 1 Poção de vida  Preço: 10 |')
    print('| 2 Poção de mana  Preço: 10 |')
    print('| 3 Sair                     |')
    print('|                            |')
    print(f'| Dinheiro: {dinheiro}             |')
    print('-----------------------------')
    escolha = input('Digite o nome de uma das poções, ou sair: ')

    if escolha.strip(" ").lower() in pocao_de_vida[0]:
        usuario.compra_item(escolha, pocao_de_vida)

    elif escolha.strip(" ").lower() in pocao_de_mana[0]:
        usuario.compra_item(escolha, pocao_de_mana)

    elif escolha.strip(" ").lower() in ('sair', '3'):
        vila()

    else:
        print('Opção inválida.')

    sleep(2)
    clear()
    apotecario()


def ferreiro():
    tipos_equipamentos = {
        '1' or 'espadas': espadas, 
        '2' or 'escudos': escudos, 
        '3' or 'armaduras': armaduras
    }

    dinheiro = str(usuario.dinheiro).ljust(4)
    print('Ferreiro')
    print('______________')
    print('| 1 Espadas   |')
    print('| 2 Escudos   |')
    print('| 3 Armaduras |')
    print('| 4 Sair      |')
    print('--------------')
    escolha = input('Digite uma das opções, ou sair: ').strip(" ").lower()

    if escolha in tipos_equipamentos:
        equipamentos = tipos_equipamentos.get(escolha)
        print('_____________________________________________')
        for equipamento in equipamentos:
            print(f'| {equipamento[0].ljust(20)} Dano: {equipamento[1]}   Preço: {equipamento[2].ljust(3)} |')
        print('|                                           |')
        print(f'| Dinheiro: {dinheiro}                            |')
        print('---------------------------------------------')
        equip_esc = input(f'Digite o nome de um(a) dos(as) {escolha}: ').strip(" ").lower()
        usuario.compra_equip(equip_esc, equipamentos)

    elif escolha in ('sair', '4'):
        vila()

    else:
        print('Opção inválida.')

    sleep(2)
    clear()
    ferreiro()
