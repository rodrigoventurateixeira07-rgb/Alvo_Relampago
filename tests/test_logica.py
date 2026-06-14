from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import (
    atualizar_recorde,
    calcular_pontos,
    calcular_tempo_restante,
    clique_acertou_alvo,
    jogador_perdeu,
    jogador_venceu,
    tempo_acabou,
    tomar_dano,
)


def test_calcular_pontos():
    assert calcular_pontos(10, 1) == 11


def test_tomar_dano():
    assert tomar_dano(3, 1) == 2


def test_jogador_perdeu():
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu():
    assert jogador_perdeu(2) is False


def test_jogador_venceu():
    assert jogador_venceu(10, 10) is True


def test_jogador_nao_venceu():
    assert jogador_venceu(5, 10) is False


def test_atualizar_recorde_com_pontuacao_maior():
    assert atualizar_recorde(12, 8) == 12


def test_atualizar_recorde_com_pontuacao_menor():
    assert atualizar_recorde(4, 8) == 8


def test_calcular_tempo_restante():
    assert calcular_tempo_restante(30, 12) == 18


def test_calcular_tempo_restante_nao_fica_negativo():
    assert calcular_tempo_restante(30, 40) == 0


def test_tempo_acabou():
    assert tempo_acabou(0) is True


def test_tempo_nao_acabou():
    assert tempo_acabou(5) is False


def test_clique_acertou_alvo_no_centro():
    assert clique_acertou_alvo((100, 100), (100, 100), 35) is True


def test_clique_errou_alvo():
    assert clique_acertou_alvo((150, 100), (100, 100), 35) is False


def test_salvar_e_carregar_recorde(tmp_path):
    arquivo = tmp_path / "recorde.txt"

    salvar_recorde(arquivo, 15)

    assert carregar_recorde(arquivo) == 15
