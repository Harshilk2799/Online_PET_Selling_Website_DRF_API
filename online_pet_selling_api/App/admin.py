from django.contrib import admin
from App.models import Category, Animal, AnimalBreed, AnimalColor, AnimalImages, AnimalLocation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["animal_owner", "animal_category", "animal_views", "animal_likes", "animal_name", "animal_description", "animal_slug", "animal_gender"]

@admin.register(AnimalBreed)
class AnimalBreedAdmin(admin.ModelAdmin):
    list_display = ["animal_breed"]

@admin.register(AnimalColor)
class AnimalColorAdmin(admin.ModelAdmin):
    list_display = ["animal_color"]

@admin.register(AnimalImages)
class AnimalImagesAdmin(admin.ModelAdmin):
    list_display = ["animal", "animal_image"]

@admin.register(AnimalLocation)
class AnimalLocationAdmin(admin.ModelAdmin):
    list_display = ["animal", "animal_location"]