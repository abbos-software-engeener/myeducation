import openpyxl

from .models import Product


def more_adding_warehouse_product(order):
    products = []

    file = order.excel_product
    print(file, '123')
    if file is not None:
        sheet = openpyxl.load_workbook(file.path, data_only=True).active
        max_row = sheet.max_row
        for i in range(2, max_row+1):
            products.append(
                Product(
                    product_id=sheet.cell(row=i, column=1).value,
                    name=sheet.cell(row=i, column=2).value,
                    description=sheet.cell(row=i, column=3).value,
                    price=sheet.cell(row=i, column=4).value,
                    tags=sheet.cell(row=i, column=5).value,
                    image_url=sheet.cell(row=i, column=6).value,
                    option_Name=sheet.cell(row=i, column=7).value,
                    hidden=sheet.cell(row=i, column=8).value,
                    weight=sheet.cell(row=i, column=9).value,
                    hidden_btn = sheet.cell(row=i, column=10).value,
                    prepaymentPercent=sheet.cell(row=i, column=11).value,
                    bonusesPercent=sheet.cell(row=i, column=12).value
                )
            )
        print(products)
        Product.objects.bulk_create(products)
    return products[-1] if products else None
