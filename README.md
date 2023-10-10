# Documentação do Conversor de AFND para AFD

Este módulo fornece uma ferramenta que lê um Autômato Finito Não Determinístico (AFND) de um arquivo, converte-o em um Autômato Finito Determinístico (AFD), grava o AFD em outro arquivo e cria gráficos representando ambos os autômatos.

## Funções

### `ler_afnd(caminho_arquivo)`

Lê um AFND de um arquivo.

**Argumentos**:
- `caminho_arquivo`: Caminho do arquivo que contém a descrição do AFND.

**Retorno**:
- Uma tupla contendo:
  - Lista de estados.
  - Estado inicial.
  - Conjunto de estados finais.
  - Lista de transições.

### `escrever_afd(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes)`

Escreve um AFD em um arquivo.

**Argumentos**:
- `caminho_arquivo`: Caminho do arquivo onde o AFD será salvo.
- `estados`: Lista de estados.
- `estado_inicial`: Estado inicial.
- `estados_finais`: Conjunto de estados finais.
- `transicoes`: Lista de transições.

### `afnd_para_afd(estados, estado_inicial, estados_finais, transicoes)`

Converte um AFND para um AFD.

**Argumentos**:
- `estados`: Lista de estados.
- `estado_inicial`: Estado inicial.
- `estados_finais`: Conjunto de estados finais.
- `transicoes`: Lista de transições.

**Retorno**:
- Uma tupla contendo:
  - Lista de estados do AFD.
  - Estado inicial do AFD.
  - Conjunto de estados finais do AFD.
  - Lista de transições do AFD.

### `criar_grafico(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes)`

Cria um gráfico representando o autômato.

**Argumentos**:
- `caminho_arquivo`: Caminho do arquivo onde o gráfico será salvo.
- `estados`: Lista de estados.
- `estado_inicial`: Estado inicial.
- `estados_finais`: Conjunto de estados finais.
- `transicoes`: Lista de transições.

## Uso

1. Realize a instalação da biblioteca `graphviz`:
   - No Linux, execute `sudo apt install graphviz`.
   - No Windows, baixe e instale o [Graphviz](https://graphviz.org/download/).
   - No MacOS, execute `brew install graphviz`.
   - No Google Colab, execute `!apt-get install graphviz`.
   - Depois execute `pip install graphviz`.
2. Prepare um arquivo chamado `entrada.txt` contendo a descrição de um AFND sob o alfabeto `{0, 1}`:
   - A primeira linha deve conter os estados do AFND, separados por espaço.
   - A segunda linha deve conter o estado inicial.
   - A terceira linha deve conter os estados finais, separados por espaço.
   - As linhas seguintes deverão ser as transições, no formato `estado1 simbolo estado2`, onde `simbolo` pode ser um símbolo do alfabeto ou `e` para transição vazia.
3. Execute o script.
4. O AFD será salvo em `saida.txt` e os gráficos serão salvos em `afnd.png` e `afd.png`.

## Exemplo

Dado o AFND em `entrada.txt`:
```
A B C
A
C
A 0 B
B e C
A 1 C
```

Ao executar o script, o AFD em `saida.txt` será:
```
Q0 Q1 Q2 ...
Q0
Q2
Q0 0 Q1
Q0 1 Q2
...
```

E dois gráficos, `afnd` e `afd`, serão gerados, representando visualmente os autômatos.

## Autor
Kevin Ponciano - [kevinponciano](https://github.com/kevin-ponciano)

## Ferramentas Utilizadas
- [Python](https://www.python.org/)
- [Graphviz](https://graphviz.org/)
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
- [ChatGPT-3](https://chat.openai.com/)