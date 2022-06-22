import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data_csv(path):
        list_datas = list()
        with open(path, encoding="utf-8") as file:
            datas = csv.DictReader(
              file,
              delimiter=',',
              quotechar='"'
            )
            for data in datas:
                list_datas.append(data)
        return list_datas

    def import_data_json(path):
        with open(path) as file:
            return json.load(file)

    def import_data_xml(path):
        list_datas = list()
        tree = ET.parse(path)
        root = tree.getroot()
        for item in root:
            dict_datas = dict()
            for data in item:
                dict_datas[data.tag] = data.text
            list_datas.append(dict_datas)
        return list_datas

    def file(f):
        split_path = f.split('.')[1]
        if split_path == 'csv':
            return Inventory.import_data_csv(f)

        elif split_path == 'json':
            return Inventory.import_data_json(f)

        elif split_path == 'xml':
            return Inventory.import_data_xml(f)

    def import_data(path, type):
        product_list = Inventory.file(path)

        if type == "simples":
            return SimpleReport.generate(product_list)

        if type == "completo":
            return CompleteReport.generate(product_list)
