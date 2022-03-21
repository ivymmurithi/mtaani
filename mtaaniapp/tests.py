from django.test import TestCase
from .models import *

# Create your tests here.
class NeighboorhoodTestClass(TestCase):

    """
    Test Neighbourhood class methods, delete,save,and if its a class instance
    """

    def setUp(self):
        self.mtaani1= Neighbourhood(mtaani_name='Pazuri',mtaani_location='Pazuri',mtaani_occupants='10')
        self.mtaani1.save_mtaani()

    def test_instance(self):
        self.assertTrue(isinstance(self.mtaani1,Neighbourhood))

    def test_save_method(self):
        self.mtaani1.save_mtaani()
        mtaanis = Neighbourhood.objects.all()
        self.assertTrue(len(mtaanis) > 0)

    def test_delete_method(self):
        self.mtaani1.save_mtaani()
        self.mtaani1.delete_mtaani()
        mtaanis = Neighbourhood.objects.all()
        self.assertTrue(len(mtaanis) -1)

class BusinessTestClass(TestCase):

    """
    Test Business class methods, delete,save,and if its a class instance
    """

    def setUp(self):
        self.business1= Business(business_name='Posho Mill',business_description='We grind all forms of cereals whether for human or animal consumption',business_email='test@gmail.com')
        self.business1.save_business()

    def test_instance(self):
        self.assertTrue(isinstance(self.business1,Business))

    def test_save_method(self):
        self.business1.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business1.save_business()
        self.business1.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) -1)