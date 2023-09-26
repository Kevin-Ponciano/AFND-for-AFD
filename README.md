# Documentação do Conversor de AFND para AFD

Neste módulo, fornecemos uma ferramenta que lê um autômato finito não determinístico (AFND) de um arquivo, converte-o em um autômato finito determinístico (AFD) e, em seguida, grava o AFD em outro arquivo e cria gráficos representando ambos os autômatos.

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

### `fechamento_epsilon(transicoes, estados)`

Calcula o fechamento epsilon para um estado.

**Argumentos**:
- `transicoes`: Lista de transições.
- `estados`: Lista de estados.

**Retorno**:
- Dicionário representando o fechamento epsilon para cada estado.

### `remover_movimentos_vazios(estados, estado_inicial, estados_finais, transicoes)`

Remove transições epsilon do AFND.

**Argumentos**:
- `estados`: Lista de estados.
- `estado_inicial`: Estado inicial.
- `estados_finais`: Conjunto de estados finais.
- `transicoes`: Lista de transições.

**Retorno**:
- Uma tupla contendo:
  - Lista atualizada de estados.
  - Estado inicial atualizado.
  - Conjunto atualizado de estados finais.
  - Lista atualizada de transições.

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

1. Prepare um arquivo contendo a descrição do AFND.
2. Execute o script.
3. O AFD convertido será salvo em `saida.txt` e os gráficos do AFND e AFD serão gerados como `afnd` e `afd`, respectivamente.

## Exemplo

Dado o AFND em `entrada.txt`:
```
A B C
A
C
A 0 B
B ε C
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