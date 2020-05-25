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
        if not os.path.exists("backup"):
            os.makedirs("backup")

        Category.copy_objects.to_csv("./backup/Category.csv")
        CategoryTranslation.copy_objects.to_csv("./backup/CategoryTranslation.csv")
        ProductType.copy_objects.to_csv("./backup/ProductType.csv")
        Product.copy_objects.to_csv("./backup/Product.csv")
        ProductTranslation.copy_objects.to_csv("./backup/ProductTranslation.csv")
        ProductVariant.copy_objects.to_csv("./backup/ProductVariant.csv")
        ProductVariantTranslation.copy_objects.to_csv(
            "./backup/ProductVariantTranslation.csv"
        )
        DigitalContent.copy_objects.to_csv("./backup/DigitalContent.csv")
        DigitalContentUrl.copy_objects.to_csv("./backup/DigitalContentUrl.csv")
        AssignedProductAttribute.copy_objects.to_csv(
            "./backup/AssignedProductAttribute.csv"
        )
        AssignedVariantAttribute.copy_objects.to_csv(
            "./backup/AssignedVariantAttribute.csv"
        )
        AttributeProduct.copy_objects.to_csv("./backup/AttributeProduct.csv")
        AttributeVariant.copy_objects.to_csv("./backup/AttributeVariant.csv")
        Attribute.copy_objects.to_csv("./backup/Attribute.csv")
        AttributeTranslation.copy_objects.to_csv("./backup/AttributeTranslation.csv")
        AttributeValue.copy_objects.to_csv("./backup/AttributeValue.csv")
        AttributeValueTranslation.copy_objects.to_csv(
            "./backup/AttributeValueTranslation.csv"
        )
        ProductImage.copy_objects.to_csv("./backup/ProductImage.csv")
        VariantImage.copy_objects.to_csv("./backup/VariantImage.csv")
        CollectionProduct.copy_objects.to_csv("./backup/CollectionProduct.csv")
        Collection.copy_objects.to_csv("./backup/Collection.csv")
