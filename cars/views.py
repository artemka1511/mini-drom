from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, FormView, TemplateView
from cars.models import Car, Brand, Images
from cars.forms import CarAddForm, CarImageAddForm
from django.core.files.base import ContentFile


class CarsListView(ListView):
    template_name = 'main.html'
    model = Car
    context_object_name = 'cars'
    queryset = Car.objects.all()[:7]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.all()
        context['images'] = Images.objects.all()
        return context


class CarAdd(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'car_add.html'
    form_class = CarAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarAddForm()
        context['form2'] = CarImageAddForm()
        return context

    def post(self, request, *args, **kwargs):
        self.upload(request)
        return super().post(request, *args, **kwargs)

    def upload(self, request):
        form = CarAddForm(request.POST, request.user)
        form2 = CarImageAddForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            car = form.save(commit=False)
            car.car_user = request.user
            car.save()
            for f in request.FILES.getlist('image'):
                data = f.read()
                img = Images(car=car)
                img.images.save(f.name, ContentFile(data))
                img.save()
            return redirect(car)


class CarDetailView(DetailView):
    model = Car
    template_name = 'detail_car.html'
    context_object_name = 'detail_car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context
