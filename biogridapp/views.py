from django.shortcuts import render, redirect, get_object_or_404
from .models import Biography
from .forms import BiographyForm

def home(request):
    bios = Biography.objects.order_by('name')
    return render(request, 'biogridapp/home_db.html', {'bios': bios})

def add_bio(request):
    if request.method == 'POST':
        form = BiographyForm(request.POST, request.FILES)  # 👈 IMPORTANTÍSIMO request.FILES
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BiographyForm()
    return render(request, 'biogridapp/add_bio.html', {'form': form})

def delete_bio(request, id):
    bio = get_object_or_404(Biography, id=id)
    if request.method == 'POST':
        bio.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'bio': bio})