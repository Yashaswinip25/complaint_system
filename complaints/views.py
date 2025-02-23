from django.shortcuts import render, redirect # type: ignore
from django.urls import reverse_lazy # type: ignore
from .forms import ComplaintForm

def home(request):
    return render(request, 'complaints/home.html')

def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('complaint_success'))
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_file.html', {'form': form})

def complaint_success(request):
    return render(request, 'complaints/success.html')
