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