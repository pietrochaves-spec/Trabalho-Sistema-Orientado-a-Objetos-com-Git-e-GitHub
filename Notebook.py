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


    @property
    def memoria_ram_gb(self):
        """Retorna a memória RAM em GB."""
        return self.__memoria_ram_gb

    @memoria_ram_gb.setter
    def memoria_ram_gb(self, valor):
        """Define a memória RAM, recusando valores menores ou iguais a zero."""
        if valor <= 0:
            raise ValueError("A memória RAM deve ser maior que zero.")
        self.__memoria_ram_gb = valor

    @property
    def peso_kg(self):
        """Retorna o peso do notebook em quilos."""
        return self.__peso_kg

    @peso_kg.setter
    def peso_kg(self, valor):
        """Define o peso, recusando valores menores ou iguais a zero."""
        if valor <= 0:
            raise ValueError("O peso deve ser maior que zero.")
        self.__peso_kg = valor

    def calcular_preco_final(self):
        """Calcula o preço final do notebook, somando o frete por peso.

        Returns:
            float: preço do produto mais o frete.
        """
        return self.preco + self.peso_kg * self.FRETE_POR_KG

    def classificar_desempenho(self):
        """Classifica o desempenho pela memória RAM (método próprio de Notebook).

        Returns:
            str: "Alto desempenho", "Intermediário" ou "Básico".
        """
        if self.memoria_ram_gb >= 16:
            return "Alto desempenho"
        if self.memoria_ram_gb >= 8:
            return "Intermediário"
        return "Básico"

    def __str__(self):
        """Retorna os dados do notebook em texto legível."""
        return (f"{super().__str__()} | Notebook | RAM: {self.memoria_ram_gb} GB | "
                f"Peso: {self.peso_kg} kg | {self.classificar_desempenho()}")
