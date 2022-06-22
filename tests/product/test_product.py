from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Redmi note 7',
        'Xiaomi',
        '01/03/2019',
        '19/10/2025',
        '19101984',
        'Longe da umidade'
    )

    assert product.id == 1
    assert product.nome_do_produto == 'Redmi note 7'
    assert product.nome_da_empresa == 'Xiaomi'
    assert product.data_de_fabricacao == '01/03/2019'
    assert product.data_de_validade == '19/10/2025'
    assert product.numero_de_serie == '19101984'
    assert product.instrucoes_de_armazenamento == 'Longe da umidade'
