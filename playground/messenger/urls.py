from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, create_messenger

messenger_patterns = ([
    path('messages', ThreadList.as_view(), name='messages'),
    path('messages/t/<int:pk>', ThreadDetail.as_view(), name='message'),
    path('messages/add/<int:pk>', add_message, name='add'),
    path('messages/new/<username>', create_messenger, name='new')
], 'messenger')