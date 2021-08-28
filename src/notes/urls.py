from django.urls import include, path

from . import views


app_name = "notes"

urlpatterns = [
    path("", views.note_list),
    
    # api
    path("api/", include("notes.api.urls"))
]
