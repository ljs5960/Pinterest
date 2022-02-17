from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from accountapp.models import HelloWorld


# function type view
def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # def -> reverse
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


# class type view - Create
class AccountCreateView(CreateView):
    # Django give all lines module
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # class -> reverse_lazy
    template_name = 'accountapp/create.html'