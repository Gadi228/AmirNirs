from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

# Create your views here.


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class SectionView(ListView):
    model = Section


class IndexView(DataMixin, ListView):
    model = Section
    template_name = "sport/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Section.objects.filter(is_action=True)


class ViewView(DataMixin, ListView):
    model = Section
    template_name = "sport/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].view),
                                      cat_selected=context['posts'][0].view_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Section.objects.filter(view__slug=self.kwargs['view_slug'], is_action=True)


def About(request):
    contact_list = Section.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sport/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'sport/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'sport/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

class RecordsView(DataMixin, ListView):
    model = Section

def saveorder(request):
    quant = request.POST['quantity']
    prod = request.POST['prod']
    order = request.user.orders_set.order_by('-date').last()
    if not order:
        order = Records.objects.create(user=request.user)
    if order.is_paid:
        order = Records.objects.create(user=request.user)

    return redirect('detail', item_slug=prod)


def payment(request):
    ord = request.user.orders_set.last()
    ord.is_paid = True
    ord.is_took = True
    ord.save()
    return redirect('home')