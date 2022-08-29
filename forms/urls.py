from django.urls import path
from .views import upload_link_form, key_search, wait_screen, final_result, auto_generator, autoFinalResult, test

urlpatterns = [
    path('', upload_link_form, name="upload_link_form"),
    path('key-search/', key_search, name="key-search"),
    path('wait/', wait_screen, name="wait-screen"),
    path('test/', test, name="test"),
    path('final-result/', final_result, name="final-result"),
    path('auto-generator/', auto_generator, name="auto-generator"),
    path('auto-final-result/', autoFinalResult, name="auto-final-result"),
]
