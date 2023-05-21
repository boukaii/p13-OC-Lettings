from . import views
from django.contrib import admin
from django.urls import include, path


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    # path('', include('home.urls')),
    path('lettings/', include('Lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

