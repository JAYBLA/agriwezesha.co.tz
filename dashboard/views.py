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
    projects = Project.objects.all()
    active_adverts = Job.objects.filter(status='active')
    expired_adverts = Job.objects.filter(status='expired')
    context = {
        'active_adverts':active_adverts,
        'expired_adverts':expired_adverts,
        'projects':projects,
    }

    return render(request, template_name,context)

@login_required(login_url='users:login')
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

@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
def job_list(request):
    template_name = 'jobs/list.html'
    jobs = Job.objects.all().order_by('-created_at')
    context = {'jobs':jobs}
    return render(request, template_name, context)


@login_required(login_url='users:login')
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

@login_required(login_url='users:login')
def job_detail(request,job_id):
    template = 'jobs/detail.html'    
    job = get_object_or_404(Job, pk =job_id)   
    context = {
        'job' :job,      
    }    
    return render(request, template,context)

@login_required(login_url='users:login')
def job_delete(request,job_id):     
    job = get_object_or_404(Job, pk =job_id)   
    job.delete()
    return redirect(to="dashboard:jobs")


@login_required(login_url='users:login')
def project(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Project.objects.create(images=image)
    images = Project.objects.all()
    return render(request, 'index.html', {'images': images})



@login_required(login_url='users:login')
def create_project(request):
    template_name = 'project/create.html'
    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted Successfully', extra_tags='alert alert-success')
            return redirect(to='dashboard:projectlist')
        else:
            messages.error(request, 'An error occured', extra_tags='alert alert-danger')
    else:
        form = ProjectForm()
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='users:login')
def projectlist(request):
    projects = Project.objects.all().order_by('-created_at')
    template_name = 'project/list.html' 
    context = {
        'projects':projects,
    }
    return render(request,template_name,context)

@login_required(login_url='users:login')
def project_detail(request,project_id):
    template = 'project/detail.html'    
    project = get_object_or_404(Project, pk =project_id)   
    context = {
        'project' :project,      
    }    
    return render(request, template,context)

@login_required(login_url='users:login')
def update_project(request, p_id):
    template = 'jobs/update.html'
    project = get_object_or_404(Project, pk=p_id)

    project.name = request.POST['name']
    project.save()
    return redirect(to="dashboard:projectlist")

@login_required(login_url='users:login')
def project_delete(request,p_id):     
    project = get_object_or_404(Project, pk =p_id)   
    project.delete()
    return redirect(to="dashboard:projectlist")


@login_required(login_url='users:login')
def project_images(request):
    template = 'project_images/create.html'
   
    if request.method=='POST':
        p_id = request.POST['project_id']        
        images = request.FILES.getlist('images')     
                
        if p_id=='None':
            projects = Project.objects.order_by('name')
            context = {
                'projects' : projects,
                'error_message' : 'Please select a Project',
            }
            return render(request, template, context)
        else:
            project = get_object_or_404(Project, pk=p_id)
            for image in images:
                MultipleImage.objects.create(images=image,project=project)

            image_list = MultipleImage.objects.all()
            context = {
            'images' : image_list,		
            }
        return render(request, template, context) 
    else:
        projects = Project.objects.all()
        image_list = MultipleImage.objects.all()        
        context = {			
            'images' : image_list,
            'projects':projects,			
        }
        return render(request, template, context)


@login_required(login_url='users:login')
def images(request):
    template = 'project_images/list.html'
    image_list = MultipleImage.objects.all()        
    context = {			
        'images' : image_list,       		
    }
    return render(request, template, context)

@login_required(login_url='users:login')
def project_photo_delete(request,image_id):     
    image = get_object_or_404(MultipleImage, pk =image_id)   
    image.delete()
    return redirect(to="dashboard:images")


# AGROFOREST PROJECT
@login_required(login_url='users:login')
def create_agroforest(request):
    template_name = 'agroforest/create.html'
    if request.POST:
        form = AgroforestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted Successfully', extra_tags='alert alert-success')
            return redirect(to='dashboard:agroforestlist')
        else:
            messages.error(request, 'An error occured', extra_tags='alert alert-danger')
    else:
        form = AgroforestForm()
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='users:login')
def agroforestlist(request):
    agroforests = Agroforest.objects.all().order_by('-created_at')
    template_name = 'agroforest/list.html' 
    context = {
        'agroforests':agroforests,
    }
    return render(request,template_name,context)

@login_required(login_url='users:login')
def agroforest_detail(request,project_id):
    template = 'agroforest/detail.html'    
    agroforest = get_object_or_404(Agroforest, pk =project_id)   
    context = {
        'project' :agroforest,      
    }    
    return render(request, template,context)

@login_required(login_url='users:login')
def update_agroforest(request, p_id):    
    project = get_object_or_404(Agroforest, pk=p_id)

    project.name = request.POST['name']
    project.trees = request.POST['trees']
    project.acres = request.POST['acres']
    project.people = request.POST['people']
    project.save()
    return redirect(to="dashboard:agroforestlist")

@login_required(login_url='users:login')
def agroforest_delete(request,p_id):     
    project = get_object_or_404(Agroforest, pk =p_id)   
    project.delete()
    return redirect(to="dashboard:agroforestlist")