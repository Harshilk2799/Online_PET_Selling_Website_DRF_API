import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Static Choices
# ANIMAL_CHOICES = (
#     ("Dog", "Dog"),
#     ("Cat", "Cat"),
#     ("Horse", "Horse"),
#     ("Rabbit", "Rabbit"),
# )

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Dynamic Choices
class Category(BaseModel):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class AnimalBreed(BaseModel):
    animal_breed = models.CharField(max_length=255)

    def __str__(self):
        return self.animal_breed    

class AnimalColor(BaseModel):
    animal_color = models.CharField(max_length=25)

    def __str__(self):
        return self.animal_color    

class Animal(BaseModel):
    animal_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="animals")
    # animal_category = models.CharField(max_length=255, choices=ANIMAL_CHOICES)
    animal_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    animal_views = models.IntegerField(default=0)
    animal_likes = models.IntegerField(default=1)
    animal_name = models.CharField(max_length=255)
    animal_description = models.TextField()
    animal_slug = models.SlugField(max_length=255, unique=True)
    animal_gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    animal_breed = models.ManyToManyField(AnimalBreed, blank=True)
    animal_color = models.ManyToManyField(AnimalColor, blank=True)
    
    def save(self, *args, **kwargs):
        uid = str(uuid.uuid4()).split("-")
        self.animal_slug = slugify(self.animal_name) + "-" + uid[0]
        super(Animal, self).save(*args, **kwargs)

    def incrementViews(self):
        self.animal_views += 1
        self.save()

    def incrementLikes(self):
        self.animal_likes += 1
        self.save()

    class Meta:
        ordering = ["animal_name"]

    # def __str__(self):
    #     return self.animal_name    

class AnimalLocation(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="location")
    animal_location = models.CharField(max_length=255)

    def __str__(self):
        return self.animal_location  

class AnimalImages(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="images")
    animal_image = models.ImageField(upload_to="Animals/")
