from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import task

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, 'tasks/index.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))

# class index(ListView):
#     model = User
#     template_name = 'tasks/index.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form':form})



# class AddTask(CreateView):
#     model = task
#     fields = ['title']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(AddTask, self).form_valid(form)

#     def get_success_url(self):
#         return reverse('index')

# class EditTask(UpdateView):
#     model = task
#     fields = ['title']

#     def get_success_url(self):
#         return reverse('index')

# class DeleteTask(DeleteView):
#     model = task
#     # fields = ['title']

#     def get_success_url(self):
#         return reverse('index')

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
