from django.urls import path
from .views import render_abilitys
app_name = "skill"
urlpatterns = [
    path('', render_abilitys, name='abilitys'),
]
