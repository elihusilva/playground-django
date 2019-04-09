from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/', ProfileUpdate.as_view(), name='settings'),
    path('settings/edit-email/', EmailUpdate.as_view(), name='edit_email')
]