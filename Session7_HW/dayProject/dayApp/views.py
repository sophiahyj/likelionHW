from django.shortcuts import render, redirect
from .models import Day

# Create your views here.
def home(request):
    days = Day.objects.all().order_by('date')

    return render(request, 'home.html', {'days': days})

def new(request):
    if request.method =='POST':
        new_day = Day.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date'],
        )
        return redirect('detail', new_day.pk)

    return render(request, 'new.html')

def detail(request, day_pk):
    day = Day.objects.get(pk=day_pk)

    return render(request, 'detail.html', {'day': day})

def edit(request, day_pk):
    day = Day.objects.get(pk=day_pk)

    if request.method == 'POST':
        Day.objects.filter(pk=day_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date'],
        )
        return redirect('detail', day_pk)

    return render(request, 'edit.html', {'day': day})


def delete(request, day_pk):
    day = Day.objects.get(pk=day_pk)
    day.delete()

    return redirect('home')