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
    help = "Save product related data to CSV from database."

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
            self.create_backup_from_model(model)

    def check_dirs(self):
        if not os.path.exists("backup"):
            os.makedirs("backup")

    def create_backup_from_model(self, model):
        model.copy_objects.to_csv(f"./backup/{model.__name__}.csv")
