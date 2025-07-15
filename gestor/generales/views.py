from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

class UserLoginView(FormView):
    """
    Vista de inicio de sesión personalizada que hereda de FormView
    y utiliza el formulario estándar de autenticación.
    """
    template_name = "generales/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")

    # Si ya está autenticado, que no vuelva a ver el login
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    # Autenticamos y hacemos login manualmente
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(self.get_success_url())
    
class HomeView(LoginRequiredMixin, TemplateView):
    """
    Home protegido: solo usuarios autenticados.
    """
    template_name = "generales/homepage.html"
    login_url = "login"   