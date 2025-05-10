from django.db import models

class SaleItem(models.Model): # Товар на продажу
    name = models.CharField(max_length=100) # Название товара
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена товара
    quantity = models.IntegerField() # Количество товара в наличии
    description = models.TextField() # Описание товара
    image_url = models.TextField() # URL изображения товара