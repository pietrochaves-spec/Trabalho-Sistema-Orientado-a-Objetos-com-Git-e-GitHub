"""Módulo da classe Notebook, filha de Produto."""

from produto import Produto


class Notebook(Produto):
    """Representa um notebook à venda na loja.

    Além dos dados de Produto, guarda a memória RAM e o peso do aparelho.
    """

    FRETE_POR_KG = 15.0  # valor do frete cobrado por quilo

    def __init__(self, codigo, nome, preco, estoque, memoria_ram_gb, peso_kg):
        """Cria um notebook.

        Args:
            codigo (int): identificador único do produto.
            nome (str): modelo do notebook.
            preco (float): preço de venda.
            estoque (int): quantidade em estoque.
            memoria_ram_gb (int): memória RAM em GB (maior que zero).
            peso_kg (float): peso em quilos (maior que zero).
        """
        super().__init__(codigo, nome, preco, estoque)
        self.memoria_ram_gb = memoria_ram_gb
        self.peso_kg = peso_kg