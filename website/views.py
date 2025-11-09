from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.add_message(request, messages.SUCCESS, 'your ticket success submited!')
        else:
            message = messages.add_message(request, messages.ERROR, 'your ticket not submited!')
    form = ContactForm()
    context = {'form' : form}
    return render(request, 'website/contact.html', context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.add_message(request, messages.SUCCESS, 'Email success submited!')
        else:
            message = messages.add_message(request, messages.ERROR, 'Email not submited!')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')