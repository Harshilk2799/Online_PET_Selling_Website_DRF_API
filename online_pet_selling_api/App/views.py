from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import Animal
from App.serializers import AnimalSerializer, RegistrationSerializer, LoginSerializer
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AnimalAPI(APIView):
    def get(self, request):
        queryset = Animal.objects.all()

        # Search Functionality
        if request.GET.get("search"):
            search = request.GET.get("search")
            print("Search: ", search)
            queryset = queryset.filter(
                Q(animal_name__icontains=search) | 
                Q(animal_description__icontains=search) |
                Q(animal_description__icontains=search) |
                Q(animal_gender__iexact=search) |
                Q(animal_breed__animal_breed__icontains=search)|
                Q(animal_color__animal_color__icontains=search)
            )

        serializer = AnimalSerializer(queryset, many=True)
        return Response({
            "status": True,
            "message": "Animal Fetched with GET Method!!!",
            "data": serializer.data
        })
    

class AnimalDetailAPI(APIView):
    def get(self, request, pk=None):
        try:
            queryset = Animal.objects.get(pk=pk)
            queryset.incrementViews()
            serializer = AnimalSerializer(queryset)
            return Response({
                "status": True,
                "message": "Animal Fetched with GET Method!!!",
                "data": serializer.data
            })
        
        except Exception as e:
            return Response({
                "status": False,
                "message": "Something went wrong!!!",
                "data": {}
            })

class RegistrationAPI(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            
            user = User.objects.create(
                username=serializer.data.get("username"),
                email=serializer.data.get("email")
            )
            user.set_password(serializer.data.get("password"))
            user.save()
            return Response({
                "status": True,
                "message": "Account Created!!!",
                "data":serializer.data
            })
        return Response({"status": False, "data":serializer.errors})

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                print("Token: ", token)
                return Response({"status": True, "message": "Login Successfully!!!", "token": token.key})
            else:
                return Response({"status": False, "message":"Username or Password Invalid!!!"})
        return Response({"status":"False", "message":"Something went wrong!", "error": serializer.errors})
    
class AnimalCreateAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":True, "message":"Animal Created!!!", "data": serializer.data})
        return Response({"status": False, "message":"Invalid Data!!!", "data": serializer.errors})
    
    def patch(self, request, pk=None):
        animal_obj = Animal.objects.get(pk=pk)
        serializer = AnimalSerializer(animal_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":True, "message":"Animal Updated!!!", "data": serializer.data})
        return Response({"status": False, "message":"Invalid Data!!!", "data": serializer.errors})
