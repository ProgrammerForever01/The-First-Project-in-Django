from django.urls import path
from .views import Homepage,Secondpage
urlpatterns = [
    path('' ,Homepage),
    path('next/', Secondpage)
]