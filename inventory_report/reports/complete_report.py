from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(product_list):
        simple_report = SimpleReport.generate(product_list)
        list_company_result = list()
        dict_companies = dict()

        for product in product_list:
            if not dict_companies.get(product['nome_da_empresa']):
                dict_companies[product['nome_da_empresa']] = 0
            dict_companies[product['nome_da_empresa']] += 1

        for company in dict_companies:
            list_company_result.append(
              f"- {company}: {dict_companies[company]}\n"
            )

        return (
          f"{simple_report}\n"
          f"Produtos estocados por empresa:\n"
          f"{''.join(list_company_result)}"
        )
