from django.urls import path

from .views import CustomLoginView, CustomSignupView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('sign_up/',CustomSignupView.as_view(), name='sing_up'),
]