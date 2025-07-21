from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView

urlpatterns = [
    # ── Login (raíz del sitio) ───────────────────────────────────
    path("",auth_views.LoginView.as_view(template_name="generales/login.html"),name="login",),

    # ── Home protegido ──────────────────────────────────────────
    path("home/", HomeView.as_view(), name="home"),

    # ── Logout SOLO por POST (la vista ya lo permite, el truco es usar un <form>) ──
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
