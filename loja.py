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

    def buscar_produto(self, termo):
        """Busca produtos pelo código exato ou por parte do nome.

        Args:
            termo (str): código ou trecho do nome (sem diferenciar maiúsculas).

        Returns:
            list: produtos encontrados (lista vazia se nenhum for encontrado).
        """
        termo = termo.strip().lower()
        if not termo:
            return []
        encontrados = []
        for produto in self.__produtos:
            if termo == str(produto.codigo) or termo in produto.nome.lower():
                encontrados.append(produto)
        return encontrados

    def calcular_precos_finais(self):
        """Executa a ação polimórfica: calcula o preço final de cada produto.

        Percorre a lista com objetos de tipos diferentes (Celular, Notebook...)
        e chama o mesmo método, calcular_preco_final(). Cada objeto responde
        com a sua própria regra.

        Returns:
            list: tuplas (produto, preço final).
        """
        resultados = []
        for produto in self.__produtos:
            resultados.append((produto, produto.calcular_preco_final()))
        return resultados

    def __str__(self):
        """Retorna o resumo da loja em texto legível."""
        return f"Loja {self.nome} | {len(self.__produtos)} produto(s) cadastrado(s)"