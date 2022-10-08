from django.urls import path
from .api import *
urlpatterns = [
    path("mohadra/<str:session_name>",seesion_api.as_view()),
    path("maoad",scientific_material_api.as_view()),
    path("akhtbar/<str:session_name>",one_akhtbar_material_api.as_view()),
    path("maoad/<str:scientific_material_name>",one_scientific_material_api.as_view())
]