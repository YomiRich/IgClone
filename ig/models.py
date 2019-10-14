from django.db import models

# Q objects to search for multiple terms
from django.db.models import Q


# Create your models here.
class Caption (models.Model):
    caption = models.CharField(max_length =30)
    def __str__(self):
        return self.caption
    
    def save_caption(self):
        self.save()
        
class Profile (models.Model):
    profile_photo = models.ImageField(upload_to='images/',default='',blank=True)
    bio = models.CharField(max_length =60)
    def __str__(self):
        return self.bio
    
    class Meta:
        ordering = ['profile']
        
    def save_profile_photo(self):
        self.save()
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='',blank=True)
    image_name =models.CharField(max_length =60) 
    image_caption = models.CharField(max_length=255)
    image_profile = models.ForeignKey('Profile',on_delete=models.SET_NULL,null=True)
    likes = 
    comments =
    
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
    def search_by_profile(cls,search_term):
        image = Image.objects.filter(profile__id=search_term).all()
        return image
    
    @classmethod
    def search_by_caption(cls,search_term):
        images = Image.objects.filter(Q(image_profile__profile__icontains=search_term)| Q(image_profile__profile__icontains=search_term) |Q(image_name__icontains=search_term))
        return images
