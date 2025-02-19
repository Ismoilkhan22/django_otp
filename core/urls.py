from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.sing_up, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login", views.sign_in, name="sign-in")
]
