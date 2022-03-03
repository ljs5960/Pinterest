from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name= 'articleapp/list.html'), name= 'list'),
    path('create/', ArticleCreateView.as_view(template_name= 'articleapp/create.html'), name= 'create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(template_name= 'articleapp/detail.html'), name= 'detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(template_name= 'articleapp/update.html'), name= 'update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(template_name= 'articleapp/delete.html'), name= 'delete'),
]
