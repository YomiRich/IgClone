from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.

class CategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.Fashion= Category(category='Fashion')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Fashion,Category))
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_save_method(self):
        self.Fashion.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
        
    #Testing save method
    def test_save_method(self):
        self.Fashion.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)  

    #Testing save multiple
    def test_save_multiple_categories(self):
        self.Fashion.save_category()

        test_Fashion=Category(category_name='Fashion')
        test_Fashion.save_category()

        categories=Category.objects.all()
        self.assertEqual(len(categories),2)


    #Testiing delete method
    def test_delete_method(self):
        self.Fashion.save_category()

        test_Fashion=Category(category_name='Fashion')
        test_Fashion.save_category()

        test_Fashio.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),1)   
    
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.Santorini=Location(location='Santorini')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Santorini,Location))
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_method(self):
        self.Santorini.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)
    
    def test_delete_method(self):
        self.Santorini.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)   
        test_Santorini=Location(location_name='Santorini')
        test_Santorini.save_location()

        test_Santorini.delete_location()
        locations=Location.objects.all()
        self.assertEqual(len(location),1)
        
    #Testing save multiple
    def test_save_multiple_locations(self):
        self.Santorini.save_locations()

        test_Santorini=Location(location_name='Santorini')
        test_Santorini.save_locations()

        locations=Location.objects.all()
        self.assertEqual(len(locations,2)
        
class ImageTestClass(TestCase):
    
    def setUp(self):
        self.test_category = Category(category=list('Fashion'))
        self.test_category.save_category()

        self.location = Location(location="Santorini")
        self.location.save_location()

        self.image = Image(id=1,image_name="Greece",image_description="Number one tourist destination",category=self.test_category,location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()    
        
    def test_get_photos(self):
        photos=Image.get_photos()
        self.assertTrue(len(photos)>0)

    
        
