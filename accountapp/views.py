from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# function type view
def hello_world(request):
    if request.user.is_authenticated:   # only login user can access
        if request.method == 'POST':
            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))  # def -> reverse
        else:
            hello_world_list = HelloWorld.objects.all()

            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


# class type view - Create
class AccountCreateView(CreateView):
    # Django give all lines module
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # class -> reverse_lazy
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # Everyone contacts my page can see my info, not their info
    template_name = 'accountapp/detail.html'

    def get(self, *args, **kwargs): # Defining 'get' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:  # Only authenticated user can access to AccountUpdateView
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()  # Django Forbidden response

    def post(self, *args, **kwargs):  # Defining 'post' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs): # Defining 'get' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:  # self == this class
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):  # Defining 'post' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs): # Defining 'get' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:  # self.get_object() returns user.pk
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):  # Defining 'post' function
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()