# from the current folder import views
from .views import index
# importing path from django.urls
from django.urls import path

# this is the list of the app's views
# if the app has several views then it will have several paths
urlpatterns = [
    path('', index, name='home'),
]