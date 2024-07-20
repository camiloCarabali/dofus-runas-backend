from django.test import TestCase, RequestFactory
from RuneApp.models import Category, Characteristic, Rune
from RuneApp.views import showCategories, createCategories, editCategory, deleteCategory, showCharacteristics, \
    createCharacteristics, editCharacteristic, deleteCharacteristic, showRunes, createRunes, editRune, deleteRune


class CategoryViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(Name='Test Category')

    def test_showCategories(self):
        request = self.factory.get('/showCategories/')
        response = showCategories(request)
        self.assertEqual(response.status_code, 200)

    def test_createCategories(self):
        request = self.factory.post('/createCategories/', {'Name': 'New Category'},
                                    content_type='application/json')
        response = createCategories(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.last().Name, 'New Category')

    def test_editCategory(self):
        request = self.factory.put('/editCategory/', {'ID': self.category.ID, 'Name': 'Updated Category'},
                                   content_type='application/json')
        response = editCategory(request)
        self.assertEqual(response.status_code, 200)
        self.category.refresh_from_db()
        self.assertEqual(self.category.Name, 'Updated Category')

    def test_deleteCategory(self):
        request = self.factory.delete('/deleteCategory/' + str(self.category.ID) + '/')
        response = deleteCategory(request, self.category.ID)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Category.objects.filter(ID=self.category.ID).exists())


class CharacteristicViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.characteristic = Characteristic.objects.create(Name='Test Characteristic')

    def test_showCharacteristics(self):
        request = self.factory.get('/showCharacteristics/')
        response = showCharacteristics(request)
        self.assertEqual(response.status_code, 200)

    def test_createCharacteristics(self):
        request = self.factory.post('/createCharacteristics/', {'Name': 'New Characteristic'},
                                    content_type='application/json')
        response = createCharacteristics(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Characteristic.objects.last().Name, 'New Characteristic')

    def test_editCharacteristic(self):
        request = self.factory.put('/editCharacteristic/',
                                   {'ID': self.characteristic.ID, 'Name': 'Updated Characteristic'},
                                   content_type='application/json')
        response = editCharacteristic(request)
        self.assertEqual(response.status_code, 200)
        self.characteristic.refresh_from_db()
        self.assertEqual(self.characteristic.Name, 'Updated Characteristic')

    def test_deleteCharacteristic(self):
        request = self.factory.delete('/deleteCharacteristic/' + str(self.characteristic.ID) + '/')
        response = deleteCharacteristic(request, self.characteristic.ID)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Characteristic.objects.filter(ID=self.characteristic.ID).exists())


class RuneViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.rune = Rune.objects.create(Name='Test Rune')

    def test_showRunes(self):
        request = self.factory.get('/showRunes/')
        response = showRunes(request)
        self.assertEqual(response.status_code, 200)

    def test_createRunes(self):
        request = self.factory.post('/createRunes/', {'Name': 'New Rune'},
                                    content_type='application/json')
        response = createRunes(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Rune.objects.last().Name, 'New Rune')

    def test_editRune(self):
        request = self.factory.put('/editRune/', {'ID': self.rune.ID, 'Name': 'Updated Rune'},
                                   content_type='application/json')
        response = editRune(request)
        self.assertEqual(response.status_code, 200)
        self.rune.refresh_from_db()
        self.assertEqual(self.rune.Name, 'Updated Rune')

    def test_deleteRune(self):
        request = self.factory.delete('/deleteRune/' + str(self.rune.ID) + '/')
        response = deleteRune(request, self.rune.ID)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Rune.objects.filter(ID=self.rune.ID).exists())
