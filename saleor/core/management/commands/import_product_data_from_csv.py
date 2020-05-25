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
        if not os.path.exists("backup"):
            os.makedirs("backup")

        Category.copy_objects.from_csv("./backup/Category.csv")
        CategoryTranslation.copy_objects.from_csv("./backup/CategoryTranslation.csv")
        ProductType.copy_objects.from_csv("./backup/ProductType.csv")
        Product.copy_objects.from_csv("./backup/Product.csv")
        ProductTranslation.copy_objects.from_csv("./backup/ProductTranslation.csv")
        ProductVariant.copy_objects.from_csv("./backup/ProductVariant.csv")
        ProductVariantTranslation.copy_objects.from_csv(
            "./backup/ProductVariantTranslation.csv"
        )
        DigitalContent.copy_objects.from_csv("./backup/DigitalContent.csv")
        DigitalContentUrl.copy_objects.from_csv("./backup/DigitalContentUrl.csv")
        AssignedProductAttribute.copy_objects.from_csv(
            "./backup/AssignedProductAttribute.csv"
        )
        AssignedVariantAttribute.copy_objects.from_csv(
            "./backup/AssignedVariantAttribute.csv"
        )
        AttributeProduct.copy_objects.from_csv("./backup/AttributeProduct.csv")
        AttributeVariant.copy_objects.from_csv("./backup/AttributeVariant.csv")
        Attribute.copy_objects.from_csv("./backup/Attribute.csv")
        AttributeTranslation.copy_objects.from_csv("./backup/AttributeTranslation.csv")
        AttributeValue.copy_objects.from_csv("./backup/AttributeValue.csv")
        AttributeValueTranslation.copy_objects.from_csv(
            "./backup/AttributeValueTranslation.csv"
        )
        ProductImage.copy_objects.from_csv("./backup/ProductImage.csv")
        VariantImage.copy_objects.from_csv("./backup/VariantImage.csv")
        CollectionProduct.copy_objects.from_csv("./backup/CollectionProduct.csv")
        Collection.copy_objects.from_csv("./backup/Collection.csv")
