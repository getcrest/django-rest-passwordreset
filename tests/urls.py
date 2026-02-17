""" Tests App URL Config """
from django.urls import include, re_path
from django.contrib import admin


urlpatterns = [
    re_path(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    re_path(r'^admin/', admin.site.urls),
]
