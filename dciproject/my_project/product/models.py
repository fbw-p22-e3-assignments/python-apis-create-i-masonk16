from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_id = models.BigAutoField(primary_key=True)
    product_category = models.CharField(max_length=50)
    product_description = models.TextField(max_length=250)
    product_image_url = models.URLField()
    product_price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product_name
