from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorates import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
  model = Profile
  context_object_name = 'target_profile'
  form_class = ProfileCreationForm
  template_name = 'profileapp/create.html'

  def form_valid(self, form): # Client에서의 조작 방지를 위해 Forms에 user 미입력 -> POST하는 user값 user에 입력 후 저장
    temp_profile = form.save(commit=False)
    temp_profile.user = self.request.user
    temp_profile.save()
    return super().form_valid(form)

  def get_success_url(self):  # detail로 가기위한 인자 pk를 싣는 방법
    return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
  model = Profile
  context_object_name = 'target_profile'
  form_class = ProfileCreationForm
  template_name = 'profileapp/update.html'

  def get_success_url(self):
    return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})