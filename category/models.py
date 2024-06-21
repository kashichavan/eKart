from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=25)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cat_image=models.ImageField(upload_to='photos/categories',blank=True)

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])
