from django.shortcuts import render, redirect
from .forms import CustomerForm

# Create your views here.

def index(request):
    return render(request, 'myassess/index.html')


def register(request):    
    form = CustomerForm(request.POST or None)    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')   
    context = {'form':form}
    return render(request, 'myassess/index.html', context)


    