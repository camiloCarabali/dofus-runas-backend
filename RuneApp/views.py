from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from RuneApp.models import Category, Characteristic, Rune
from RuneApp.serializers import CategorySerializer, CharacteristicSerializer, RuneSerializer

# Create your views here.


@csrf_exempt
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def showCategories(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            categories_serializer = CategorySerializer(categories, many=True)
            return JsonResponse(categories_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def createCategories(request):
    if request.method == 'POST':
        try:
            category_data = JSONParser().parse(request)
            name = category_data.get('Name')
            if Category.objects.filter(Name=name).exists():
                return JsonResponse({"error": "A category with this name already exists."})
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()
                return JsonResponse({"message": "Category created successfully!"})
            return JsonResponse({"error": category_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def editCategory(request):
    if request.method == 'PUT':
        try:
            category_data = JSONParser().parse(request)
            category = Category.objects.get(ID=category_data['ID'])
            new_name = category_data.get('Name')
            if category.Name == new_name:
                return JsonResponse({"error": "The new name is the same as the old one."})
            if Category.objects.filter(Name=new_name).exists():
                return JsonResponse({"error": "A category with this name already exists."})
            category_serializer = CategorySerializer(category, data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()
                return JsonResponse({"message": "Category updated successfully!"})
            return JsonResponse({"error": category_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def deleteCategory(request, id):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(ID=id)
            category.delete()
            return JsonResponse({"message": "Category deleted successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def showCharacteristics(request):
    if request.method == 'GET':
        try:
            characteristics = Characteristic.objects.all()
            characteristics_serializer = CharacteristicSerializer(characteristics, many=True)
            return JsonResponse(characteristics_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def createCharacteristics(request):
    if request.method == 'POST':
        try:
            characteristic_data = JSONParser().parse(request)
            name = characteristic_data.get('Name')
            if Characteristic.objects.filter(Name=name).exists():
                return JsonResponse({"error": "A characteristic with this name already exists."})
            characteristic_serializer = CharacteristicSerializer(data=characteristic_data)
            if characteristic_serializer.is_valid():
                characteristic_serializer.save()
                return JsonResponse({"message": "Characteristic created successfully!"})
            return JsonResponse({"error": characteristic_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def editCharacteristic(request):
    if request.method == 'PUT':
        try:
            characteristic_data = JSONParser().parse(request)
            characteristic = Characteristic.objects.get(ID=characteristic_data['ID'])
            new_name = characteristic_data.get('Name')
            if characteristic.Name == new_name:
                return JsonResponse({"error": "The new name is the same as the old one."})
            if Characteristic.objects.filter(Name=new_name).exists():
                return JsonResponse({"error": "A characteristic with this name already exists."})
            characteristic_serializer = CharacteristicSerializer(characteristic, data=characteristic_data)
            if characteristic_serializer.is_valid():
                characteristic_serializer.save()
                return JsonResponse({"message": "Characteristic updated successfully!"})
            return JsonResponse({"error": characteristic_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def deleteCharacteristic(request, id):
    if request.method == 'DELETE':
        try:
            characteristic = Characteristic.objects.get(ID=id)
            characteristic.delete()
            return JsonResponse({"message": "Characteristic deleted successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def showRunes(request):
    if request.method == 'GET':
        try:
            runes = Rune.objects.all()
            runes_serializer = RuneSerializer(runes, many=True)
            return JsonResponse(runes_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def createRunes(request):
    if request.method == 'POST':
        try:
            rune_data = JSONParser().parse(request)
            name = rune_data.get('Name')
            if Rune.objects.filter(Name=name).exists():
                return JsonResponse({"error": "A rune with this name already exists."})
            rune_serializer = RuneSerializer(data=rune_data)
            if rune_serializer.is_valid():
                rune_serializer.save()
                return JsonResponse({"message": "Rune created successfully!"})
            return JsonResponse({"error": rune_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def editRune(request):
    if request.method == 'PUT':
        try:
            rune_data = JSONParser().parse(request)
            rune = Rune.objects.get(ID=rune_data['ID'])
            new_name = rune_data.get('Name')
            if rune.Name == new_name:
                return JsonResponse({"error": "The new name is the same as the old one."})
            if Rune.objects.filter(Name=new_name).exists():
                return JsonResponse({"error": "A rune with this name already exists."})
            rune_serializer = RuneSerializer(rune, data=rune_data)
            if rune_serializer.is_valid():
                rune_serializer.save()
                return JsonResponse({"message": "Rune updated successfully!"})
            return JsonResponse({"error": rune_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def deleteRune(request, id):
    if request.method == 'DELETE':
        try:
            rune = Rune.objects.get(ID=id)
            rune.delete()
            return JsonResponse({"message": "Rune deleted successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

