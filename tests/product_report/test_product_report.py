from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'Redmi note 7',
        'Xiaomi',
        '01/03/2019',
        '19/10/2025',
        '19101984',
        'longe da umidade'
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa}"
        f" com validade até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
