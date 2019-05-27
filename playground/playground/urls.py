"""playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from django.conf import settings

urlpatterns = [
    # Paths de la App Core.
    path('', include('core.urls')),

    # Paths de la App Messenger.
    path('', include(messenger_patterns)),

    # Paths de la App Pages.
    path('', include(pages_patterns)),

    # Paths de la App Profiles.
    path('', include(profiles_patterns)),

    # Paths de la App del Administrador.
    path('dashboard/', admin.site.urls),
    
    # Paths de la App Registration.
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('registration.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuraciones en la interfaz del panel de administración.
# Título.
admin.site.site_header = 'Playground'

# Subtitulo.
admin.site.index_title = 'Dashboard'

# Title tag.
admin.site.site_title = 'Playground'