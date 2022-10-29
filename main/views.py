from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import *
from .models import *

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    template_name = 'home.html'
    form = ContactForm()
    partiner_form = PartinerForm()
    context = {
        'form':form,
        'partiner_form':partiner_form,
        }
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
    form = DonateForm
    context = {
        "title":title,
        "form":form,
    }
    return render(request,template_name,context)

def careers(request):
    template_name = 'careers.html'
    title="Careers"
    context = {
        "title":title,
    }
    return render(request,template_name,context)

def jobs(request):
    template_name = 'jobs.html'
    title="Announced Jobs"
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
    title="Get Connected To The Market"
    form = MarketForm
    context = {
        "title":title,
        "form":form,
    }
    return render(request,template_name,context)

def get_expert(request):
    template_name = 'get_expert.html'
    title="Get In Touch With An Expert"
    form = ExpertForm
    context = {
        "title":title,
        "form":form,
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
    title="Contact Us"
    context = {
        'form':form,
         "title":title,
    }
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
        
def process_expert(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'],
            phone = request.POST['phone'],            
            village = request.POST['village'],
            district = request.POST['district'],
            region = request.POST['region'],
            message = request.POST['message']
            
            expert = Expert(
                name=name,               
                phone=phone,
                village=village,
                district=district,   
                region=region,                        
                message=message                
            )
            expert.save()
            subject = 'Need an Expert!'
            html_message = render_to_string('expert_mail_template.html', {
                'name':name, 
                'phone':phone,       
                'village': village,
                'district': district,
                'region':region,
                'message':message,
                'subject':subject,
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['agriwezesha@gmail.com',]
            from_email = "contact@agriwezesha.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})
        
def process_market(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'],
            phone = request.POST['phone'],            
            village = request.POST['village'],
            district = request.POST['district'],
            region = request.POST['region'],
            crop = request.POST['crop']
            crop_qty = request.POST['crop_qty']
            sell_time = request.POST['sell_time']
            
            market = Market(
                name=name,               
                phone=phone,
                village=village,
                district=district,   
                region=region,                        
                crop = crop,
                crop_qty = crop_qty,
                sell_time = sell_time,         
            )
            market.save()
            subject = 'Get Connected to Market'
            html_message = render_to_string('market_mail_template.html', {
                'name':name, 
                'phone':phone,       
                'village': village,
                'district': district,
                'region':region,
                'crop' : crop,
                'crop_qty' :crop_qty,
                'sell_time' : sell_time,
                'subject':subject,
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['agriwezesha@gmail.com',]
            from_email = "contact@agriwezesha.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})
        
        
def process_donation(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'],
            email = request.POST['email'],            
            amount = request.POST['amount'],
            
            donation = Donate(
                name=name,               
                email=email,
                amount=amount,        
            )
            donation.save()
            subject = 'Donation Information'
            html_message = render_to_string('donation_mail_template.html', {
                'name':name, 
                'email':email,       
                'amount': amount,
                'subject':subject,
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['agriwezesha@gmail.com',]
            from_email = "contact@agriwezesha.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})

def process_partiner(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'],
            organization = request.POST['organization'],            
            address = request.POST['address'],
            city = request.POST['city'],
            country = request.POST['country'],
            message = request.POST['message'],
            
            partiner = Partiner(
                name=name,               
                organization=organization,
                address=address,
                city=city,
                country=country,                
                message=message
                
            )
            partiner.save()
            subject = 'Partinership Request'
            html_message = render_to_string('partiner_mail_template.html', {
                'name':name,               
                'organization':organization,
                'address':address,
                'city':city,
                'country':country,                
                'message':message, 
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['agriwezesha@gmail.com',]
            from_email = "info@agriwezesha.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})