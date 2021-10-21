import self as self
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, FormView, DetailView, ListView
from accounts.forms import UserAddForm, UserAddFieldForm
from cars.models import Car


class UserAdd(CreateView):
    model = User
    template_name = 'registration.html'
    success_url = '/accounts/login'
    form_class = UserAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserAddForm()
        context['form2'] = UserAddFieldForm()
        return context


class MyProfile(ListView):
    model = Car
    template_name = 'my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.filter(car_user=self.request.user)
        return context





