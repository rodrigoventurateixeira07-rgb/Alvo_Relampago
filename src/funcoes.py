def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos com a pontuacao atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vidas, dano):
    """Tira vidas do jogador."""
    return vidas - dano


def jogador_perdeu(vidas):
    """Verifica se o jogador perdeu todas as vidas."""
    return vidas <= 0


def atualizar_recorde(pontos, recorde):
    """Retorna o maior valor entre a pontuacao atual e o recorde."""
    if pontos > recorde:
        return pontos
    return recorde


def calcular_nivel(pontos):
    """Mostra o nivel do jogador de acordo com a pontuacao."""
    if pontos < 25:
        return "Iniciante"

    if pontos < 50:
        return "Intermediario"

    if pontos < 75:
        return "Excelente"

    if pontos < 100:
        return "Extraordinario"

    return "Deus"


def calcular_tempo_restante(tempo_limite, segundos_passados):
    """Calcula quanto tempo ainda falta para acabar a partida."""
    tempo_restante = tempo_limite - segundos_passados

    if tempo_restante < 0:
        return 0

    return tempo_restante


def tempo_acabou(tempo_restante):
    """Verifica se o tempo chegou a zero."""
    return tempo_restante <= 0


def clique_acertou_alvo(posicao_clique, posicao_alvo, raio_alvo):
    """Verifica se o clique do mouse acertou o alvo circular."""
    clique_x = posicao_clique[0]
    clique_y = posicao_clique[1]
    alvo_x = posicao_alvo[0]
    alvo_y = posicao_alvo[1]

    distancia_x = clique_x - alvo_x
    distancia_y = clique_y - alvo_y
    distancia = (distancia_x**2 + distancia_y**2) ** 0.5

    return distancia <= raio_alvo
