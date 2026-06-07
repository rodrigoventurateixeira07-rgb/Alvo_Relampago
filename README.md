# Alvo Relampago

Projeto final da disciplina de Introducao a Algoritmos/Programacao, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Daniel Viana
- Rodrigo
- Luiz Moura
- Mateus Andrade

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicacao.
- `src/`: codigo-fonte principal do jogo.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes.
- `tests/`: testes unitarios com `pytest`.
- `docs/`: documentacao do projeto, incluindo proposta inicial.

## Descricao do jogo

Alvo Relampago e um jogo simples de clique rapido. Um alvo circular aparece em uma posicao aleatoria da tela, e o jogador deve clicar nele para ganhar pontos. Quando o jogador erra o alvo, perde uma vida.

## Objetivo do jogador

O objetivo e acertar o maior numero possivel de alvos antes de perder todas as vidas.

## Regras do jogo

- O jogador comeca com 3 vidas.
- Cada clique correto no alvo aumenta a pontuacao.
- Cada clique fora do alvo remove 1 vida.
- Depois de um acerto, o alvo muda para uma nova posicao aleatoria.
- A partida termina quando as vidas chegam a zero.

## Controles

- Mouse: clicar no alvo.
- Espaco: reiniciar depois do fim da partida.
- ESC: sair do jogo.

## Como executar o projeto

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist minimo para entrega

- Janela do Pygame abre com tamanho 800x600.
- Alvo aparece na tela.
- Mouse interage com o alvo.
- Pontuacao aumenta quando o jogador acerta.
- Vidas diminuem quando o jogador erra.
- Codigo esta organizado em funcoes.
- Proposta inicial esta em `docs/proposta.md`.
- Jogo executa com `python main.py`.
- Testes passam com `python -m pytest`.
