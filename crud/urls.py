from django.urls import path
from crud.views import CrudView

urlpatterns = [
    path("crud/", CrudView.as_view(), name="crud_view")
]