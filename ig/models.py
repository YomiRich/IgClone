from django.db import models

# Q objects to search for multiple terms
from django.db.models import Q


# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length =30)
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
        
class Location (models.Model):
    location = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location']
        
    def save_location(self):
        self.save()
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='',blank=True)
    image_name =models.CharField(max_length =60) 
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey('Location',on_delete=models.SET_NULL,null=True)
    image_category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image
    
    @classmethod
    def delete_image_by_id(cls,id):
        image = cls.objects.remove(id=id)
        return image
    
    @classmethod
    def update_image_by_id(cls,id):
        image = cls.objects.update(id=id)
        return image
    
    @classmethod
    def search_by_location(cls,search_term):
        image = Image.objects.filter(location__id=search_term).all()
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        images = Image.objects.filter(Q(image_category__category__icontains=search_term)| Q(image_location__location__icontains=search_term) |Q(image_name__icontains=search_term))
        return images
