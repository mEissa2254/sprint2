from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Event
from .form import TicketForm
from .form import UserForm
from .form import PaymentForm
from .form import RegistrationForm

# Create your views here.
def index(request):
    # return HttpResponse('index pages')
    x={'name':'ALI','age':'24'}
    return render(request,'index.html',x)

def about(request):
    # return HttpResponse('about pages')
    return render(request,'about.html')
def events(request):
   return render(request, 'events.html')
def ticket(request):
   form=TicketForm()
   dict_form={
      'form':form
   }
   return render(request, 'ticket.html',dict_form) 
def contact(request):
   return render(request, 'contact.html')
def notification(request):
   messages.success(request, 'This is a success message.')
   return render(request, 'notification.html')
   


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'user.html', {'form': form})

 
   
def payment(request):
   form=PaymentForm()
   dict_form={
      'form':form
   }
   return render(request, 'payment.html',dict_form)
def registraion(request):
   form=RegistrationForm()
   dict_form={
      'form':form
   }
   return render(request, 'registration.html',dict_form)



