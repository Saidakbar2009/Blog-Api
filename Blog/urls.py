from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolalarModelViewSet.as_view()),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('maqola/<int:pk>', MaqolaApiView.as_view()),
]
