from django.urls import path
from RuneApp import views

urlpatterns = [
    path('categories', views.showCategories),
    path('createCategory', views.createCategories),
    path('editCategory', views.editCategory),
    path('deleteCategory/<int:id>', views.deleteCategory),
    path('characteristics', views.showCharacteristics),
    path('createCharacteristic', views.createCharacteristics),
    path('editCharacteristic', views.editCharacteristic),
    path('deleteCharacteristic/<int:id>', views.deleteCharacteristic),
    path('runes', views.showRunes),
    path('createRune', views.createRunes),
    path('editRune', views.editRune),
    path('deleteRune/<int:id>', views.deleteRune)
]
