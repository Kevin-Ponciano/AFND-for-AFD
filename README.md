# Documentação do Conversor de AFND para AFD

Este módulo fornece uma ferramenta que lê um Autômato Finito Não Determinístico (AFND) de um arquivo, converte-o em um Autômato Finito Determinístico (AFD), grava o AFD em outro arquivo e cria gráficos representando ambos os autômatos.

## Índice
1. [Documentação do Conversor de AFND para AFD](#documentação-do-conversor-de-afnd-para-afd)
2. [Funções](#funções)
   - [ler_afnd(caminho_arquivo)](#ler_afndcaminho_arquivo)
   - [escrever_afd(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes)](#escrever_afdcaminho_arquivo-estados-estado_inicial-estados_finais-transicoes)
   - [afnd_para_afd(estados, estado_inicial, estados_finais, transicoes)](#afnd_para_afdestados-estado_inicial-estados_finais-transicoes)
   - [criar_grafico(caminho_arquivo, estados, estado_inicial, estados_finais, transicoes)](#criar_graficocaminho_arquivo-estados-estado_inicial-estados_finais-transicoes)
   - [verificar_palavras_afd(caminho_arquivo_afd, caminho_arquivo_palavras, caminho_arquivo_saida)](#verificar_palavras_afdcaminho_arquivo_afd-caminho_arquivo_palavras-caminho_arquivo_saida)
3. [Uso](#uso)
4. [Exemplo](#exemplo)
5. [Autor](#autor)
6. [Ferramentas Utilizadas](#ferramentas-utilizadas)

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

### `verificar_palavras_afd(caminho_arquivo_afd, caminho_arquivo_palavras, caminho_arquivo_saida)`

Verifica se palavras são aceitas por um AFD e escreve o resultado em um arquivo.

**Argumentos**:
- `caminho_arquivo_afd`: Caminho do arquivo que contém a descrição do AFD.
- `caminho_arquivo_palavras`: Caminho do arquivo que contém as palavras a serem verificadas.
- `caminho_arquivo_saida`: Caminho do arquivo onde o resultado da verificação será salvo.

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
3. Prepare um arquivo chamado `palavras.txt` contendo as palavras a serem verificadas pelo AFD, uma por linha.
4. Execute o script.
5. O AFD será salvo em `saida.txt` e os gráficos serão salvos em `afnd` e `afd` (os gráficos foram gerados nos arquivos `afnd.pdf` e `afd.pdf`).
6. O resultado da verificação das palavras será salvo em `resultado.txt`, com as palavras seguidas por `aceito` ou `não aceito`.


## Exemplo

Dado o AFND em `entrada.txt`:
```
0 1 2 3 4 5 6 7 8
0
7 8
0 e 1
0 e 2
1 e 3
1 1 4
...
```

Verificação das palavras `palavras.txt`:
```
0100
010101
0110101100
...
```

Ao executar o script, o AFD em `saida.txt` será:
```
Q0 Q1 Q2 Q3 Q4 Q5 ...
Q0
Q9 Q4 Q8 Q6
Q0 0 Q1
Q0 1 Q2
Q2 0 Q3
Q2 1 Q4
...
```

E dois gráficos, `afnd.pdf` e `afd.pdf`, serão gerados, representando visualmente os autômatos.

## Autor
Kevin Ponciano - [kevin-ponciano](https://github.com/kevin-ponciano)
### Co-autores
Luiz Guilherme - [luizrool](https://github.com/Luizrool)

## Ferramentas Utilizadas
- [Python](https://www.python.org/)
- [Graphviz](https://graphviz.org/)
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
- [ChatGPT-3](https://chat.openai.com/)