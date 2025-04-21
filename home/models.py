from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Diagnosis(models.Model):
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    result = models.TextField()  # e.g., "acne, dry skin"
    recommended_products = models.TextField()  # store product IDs or JSON

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    image_url = models.CharField(max_length=255)
    skin_conditions = models.ManyToManyField('SkinCondition')

class SkinCondition(models.Model):
    name = models.CharField(max_length=100)  # e.g., acne, dry skin, pigmentation
