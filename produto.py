"""Módulo da classe base Produto, usada pela loja de eletrônicos."""

class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.__codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque