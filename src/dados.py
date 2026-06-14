def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva o recorde em um arquivo de texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo no arquivo."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
