"""Módulo da classe base Produto, usada pela loja de eletrônicos."""

class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.__codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = valor

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = valor