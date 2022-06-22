class SimpleReport:

    def generate(product_list):
        list_companies = list()
        list_manufactures = list()
        list_validity = list()
        for product in product_list:
            list_companies.append(product['nome_da_empresa'])
            list_manufactures.append(product['data_de_fabricacao'])
            list_validity.append(product['data_de_validade'])

        company_more_products = max(
          set(list_companies),
          key=list_companies.count
        )

        return (
                f"Data de fabricação mais antiga: {min(list_manufactures)}\n"
                f"Data de validade mais próxima: {min(list_validity)}\n"
                f"Empresa com mais produtos: {company_more_products}\n"
        )
