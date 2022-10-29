from django.shortcuts import render

# Create your views here.
def create(request):
    template_name = 'project/create.html'
    form = ContactForm()
    title="Contact Us"
    context = {
        'form':form,
         "title":title,
    }
    return render(request,template_name,context)

def projectlist(request):
    template_name = 'project/list.html' 
    context = {}
    return render(request,template_name,context)
