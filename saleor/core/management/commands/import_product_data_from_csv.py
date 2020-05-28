import os

from django.core.management.base import BaseCommand

from ....product.models import (
    AssignedProductAttribute,
    AssignedVariantAttribute,
    Attribute,
    AttributeProduct,
    AttributeTranslation,
    AttributeValue,
    AttributeValueTranslation,
    AttributeVariant,
    Category,
    CategoryTranslation,
    Collection,
    CollectionProduct,
    DigitalContent,
    DigitalContentUrl,
    Product,
    ProductImage,
    ProductTranslation,
    ProductType,
    ProductVariant,
    ProductVariantTranslation,
    VariantImage,
)


class Command(BaseCommand):
    help = "Load product related data to database from CSV file."

    def handle(self, *args, **options):
        self.check_dirs()

        models = [
            AssignedProductAttribute,
            AssignedVariantAttribute,
            Attribute,
            AttributeProduct,
            AttributeTranslation,
            AttributeValue,
            AttributeValueTranslation,
            AttributeVariant,
            Category,
            CategoryTranslation,
            Collection,
            CollectionProduct,
            DigitalContent,
            DigitalContentUrl,
            Product,
            ProductImage,
            ProductTranslation,
            ProductType,
            ProductVariant,
            ProductVariantTranslation,
            VariantImage,
        ]

        for model in models:
            self.load_from_backup(model)

    def check_dirs(self):
        if not os.path.exists("backup"):
            os.exit()

    def load_from_backup(self, model):
        model.copy_objects.from_csv(f"./backup/{model.__name__}.csv")
