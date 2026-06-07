def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos a pontuacao atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantem um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def clique_acertou_alvo(posicao_clique, posicao_alvo, raio_alvo):
    """Verifica se uma posicao clicada esta dentro do circulo do alvo."""
    distancia_x = posicao_clique[0] - posicao_alvo[0]
    distancia_y = posicao_clique[1] - posicao_alvo[1]
    distancia_quadrada = distancia_x**2 + distancia_y**2

    return distancia_quadrada <= raio_alvo**2


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposicao entre dois retangulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)
