from django.urls import path

from {{ project_name }}.core.views import home

app_name = 'core'

urlpatterns = [
    path('', home),
]
