"""Módulo da classe Celular, filha de Produto."""

from produto import Produto


class Celular(Produto):
    """Representa um celular à venda na loja.

    Além dos dados de Produto, guarda a capacidade de armazenamento
    e se o aparelho tem suporte a 5G.
    """

    DESCONTO_A_VISTA = 0.05  # 5% de desconto no preço final

    def __init__(self, codigo, nome, preco, estoque, armazenamento_gb, possui_5g):
        """Cria um celular.

        Args:
            codigo (int): identificador único do produto.
            nome (str): modelo do celular.
            preco (float): preço de venda.
            estoque (int): quantidade em estoque.
            armazenamento_gb (int): armazenamento interno em GB (maior que zero).
            possui_5g (bool): True se o aparelho tem suporte a 5G.
        """
        super().__init__(codigo, nome, preco, estoque)
        self.armazenamento_gb = armazenamento_gb
        self.possui_5g = possui_5g