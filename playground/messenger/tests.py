from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread

# Create your tests here.
class ThreadTestCase(TestCase):
    
    # Preparación de entorno de pruebas.
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        # Hilo para asignar usuarios y mensajes.
        self.thread = Thread.objects.create()
    
    # Prueba para agregar usuarios a un hilo de conversación.
    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

    # Prueba que recupera hilos existentes de los usuarios.
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        
        # Hilos a donde pertenece determinado usuario.
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])

    # Prueba que recupera hilos donde no pertenecen los usuarios.
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(self.thread.users.all()), 0)
    
    # Prueba para agregar mensajes.
    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content='Holi')
        message2 = Message.objects.create(user=self.user2, content='Holiwis')
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print('{}: {}'.format(message.user, message.content))

    # Prueba donde un usuario que no forma parte de un hilo, puede agregar mensajes.
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content='Hello')
        message2 = Message.objects.create(user=self.user2, content='Seahorse!')
        message3 = Message.objects.create(user=self.user3, content='Incendio')
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)

    # Prueba de Model Manager. Buscará un hilo con el custom manager.
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread)