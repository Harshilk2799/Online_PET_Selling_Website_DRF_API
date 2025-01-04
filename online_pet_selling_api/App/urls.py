from django.urls import path
from App import views

urlpatterns = [
    path("animal/", views.AnimalAPI.as_view()),
    path("animal/<pk>/", views.AnimalDetailAPI.as_view()),
    path("register/", views.RegistrationAPI.as_view()),
    path("login/", views.LoginAPI.as_view()),
    path("create_animal/", views.AnimalCreateAPI.as_view()),
    path("create_animal/<uuid:pk>/", views.AnimalCreateAPI.as_view())
]
