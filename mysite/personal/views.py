from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
def contact(request):
    return render(request, 'personal/basic.html', {'content': ['contact me:', 'klofseattle@hotmail.com','/ 206)327-7850']})
