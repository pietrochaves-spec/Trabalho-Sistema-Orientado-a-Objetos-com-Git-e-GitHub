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

        @property
        def armazenamento_gb(self):
            """Retorna o armazenamento interno em GB."""
            return self.__armazenamento_gb

        @armazenamento_gb.setter
        def armazenamento_gb(self, valor):
            """Define o armazenamento, recusando valores menores ou iguais a zero."""
            if valor <= 0:
                raise ValueError("O armazenamento deve ser maior que zero.")
            self.__armazenamento_gb = valor

        @property
        def possui_5g(self):
            """Retorna True se o celular tem suporte a 5G."""
            return self.__possui_5g

        @possui_5g.setter
        def possui_5g(self, valor):
            """Define o suporte a 5G, aceitando apenas True ou False."""
            if not isinstance(valor, bool):
                raise ValueError("O suporte a 5G deve ser verdadeiro ou falso.")
            self.__possui_5g = valor

        def calcular_preco_final(self):
            """Calcula o preço final do celular, com 5% de desconto à vista.

            Returns:
                float: preço com desconto aplicado.
            """
            return self.preco * (1 - self.DESCONTO_A_VISTA)

        def calcular_parcela(self, numero_parcelas):
            """Calcula o valor de cada parcela sem juros (método próprio de Celular).

            Args:
                numero_parcelas (int): quantidade de parcelas (maior que zero).

            Returns:
                float: valor de cada parcela.
            """
            if numero_parcelas <= 0:
                raise ValueError("O número de parcelas deve ser maior que zero.")
            return self.preco / numero_parcelas

        def __str__(self):
            """Retorna os dados do celular em texto legível."""
            suporte = "Sim" if self.possui_5g else "Não"
            return (f"{super().__str__()} | Celular | "
                    f"{self.armazenamento_gb} GB | 5G: {suporte}")