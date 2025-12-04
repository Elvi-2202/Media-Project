from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView

urlpatterns = [
    path("users", views.users, name="users"),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

