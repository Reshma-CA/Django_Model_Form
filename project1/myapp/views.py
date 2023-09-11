from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def index(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyModelForm()

    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')
