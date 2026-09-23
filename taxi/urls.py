from django.urls import path

from taxi.views import index

app_name = "index"
urlpatterns = [
    path("", index),
]
