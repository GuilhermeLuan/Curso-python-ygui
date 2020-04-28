# Exercício Python 110
# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.



def dobro(v=0, formato=False):
    """
        -> Realiza o calculo do dobro de um valor específico
        :param v: Valor digitado
        :formato: Parametro para a formatação da moeda
        :return: Retorna o dobro do valor digitado
    """
    res = v * 2
    return res if formato is False else formatacao(res)


def metade(v=0, formato=False):
    """
        -> Realiza o calculo da metade de um valor específico
        :param v: Valor digitado
        :formato: Parametro para a formatação da moeda
        :return: Retorna o valor com sua metade calculada
    """
    res = v / 2
    return res if formato is False else formatacao(res)


def aumentar(v=0, taxa=0, formato=False):
    """
        -> Aumenta o falor em X porcentagem e retorna seu valor
        :param v: Valor digitado
        :param taxa: Porcetagem
        :param formato: Parametro para a formatacão da moeda
        :return: Retorna o valor com o aumento com X porcentagem.
    """
    res = v + (v * taxa/100)
    return res if formato is False else formatacao(res)


def diminuir(v=0, taxa=0, formato=False):
    """
        -> Realiza a reduzão de um valor em X porcentagem
        :param v: Valor digitado
        :param taxa: Porcetagem
        :param formato: Parametro para a formatacão da moeda
        :return: Retorna o valor com a diminuição com X porcentagem.

    """
    res = v - (v * taxa/100)
    return res if formato is False else formatacao(res)


def formatacao(v=0, moeda='R$'):
    """
        -> Realiza formatação do valor passado para dinheiro
        :param v: Valor digitado
        :param moeda: Formatacão da moeda
        :return: Retorna o parâmetro passado em formato de reais (R$)
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')

def resumo(v=0, aumenta=0, diminui=0):
    print(30*'-')
    print(f"{'RESUMO DO VALOR':^30}")
    print(30 * '-')
    print(f'Preço analisado: {formatacao(v):>12}')
    print(f'Dobro do preço: {dobro(v, True):>13}')
    print(f'Metade do preço {metade(v, True):>13}')
    print(f'{aumenta}% de aumento: {aumentar(v, aumenta, True):>13}')
    print(f'{diminui}% de redução: {diminuir(v, diminui, True):>13}')
    print(30 * '-')