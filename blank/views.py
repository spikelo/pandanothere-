from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView , DetailView , UpdateView
from .models import Profile
from .form import ProfileForm
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.



'''         
    Создание форм при помощи класса 
    
class BlankCreate(CreateView):
    model = Profile
    template_name = 'req_create.html'
    fields = '__all__'
    initial = {'date_creating':now} 
                                        '''

class Edit(UpdateView):
    model = Profile
    form_class = ProfileForm
    #form_class = ProfileForm
    template_name = 'edit.html'



class Main(generic.ListView):
    model = Profile
    paginate_by = 15
    template_name = 'main.html'
    def get_queryset(self):
        return Profile.objects.filter(manager=self.request.user)

class BlankStatusOpen(generic.ListView):
    mdodel = Profile
    paginate_by = 15
    template_name = 'blankstatusopen.html'
    def get_queryset(self):
        return Profile.objects.filter(status='Открыта')



class MyTicket(generic.DetailView):
    model = Profile
    template_name = 'ticket.html'



##############################
def form_creating(request):
    profile = Profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.date_creating = form.cleaned_data['date_creating']
            profile.name = form.cleaned_data['name']
            profile.surname = form.cleaned_data['surname']
            profile.patronymic = form.cleaned_data['patronymic']
            profile.home = form.cleaned_data['home']
            profile.flat = form.cleaned_data['flat']
            profile.contact_number = form.cleaned_data['contact_number']
            profile.prefering_connection = form.cleaned_data['prefering_connection']
            profile.tarrif = form.cleaned_data['tarrif']
            profile.address = form.cleaned_data['address']
            profile.status = form.cleaned_data['status']
            profile.manager = request.user
            profile.save()
            return HttpResponseRedirect(reverse('main'))
        else:
            form = ProfileForm(request.POST)
            return render(request, 'req_create.html', {'form':form, 'profile': profile})



    else:
        form = ProfileForm()
        return render(request, 'req_create.html', {'form':form, 'profile': profile})




########################################################################