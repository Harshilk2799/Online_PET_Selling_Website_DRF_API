from rest_framework import serializers
from django.contrib.auth.models import User
from App.models import Animal, AnimalBreed, AnimalColor, AnimalImages, AnimalLocation, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ["category_name"]

class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        # fields = "__all__"
        fields = ["animal_breed"]

class AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalColor
        # fields = "__all__"
        fields = ["animal_color"]


class AnimalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocation
        # fields = "__all__"
        fields = ["animal_location"]

class AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImages
        # fields = "__all__"
        fields = ["animal_image"]

class AnimalSerializer(serializers.ModelSerializer):
    animal_category = CategorySerializer()
    animal_breed = AnimalBreedSerializer(many=True)
    animal_color = AnimalColorSerializer(many=True)

    class Meta:
        model = Animal
        exclude = ["updated_at"]

    def create(self, validated_data):
        print(validated_data)
        animal_color = validated_data.pop("animal_color")
        print("Animal Color: ", animal_color)

        animal_breed = validated_data.pop("animal_breed")
        print("Animal Breed: ", animal_breed)

        animal_category = validated_data.pop("animal_category")
        print("Animal Category: ", animal_category)

        category, _ = Category.objects.get_or_create(category_name=animal_category["category_name"])
        print("Category : ", category)
        
        animal = Animal.objects.create(**validated_data, animal_category=category)

        for breed in animal_breed:
            print("Breed: ", breed)
            animal_breed_obj, _ = AnimalBreed.objects.get_or_create(animal_breed=breed["animal_breed"])
            animal.animal_breed.add(animal_breed_obj)

        for color in animal_color:
            print("Color: ", color)
            animal_color_obj, _ = AnimalColor.objects.get_or_create(animal_color=color["animal_color"])
            animal.animal_color.add(animal_color_obj)

        return animal

    def update(self, instance, validated_data):
        print("Instance: ", instance)
        print("Validated Data: ", validated_data)

        if "animal_breed" in validated_data:
            print(instance.animal_breed)
            animal_breed = validated_data.pop("animal_breed")
            instance.animal_breed.clear()
            for breed in animal_breed:
                print("Breed: ", breed)
                animal_breed_obj, _ = AnimalBreed.objects.get_or_create(animal_breed=breed["animal_breed"])
                instance.animal_breed.add(animal_breed_obj)


        if "animal_color" in validated_data:
            print(instance.animal_color)
            animal_color = validated_data.pop("animal_color")
            instance.animal_color.clear()
            for color in animal_color:
                print("Color: ", color)
                animal_color_obj, _ = AnimalColor.objects.get_or_create(animal_color=color["animal_color"])
                instance.animal_color.add(animal_color_obj)


        instance.animal_name = validated_data.get("animal_name", instance.animal_name)
        instance.animal_description = validated_data.get("animal_description", instance.animal_description)
        instance.animal_gender = validated_data.get("animal_gender", instance.animal_gender)
        instance.save()
        return instance

# class AnimalSerializer(serializers.ModelSerializer):
#     # First Way
#     # animal_category = CategorySerializer()


#     animal_category = CategorySerializer()
#     # ManyToManyField (Second Way)
#     animal_breed = AnimalBreedSerializer(many=True)
#     animal_color = AnimalColorSerializer(many=True)
#     # ForeignKey
#     images = AnimalImagesSerializer(many=True)
#     location = AnimalLocationSerializer(many=True)

#     class Meta:
#         model = Animal
#         exclude = ["updated_at"]

    # Second Way
    # animal_category = serializers.SerializerMethodField()
    # def get_animal_category(self, obj):
    #     return obj.animal_category.category_name

    # Third Way
    # def to_representation(self, instance):
    #     payload = {
    #         "animal_category": instance.animal_category.category_name,
    #         "animal_views": instance.animal_views,
    #         "animal_likes": instance.animal_likes,
    #         "animal_name": instance.animal_name,
    #         "animal_description": instance.animal_description,
    #         "animal_gender": instance.animal_gender,

    #         # First Way
    #         # ManyToManyField
    #         # "animal_breed": AnimalBreedSerializer(instance.animal_breed.all(), many=True).data,
    #         # "animal_color": AnimalColorSerializer(instance.animal_color.all(), many=True).data
    #     }
    #     return payload

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        
        if "username" in attrs:
            user = User.objects.filter(username=attrs["username"])
            if user.exists():
                raise serializers.ValidationError("Username is already taken!")
            
        if "email" in attrs:
            user = User.objects.filter(email=attrs["email"])
            if user.exists():
                raise serializers.ValidationError("Emali is already taken!")
            
        return attrs

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        
        if "username" in attrs:
            user = User.objects.filter(username=attrs["username"])
            if not user.exists():
                raise serializers.ValidationError("Username does not exists!")
            
        return attrs


