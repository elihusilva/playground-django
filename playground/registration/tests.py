from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
# Prueba unitaria.
class ProfileTestCase(TestCase):

    # Configuración de datos iniciales para la prueba.
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    # Comprobación si se creó un Perfil para el usuario.
    # Siempre debe iniciar con la palabra test_
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)