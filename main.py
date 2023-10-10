from graphviz import Digraph

def verificar_palavras_afd(caminho_arquivo_afd, caminho_arquivo_palavras, caminho_arquivo_saida):
    # Lê o AFD do arquivo
    with open(caminho_arquivo_afd, 'r') as arquivo_afd:
        estados_afd = arquivo_afd.readline().strip().split()
        estado_inicial_afd = arquivo_afd.readline().strip()
        estados_finais_afd = set(arquivo_afd.readline().strip().split())
        transicoes_afd = [linha.strip().split() for linha in arquivo_afd]

    # Função para verificar se uma palavra é aceita pelo AFD
    def verificar_palavra(palavra):
        estado_atual = estado_inicial_afd
        for simbolo in palavra:
            proximo_estado = None
            for transicao in transicoes_afd:
                if transicao[0] == estado_atual and transicao[1] == simbolo:
                    proximo_estado = transicao[2]
                    break
            if proximo_estado is None:
                return "não aceito"
            estado_atual = proximo_estado
        if estado_atual in estados_finais_afd:
            return "aceito"
        else:
            return "não aceito"

    # Verifica as palavras e escreve o resultado no arquivo de saída
    with open(caminho_arquivo_palavras, 'r') as arquivo_palavras, open(caminho_arquivo_saida, 'w') as arquivo_saida:
        for palavra in arquivo_palavras:
            palavra = palavra.strip()
            resultado = verificar_palavra(palavra)
            arquivo_saida.write(f"{palavra} {resultado}\n")


# Lê um autômato finito não determinístico (AFND) de um arquivo
def ler_afnd(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        estados = arquivo.readline().strip().split()
        estado_inicial = arquivo.readline().strip()
        estados_finais = set(arquivo.readline().strip().split())
        transicoes = [linha.strip().split() for linha in arquivo]
    return estados, estado_inicial, estados_finais, transicoes


# Escreve um autômato finito determinístico (AFD) em um arquivo
def escrever_afd(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes):
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(' '.join(estados) + '\n')
        arquivo.write(estado_inicial + '\n')
        arquivo.write(' '.join(estados_finais) + '\n')
        for transicao in transicoes:
            arquivo.write(' '.join(transicao) + '\n')


# Converte um AFND para um AFD
def afnd_para_afd(estados, estado_inicial, estados_finais, transicoes):
    transicoes_afd = []

    # Função auxiliar para obter o fechamento epsilon de um conjunto de estados
    def fechamento_epsilon(estado_atual):
        fechamento = set(estado_atual)
        fila = list(estado_atual)

        while fila:
            estado = fila.pop()
            for origem, rotulo, destino in transicoes:
                if estado == origem and rotulo == 'e' and destino not in fechamento:
                    fechamento.add(destino)
                    fila.append(destino)

        return frozenset(fechamento)

    mapeamento_estados = {}  # Usar um dicionário para mapear conjuntos de estados para estados AFD
    novos_estados = [fechamento_epsilon({estado_inicial})]
    mapeamento_estados[novos_estados[0]] = "Q0"

    while novos_estados:
        estado_atual = novos_estados.pop()

        for simbolo in '01':
            proximo_estado = set()

            for estado in estado_atual:
                for origem, rotulo, destino in transicoes:
                    if estado == origem and rotulo == simbolo:
                        proximo_estado.add(destino)

            if proximo_estado:
                fechamento_proximo = fechamento_epsilon(proximo_estado)
                if fechamento_proximo not in mapeamento_estados:
                    novo_estado_afd = f"Q{len(mapeamento_estados)}"
                    mapeamento_estados[fechamento_proximo] = novo_estado_afd
                    novos_estados.append(fechamento_proximo)

                transicoes_afd.append(
                    [mapeamento_estados[estado_atual], simbolo, mapeamento_estados[fechamento_proximo]])

    estados_afd = list(mapeamento_estados.values())
    estado_inicial_afd = mapeamento_estados[fechamento_epsilon({estado_inicial})]
    estados_finais_afd = {mapeamento_estados[estado] for estado in mapeamento_estados if estado & estados_finais}

    return estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd


# Cria um gráfico representando o autômato
def criar_grafico(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes):
    grafico = Digraph()
    for estado in estados:
        grafico.node(estado, shape='doublecircle' if estado in estados_finais else None)
    grafico.node(estado_inicial, color='red')
    for origem, rotulo, destino in transicoes:
        grafico.edge(origem, destino, label=rotulo)
    grafico.render(caminho_arquivo)


# Script principal
if __name__ == "__main__":
    estados, estado_inicial, estados_finais, transicoes = ler_afnd('entrada.txt')

    estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd = afnd_para_afd(estados, estado_inicial,
                                                                                        estados_finais, transicoes)

    escrever_afd('saida.txt', estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd)
    criar_grafico('afnd', estados, estado_inicial, estados_finais, transicoes)
    criar_grafico('afd', estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd)
    verificar_palavras_afd('saida.txt', 'palavras.txt', 'resultado.txt')
