from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm
from .models import Contact

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    template_name = 'home.html'
    form = ContactForm()
    context = {'form':form,}
    return render(request,template_name,context)

def history(request):
    template_name = 'history.html'
    title="History"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def approach(request):
    template_name = 'approach.html'
    title="Our Approach"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def donate(request):
    template_name = 'donate.html'
    title="Donate"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def careers(request):
    template_name = 'careers.html'
    title="Careers"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def expert_panelist(request):
    template_name = 'expert_panelist.html'
    title="Expert Panelist"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def get_connected_to_market(request):
    template_name = 'get_connected_to_market.html'
    context = {}
    return render(request,template_name,context)

def get_expert(request):
    template_name = 'get_expert.html'
    title="Get In Touch With An Expert"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def resources(request):
    template_name = 'resources.html'
    title="Resources"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def statistics(request):
    template_name = 'statistics.html'
    title="Statistics"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def stories(request):
    template_name = 'stories.html'
    title="Stories Of Hope"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def team(request):
    template_name = 'team.html'
    title="The Team"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def testimonials(request):
    template_name = 'testimonials.html'
    title="Testimonials"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def trainings(request):
    template_name = 'trainings.html'
    title="Trainings"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def vision_mission(request):
    template_name = 'vision_mission.html'
    title="Vision & Mission"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def volunteer(request):
    template_name = 'volunteer.html'
    title="Volunteer with Us"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def consultation(request):
    template_name = 'consultation.html'
    title="Consultation"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def contact(request):
    template_name = 'contact.html'
    form = ContactForm()
    context = {'form':form}
    return render(request,template_name,context)

def process_contact(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'],
            phone = request.POST['phone'],            
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
            
            contact = Contact(
                name=name,               
                phone=phone,
                email=email,
                subject=subject,                
                message=message
                
            )
            contact.save()
            subject = 'Agriwezesha Website Contact Form'
            html_message = render_to_string('mail_template.html', {
                'name':name, 
                'phone':phone,       
                'email': email,
                'message': message,
                'subject':subject, 
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['agriwezesha@gmail.com',]
            from_email = "contact@agriwezesha.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})