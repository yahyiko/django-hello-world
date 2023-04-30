from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
        
            html = render_to_string('contact/emails/contactform.html', {
                'name':name,
                'email':email,
                'content':content

            })


            print('the form was valid')

            send_mail('The contact form subject','This is the message','MarqYourCalendar@outlook.com',['MarqYourCalendar@outlook.com'],html_message=html)
            send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, ['MarqYourCalendar@outlook.com'],html_message=html)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })

