# poo-grupo7-loja-de-eletronicos

## Tema
Protótipo de terminal em Python criado para validar a estrutura de dados do estoque de uma loja de eletrônicos antes de investir em um sistema completo. Organizado em classes (`Produto`, `Celular`, `Notebook` e `Loja`), o sistema permite cadastrar, listar, buscar itens e calcular seus preços finais conforme o tipo, aplicando desconto à vista para celulares e frete por peso para notebooks.

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


