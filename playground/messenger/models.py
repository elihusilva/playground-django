from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

# Model manager.
class ThreadManager(models.Manager):
    
    # Creación de función personalizada.
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        
        if len(queryset) > 0:
            return queryset[0]
        return None
    
    # Busca si existe un hilo con dos usuarios, en caso contrario, lo crea.
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)

        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


# Hilo que relaciona los mensajes enviados entre dos usuarios.
class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ThreadManager()

    class Meta:
        ordering = ['-updated_at']

# Conexión de una señal con cualquier cambio en la relacion ManyToMany.
def messages_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    print(instance, action, pk_set)
    false_pk_set = set()
    
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            
            # Si el usuario del mensaje no se encuentra dentro de los usuarios de la instancia del hilo.
            if msg.user not in instance.users.all():
                print('{}, no forma parte de está conversación.'.format(msg.user))
                false_pk_set.add(msg_pk)
    
    # Buscar los comentarios de false_pk_set que sí están en pk_set y se eliminan de pk_set.
    pk_set.difference_update(false_pk_set)

    # Forzar actualización para colocar primero la conversación con un último mensaje.
    instance.save()

m2m_changed.connect(messages_changed, sender=Thread.messages.through)