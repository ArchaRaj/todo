from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from .forms import Todoform
from .models import Task


# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'task':task1})
#def details(request):
 #   task1=Task.objects.all()
  #  return render(request,'detail.html',{'task':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task=Task.objects.get(id=id)

    f=Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"update.html",{'f':f,'task':task})



#class based view

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
    #not working

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update2.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DetailView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')