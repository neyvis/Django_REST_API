from django.test import TestCase

from main.models import Person


class TestPerson(TestCase):

    def test_create(self):
        p = Person.objects.create(name='Alicia')

        self.assertEqual(p.name, 'Alicia')

    def test_update(self):
        p = Person.objects.create(name='Rose')
        p.name = 'Rosemary'
        p.save()

        self.assertEqual(p.name, 'Rosemary')

    def test_delete(self):
        p = Person.objects.create(name='Ana')
        p_pk = p.pk

        Person.objects.filter(pk=p_pk).delete()

        self.assertFalse(Person.objects.filter(pk=p_pk).exists())
