from django.shortcuts import render

# Create your views here.
def userInterface(request):
    return render(request, 'softwareEngg/userInterface.html')

def pythonFullStake(request):
    return render(request, 'softwareEngg/pythonFullStake.html')

def reactNodeJs(request):
    return render(request, 'softwareEngg/reactNodeJs.html')    

def javaFullStack(request):
    return render(request, 'softwareEngg/javaFullStack.html') 