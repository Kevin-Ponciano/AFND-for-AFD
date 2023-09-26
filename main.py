from graphviz import Digraph


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


# Calcula o fechamento epsilon para um estado
def fechamento_epsilon(transicoes, estados):
    fechamento = {estado: {estado} for estado in estados}

    while True:
        fechamento_atualizado = fechamento.copy()
        for origem, rotulo, destino in transicoes:
            if rotulo == 'ε':
                fechamento_atualizado[origem] |= fechamento[destino]

        if fechamento_atualizado == fechamento:
            break
        else:
            fechamento = fechamento_atualizado

    return fechamento


# Remove movimentos vazios (transições epsilon) do AFND
def remover_movimentos_vazios(estados, estado_inicial, estados_finais, transicoes):
    fechamento = fechamento_epsilon(transicoes, estados)
    novas_transicoes = [
        [origem, rotulo, destino]
        for origem, rotulo, destino in transicoes if rotulo != 'ε'
        for origem in fechamento[origem]
    ]

    novos_estados_finais = {estado for estado in estados if fechamento[estado] & estados_finais}

    return estados, estado_inicial, novos_estados_finais, novas_transicoes


# Converte um AFND para um AFD
def afnd_para_afd(estados, estado_inicial, estados_finais, transicoes):
    transicoes_afd = []

    mapeamento_estados = {frozenset({estado_inicial}): "Q0"}
    novos_estados = [frozenset({estado_inicial})]

    while novos_estados:
        estado_atual = novos_estados.pop()

        for simbolo in '01':
            proximo_estado = {destino for estado in estado_atual for origem, rotulo, destino in transicoes if
                              estado == origem and rotulo == simbolo}
            if proximo_estado:
                proximo_estado_congelado = frozenset(proximo_estado)
                if proximo_estado_congelado not in mapeamento_estados:
                    novos_estados.append(proximo_estado_congelado)
                    mapeamento_estados[proximo_estado_congelado] = f"Q{len(mapeamento_estados)}"

                transicoes_afd.append([mapeamento_estados[estado_atual], simbolo, mapeamento_estados[proximo_estado_congelado]])

    estados_afd = list(mapeamento_estados.values())
    estado_inicial_afd = mapeamento_estados[frozenset({estado_inicial})]
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
    estados, estado_inicial, estados_finais, transicoes = remover_movimentos_vazios(estados, estado_inicial, estados_finais, transicoes)

    estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd = afnd_para_afd(estados, estado_inicial, estados_finais, transicoes)

    escrever_afd('saida.txt', estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd)
    criar_grafico('afnd', estados, estado_inicial, estados_finais, transicoes)
    criar_grafico('afd', estados_afd, estado_inicial_afd, estados_finais_afd, transicoes_afd)
