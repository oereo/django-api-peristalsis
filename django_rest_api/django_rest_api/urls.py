from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django_rest_api.global_utils.jwt_token import validate_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path('validate/', validate_jwt_token),
    path('login/', obtain_jwt_token),

    path('verify/', verify_jwt_token),
    path('refresh/', refresh_jwt_token),

    path('user/', include('accounts.urls')),
]
urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)