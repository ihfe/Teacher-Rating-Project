"""TeacherRating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView

from TeacherRating import views
from django.urls import re_path
from django.views import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/profile/',
        TemplateView.as_view(template_name='registration/profile.html'),
        name='profile'),
    path('captcha/', include('captcha.urls')),
    path('check_captcha', views.check_captcha, name='check_captcha'),
    path('panel/', include(('panel.urls', 'panel'), namespace='panel')),
    path('rating/', include(('rating.urls', 'rating'), namespace='rating')),
    path('questionnaire/', include(('questionnaire.urls', 'questionnaire'), namespace='questionnaire')),
    path('admin/', admin.site.urls),
]

urlpatterns += [re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')]
urlpatterns += [re_path(r'^media/(?P<path>.*)$', static.serve, {"document_root": settings.MEDIA_ROOT})]
