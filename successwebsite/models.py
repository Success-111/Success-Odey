from django.db import model

class HomeContent(models.Model):
    youtube_vid = models.FileField(upload_to='videos/', null=True)
    epic_moment = models.ImageField(upload_to='epic_moment/', null=True)
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
    

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    photo_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True)
    date_added = models.DateField

    def __str__(sezlf):
        return self.photo_title


class Shop(models.Model):
    shop_items = models.ImageField(upload_to='shop_item/', null=True)
    products_name = models.CharField(max_length=255, null=True)
    products_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.products_name
    

class Tour(models.Model):
    tour_name = models.CharField(max_length=255, null=True)
    date_added = models.DateField(auto_now_add=True, null=True)
    venue = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.tour_name
    
