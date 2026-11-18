"""Módulo da classe gerenciadora Loja."""

from produto import Produto


class Loja:
    """Gerencia a lista de produtos da loja de eletrônicos."""

    def __init__(self, nome):
        """Cria uma loja vazia.

        Args:
            nome (str): nome da loja (não pode ser vazio).
        """
        self.nome = nome
        self.__produtos = []
        self.__proximo_codigo = 1

    @property
    def nome(self):
        """Retorna o nome da loja."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome da loja, recusando nomes vazios."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome da loja não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def produtos(self):
        """Retorna uma cópia da lista de produtos (a original fica protegida)."""
        return list(self.__produtos)

    @property
    def proximo_codigo(self):
        """Retorna o código que será dado ao próximo produto cadastrado."""
        return self.__proximo_codigo

    def cadastrar_produto(self, produto):
        """Adiciona um produto (ou qualquer filho de Produto) à lista da loja.

        Args:
            produto (Produto): objeto a ser cadastrado.

        Raises:
            TypeError: se o objeto não for um Produto.
        """
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível cadastrar objetos do tipo Produto.")
        self.__produtos.append(produto)
        self.__proximo_codigo += 1

    def listar_produtos(self):
        """Retorna a lista com todos os produtos cadastrados."""
        return self.produtos