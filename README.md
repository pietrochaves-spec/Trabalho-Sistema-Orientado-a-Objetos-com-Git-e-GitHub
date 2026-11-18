# poo-grupo7-loja-de-eletronicos

## Tema
Protótipo de terminal em Python criado para validar a estrutura de dados do estoque de uma loja de eletrônicos antes de investir em um sistema completo. Organizado em classes (`Produto`, `Celular`, `notebook.py` e `Loja`), o sistema permite cadastrar, listar, buscar itens e calcular seus preços finais conforme o tipo, aplicando desconto à vista para celulares e frete por peso para notebooks.


## Integrantes
- Pedro Rogério
- Alison Waldmann
- Pietro Chaves
- João Neja


## Descrição das Classes
- **Produto** (produto.py): Classe base com atributos privados validados via @property (código, nome não vazio, preço maior que zero e estoque não negativo). Define o método calcular_preco_final(), retornando o preço original.

- **Celular** (celular.py): Herda de Produto, adicionando armazenamento, suporte a 5G e o método calcular_parcela(). Sobrescreve o cálculo de preço final aplicando 5% de desconto à vista.

- **Notebook** (notebook.py): Herda de Produto, adicionando memória RAM, peso e o método classificar_desempenho(). Sobrescreve o cálculo de preço final somando frete de R$ 15,00 por kg.

- **Loja** (loja.py): Classe gerenciadora do catálogo, responsável por cadastrar, listar, buscar itens (por código ou nome) e aplicar o polimorfismo ao calcular o preço final de diferentes tipos de produtos em conjunto.


## Diagrama de classes


                          +------------------------------+
                          |             Loja             |
                          +------------------------------+
                          | - __nome                     |
                          | - __produtos : list          |
                          | - __proximo_codigo           |
                          +------------------------------+
                          | + cadastrar_produto()        |
                          | + listar_produtos()          |
                          | + buscar_produto()           |
                          | + calcular_precos_finais()   |
                          | + __str__()                  |
                          +------------------------------+
                                          <> 1
                                          |
                                          | 0..*
                          +------------------------------+
                          |           Produto            |
                          +------------------------------+
                          | - __codigo                   |
                          | - __nome                     |
                          | - __preco                    |
                          | - __estoque                  |
                          +------------------------------+
                          | + calcular_preco_final()     |
                          | + __str__()                  |
                          +------------------------------+
                                          ^
                                          |
                        +-----------------+-----------------+
                        |                                   |
        +------------------------------+    +------------------------------+
        |           Celular            |    |           Notebook           |
        +------------------------------+    +------------------------------+
        | - __armazenamento_gb         |    | - __memoria_ram_gb           |
        | - __possui_5g                |    | - __peso_kg                  |
        +------------------------------+    +------------------------------+
        | + calcular_preco_final()     |    | + calcular_preco_final()     |
        | + calcular_parcela()         |    | + classificar_desempenho()   |
        | + __str__()                  |    | + __str__()                  |
        +------------------------------+    +------------------------------+


Legenda: ^ indica herança (Celular e Notebook herdam de Produto) e <>
indica que a Loja guarda uma lista com vários Produto (1 para 0..*).


## Como executar
(O programa usa apenas a biblioteca padrão do Python, então não é preciso instalar nada além do próprio Python.)


- Instale o Python 3.10 ou superior (confira com python --version).
- Clone o repositório: git clone <link-do-repositorio>
- Entre na pasta do projeto: cd loja-eletronicos
- Execute o programa: python main.py (em Linux ou Mac, use python3 main.py)

Use o menu da loja digitando o número da opção desejada:
- 1: cadastrar celular
- 2: cadastrar notebook
- 3: listar produtos
- 4: buscar produto por código ou parte do nome
- 5: calcular o preço final de cada produto (polimorfismo)
- 0: sair
Para executar pelo PyCharm, abra a pasta do projeto, abra o arquivo main.py e clique em Run.

Os arquivos produto.py, celular.py, notebook.py e loja.py precisam ficar na mesma pasta do main.py.


## Estrutura de arquivos
- **celular.py** → Alison Waldmann
- **loja.py** → João Neja
- **notebook.py** → Pietro Chaves
- **produto.py** → Pedro Rogério
- **main.py** → Pedro Rogério