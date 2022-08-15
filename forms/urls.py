from django.urls import path
from .views import upload_link_form

urlpatterns = [
    path('', upload_link_form, name="upload_link_form"),
]
