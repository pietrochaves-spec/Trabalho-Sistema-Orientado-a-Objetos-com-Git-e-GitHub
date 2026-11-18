"""Programa principal: menu no terminal da loja de eletrônicos."""

from celular import Celular
from loja import Loja
from notebook import Notebook


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido (ex.: 1999.90).")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Responda com 's' ou 'n'.")


def exibir_menu():
    print("\n===== LOJA DE ELETRÔNICOS =====")
    print("1 - Cadastrar celular")
    print("2 - Cadastrar notebook")
    print("3 - Listar produtos")
    print("4 - Buscar produto")
    print("5 - Calcular preço final (polimorfismo)")
    print("0 - Sair")


def cadastrar_celular(loja):
    print("\n--- Cadastro de celular ---")
    try:
        nome = input("Modelo: ")
        preco = ler_decimal("Preço (R$): ")
        estoque = ler_inteiro("Quantidade em estoque: ")
        armazenamento = ler_inteiro("Armazenamento (GB): ")
        possui_5g = ler_sim_nao("Tem suporte a 5G?")
        celular = Celular(loja.proximo_codigo, nome, preco, estoque,
                          armazenamento, possui_5g)
        loja.cadastrar_produto(celular)
        print("Celular cadastrado com sucesso!")
        print(celular)
    except ValueError as erro:
        print(f"Cadastro cancelado: {erro}")


def cadastrar_notebook(loja):
    print("\n--- Cadastro de notebook ---")
    try:
        nome = input("Modelo: ")
        preco = ler_decimal("Preço (R$): ")
        estoque = ler_inteiro("Quantidade em estoque: ")
        memoria_ram = ler_inteiro("Memória RAM (GB): ")
        peso = ler_decimal("Peso (kg): ")
        notebook = Notebook(loja.proximo_codigo, nome, preco, estoque,
                            memoria_ram, peso)
        loja.cadastrar_produto(notebook)
        print("Notebook cadastrado com sucesso!")
        print(notebook)
    except ValueError as erro:
        print(f"Cadastro cancelado: {erro}")


def listar_produtos(loja):
    print("\n--- Produtos cadastrados ---")
    produtos = loja.listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return
    for produto in produtos:
        print(produto)
    print(f"\n{loja}")


def buscar_produto(loja):
    print("\n--- Buscar produto ---")
    termo = input("Digite o código ou parte do nome: ")
    encontrados = loja.buscar_produto(termo)
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
    print(f"{len(encontrados)} produto(s) encontrado(s):")
    for produto in encontrados:
        print(produto)


def executar_acao_polimorfica(loja):
    print("\n--- Preço final de cada produto ---")
    resultados = loja.calcular_precos_finais()
    if not resultados:
        print("Nenhum produto cadastrado ainda.")
        return
    for produto, preco_final in resultados:
        tipo = type(produto).__name__
        print(f"{tipo:<9} | {produto.nome:<25} | "
              f"Preço: R$ {produto.preco:>9.2f} -> Final: R$ {preco_final:>9.2f}")


def main():
    loja = Loja("TecnoMais")
    opcoes = {
        1: cadastrar_celular,
        2: cadastrar_notebook,
        3: listar_produtos,
        4: buscar_produto,
        5: executar_acao_polimorfica,
    }

    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        if opcao in opcoes:
            opcoes[opcao](loja)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()