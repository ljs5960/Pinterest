from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from accountapp.decorates import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# function type view
has_ownership = [account_ownership_required, login_required]

@login_required # Django supplying decorator => configure if user is authenticated
def hello_world(request):
    # if request.user.is_authenticated:   # only login user can access
        if request.method == 'POST':
            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))  # def -> reverse
        else:
            hello_world_list = HelloWorld.objects.all()

            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    # else:
    #     return HttpResponseRedirect(reverse('accountapp:login'))


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


@method_decorator(has_ownership, 'get') # Decorator changing function to method
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
