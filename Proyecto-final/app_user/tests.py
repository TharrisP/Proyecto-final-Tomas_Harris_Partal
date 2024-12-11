from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile 
# Create your tests here.

class UserRegistrationTestCase(TestCase):

    def setUp(self):
        """
        Configura cualquier dato necesario para las pruebas.
        """
        self.url = reverse('Registro')

    def test_register_user_with_login(self):
        """
        Verifica que el usuario sea autenticado automáticamente después del registro.
        """
        # Datos de prueba
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@gmail.com',
        }

        response = self.client.post(self.url, data)

        # Verifica que el usuario está autenticado
        user = User.objects.first()
        self.assertEqual(str(self.client.login(username='testuser', password='testpassword123')), 'True')

        # Verifica que el usuario fue redirigido a la página del perfil
        self.assertRedirects(response, reverse('VerPerfil'))

    def test_register_page_status_code(self):
        """
        Verifica que la página de registro se carga correctamente (código de estado 200).
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_register_user_valid(self):
        """
        Verifica que un usuario se registre correctamente con datos válidos.
        """
        # Datos de prueba
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@gmail.com',
        }

        # Realiza la solicitud POST
        response = self.client.post(self.url, data)

        # Verifica que el usuario fue creado
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, 'testuser')

        # Verifica que la redirección ocurrió después del registro
        self.assertRedirects(response, reverse('VerPerfil'))

        # Verifica que el perfil del usuario fue creado
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user, user)


    
