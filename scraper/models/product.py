from dataclasses import dataclass
import csv

@dataclass
class Product:
    name: str
    price: float
    url: str
    selector: str

def read_products_from_csv(file_path: str):
    products = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = Product(
                name=row['name'],
                price=float(row['price']),
                url=row['url'],
                selector=row['selector']
            )
            products.append(product)
    return products

