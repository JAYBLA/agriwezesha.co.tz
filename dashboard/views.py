from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from bootstrap_modal_forms.generic import (
  BSModalDeleteView,
  BSModalUpdateView
)

@login_required(login_url='users:login')
def dashboard(request):
    template_name = 'dash-home.html'
    return render(request, template_name)

def portfolio_create(request):
    template_name = 'dashboard/create_portfolio.html'
    if request.POST:
        formSet = PortfolioFormSet(request.POST, request.FILES, prefix='portfolio')
        if formSet.is_valid():
            formSet.save()
            messages.success(request,'Uploaded successfully', extra_tags='alert alert-success')            
        else:
            messages.error(request, 'An error occured', extra_tags='alert alert-danger')
    else:
        formSet = PortfolioFormSet(prefix='portfolio')
    context = {'formset':formSet}
    return render(request,template_name,context)

def create_job(request):
    template_name = 'jobs/create.html'
    if request.POST:
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted Successfully', extra_tags='alert alert-success')
            return redirect(to='dashboard:jobs')
        else:
            messages.error(request, 'An error occured', extra_tags='alert alert-danger')
    else:
        form = JobForm()
    context = {'form':form}
    return render(request,template_name,context)

def job_list(request):
    template_name = 'jobs/list.html'
    jobs = Job.objects.all().order_by('-created_at')
    context = {'jobs':jobs}
    return render(request, template_name, context)

def update_job(request, job_id):
    template = 'jobs/update.html'
    job = get_object_or_404(Job, pk=job_id)

    job.title = request.POST['title']
    job.qualifications = request.POST['qualifications']
    job.skills = request.POST['skills']
    job.responsibilities = request.POST['responsibilities']
    job.status = request.POST['status']

    job.save()
    return redirect(to="dashboard:jobs")

@login_required()
def job_detail(request,job_id):
    template = 'jobs/detail.html'    
    job = get_object_or_404(Job, pk =job_id)   
    context = {
        'job' :job,      
    }
    
    return render(request, template,context)

@login_required()
def job_delete(request,job_id):     
    job = get_object_or_404(Job, pk =job_id)   
    job.delete()
    return redirect(to="dashboard:jobs")

def project(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Project.objects.create(images=image)
    images = Project.objects.all()
    return render(request, 'index.html', {'images': images})

def projectlist(request):
    template_name = 'project/list.html' 
    context = {}
    return render(request,template_name,context)
