from django.shortcuts import render, HttpResponseRedirect
from .form import StudentRegister
from .models import Student

# Create your views here.

# insert a record

def add_show(request):
    if request.method == 'POST':
        sr = StudentRegister(request.POST)
        if sr.is_valid():
            nm = sr.cleaned_data['name']
            em = sr.cleaned_data['email']
            ps = sr.cleaned_data['password']

            stu = Student(name=nm, email=em, password=ps)
            stu.save()
            sr = StudentRegister()

    else:
        sr = StudentRegister()
    
    stud = Student.objects.all()
    return render(request, 'enroll/home.html', {'form':sr, "stu":stud})


# update a record

def update(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        sr = StudentRegister(request.POST, instance=pi)
        if sr.is_valid():
            sr.save()
    else:
        pi = Student.objects.get(pk=id)
        sr = StudentRegister(instance=pi)
    return render(request, 'enroll/update.html', {'form':sr})


# delete a record

def delete(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        