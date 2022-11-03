from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from blog.models import Post
from .forms import *
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
    #posts = Post.objects.all().order_by('-created_at')
    #context = {'posts':posts}
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