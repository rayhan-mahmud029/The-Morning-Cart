from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    ProductName = models.CharField(max_length = 50, default="")
    title = models.CharField(max_length = 80)
    category = models.CharField(max_length= 60, default="")
    description = models.TextField(max_length = 150)
    Ratings = models.IntegerField(default=0, verbose_name="Ratings(25, 50, 75, 100)")
    price = models.IntegerField(default=0)
    PublishDate = models.DateField()
    productImage = models.ImageField(upload_to='shop/images/AllProducts', default="")
    

    def __str__(self):
        heading = self.category + " => " + self.ProductName + " ==>  " + str(self.price) + "৳"
        return heading

class HomeBanner(models.Model):
    bannner_id = models.AutoField
    heading = models.CharField(max_length= 50)
    banner_text = models.CharField(max_length=80)
    btn_text = models.CharField(max_length=20)
    cover_image = models.ImageField(upload_to='shop/images/CoverImages', default="")

    def __str__(self):
        heading = str(self.heading) +" => "+ str(self.banner_text)
        return heading

class Sale(models.Model):
    salesProduct_id = models.AutoField
    ProductName = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to = 'shop/images/SalesImage', default="")

    def __str__(self):
        heading = str(self.ProductName) +" => "+ str(self.percentage)
        return heading


class Featured(models.Model):
    featuredProduct_id = models.AutoField
    ProductName = models.CharField(max_length=20)
    category = models.CharField(max_length=20, default='')
    Ratings = models.IntegerField(default=0, verbose_name="Ratings(25, 50, 75, 100)")
    price_now = models.IntegerField(default=0)
    price_before = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to = 'shop/images/FeaturedImage', default="")
    cover_image_2 = models.ImageField(upload_to = 'shop/images/FeaturedImage', default="")

    def __str__(self):
        heading = str(self.ProductName) +" => "+ str(self.price_now) + "৳"
        return heading


