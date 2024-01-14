from django.urls import path
from RuneApp import views

urlpatterns = [
    path('categories', views.showCategories),
    path('createCategory', views.createCategories),
    path('editCategory', views.editCategory),
    path('deleteCategory/<int:id>', views.deleteCategory)
]
