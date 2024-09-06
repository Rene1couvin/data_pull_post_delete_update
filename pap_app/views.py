from django.shortcuts import render, get_object_or_404, redirect
from .models import DataModel
from .forms import DataForm

def retrieve_data(request):
    data = DataModel.objects.all()
    return render(request, 'index.html', {'data': data})

def upload_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('retrieve_data')
    else:
        form = DataForm()
    return render(request, 'upload.html', {'form': form})

def view_data(request, pk):
    entry = get_object_or_404(DataModel, pk=pk)
    
    return render(request, 'view.html', {'entry': entry})

def update_data(request, pk):
    entry = get_object_or_404(DataModel, pk=pk)
    if request.method == 'POST':        
        form = DataForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('retrieve_data')  
    else:
        form = DataForm(instance=entry)

    return render(request, 'update.html', {'form': form})
def delete_data(request, pk):
    data = get_object_or_404(DataModel, pk=pk)
    data.delete()
    return redirect('retrieve_data')
