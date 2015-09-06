import os
from django.shortcuts import render
from .utils import search
def home(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        test_file = os.path.join(os.getcwd(),'testfile.csv')
        status = search(test_file, first_name, last_name, phone, address)
        if status:
            message = 'Welcome to the site'
        else:
            message = 'Sorry we don’t recognize you'
        return render(request, 'home.html', {'message':message})
    return render(request, 'home.html')
