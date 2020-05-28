# Exporting and importing products

After setup you can export and import products from and to database.  
To make import and export work you have to comment all `MoneyFields` as they are not native `Django` models in file `saleor/product/models.py`.  
Exporting:
```bash
python manage.py export_product_data_to_csv
```

Importing:
```bash
python manage.py import_product_data_from_csv
```
