from django.conf.urls import url , include
from django.contrib import admin
from . import views
from .filters import  UserFilter
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    url(r'^main$', login_required(views.Main.as_view()), name ='main'),
    url(r'^create$', login_required(views.form_creating), name='blank-create'),
    url(r'^ticket/(?P<pk>\d+)$', login_required(views.MyTicket.as_view()), name='my-ticket'),
    url(r'^search$',  login_required(FilterView.as_view(filterset_class=UserFilter,  template_name = 'search.html')), name ='search'),
    url(r'^edit/(?P<pk>\d+)$', login_required(views.Edit.as_view()), name='edit'),
    url(r'^statusopen$', login_required(views.BlankStatusOpen.as_view()), name='statusopen'),
    url(r'^test/', include('router.urls'))


]