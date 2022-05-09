from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()

    return render(request, 'home.html', {'majors': majors, 'subjects': subjects})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__name='컴퓨터학과')

    return render(request, 'computer.html', {'computerMajor': computerMajor})

def koreanSubjectView(request):
    subjects = Subject.objects.all()
    koreanMajor = subjects.filter(major__name='국어국문학과')

    return render(request, 'korean.html', {'koreanMajor': koreanMajor})

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')
