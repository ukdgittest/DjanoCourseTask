from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel


def my_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_view')
    else:
        form = MyModelForm()
    return render(request, 'form.html', {'form': form})


def data_view(request):
    data = MyModel.objects.all()
    return render(request, 'data.html', {'data': data})


def index_view(request):
    return render(request, 'index.html')
