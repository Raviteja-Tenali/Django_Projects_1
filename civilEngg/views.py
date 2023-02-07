from django.shortcuts import render
from civilEngg.models import Students
from civilEngg.forms import StudentsModelForm
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def autoCad(request):
    form = StudentsModelForm
    studentforms = {'form': form}

    if request.method=='POST':
        form = StudentsModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)    
    return render(request, 'civilEngg/autoCad.html',studentforms)

def totalStation(request):
    return render(request, 'civilEngg/totalStation.html')

def estimations(request):
    result = Students.objects.all()
    students = {"allstudents":"result"}
    return render(request, 'civilEngg/estimations.html', students) ;   

class raviclass(View):
    def get(self,request):
        return HttpResponse("Hello class based view")  