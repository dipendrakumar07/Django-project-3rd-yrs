from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from addChef.models import AddChef
from contactApp.models import Contact
from appMedia.models import Icecreams
from bestService.models import BestService
from django.core.mail import send_mail as send_email
from django.conf import settings
from django.template.loader import render_to_string
import requests
from rajesh.settings import DEFAULT_FROM_EMAIL




def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        allData = Contact(name=name, email=email, subject=subject, message=message)
        allData.save()
        # messages.success(request, "Your form has been submitted successfully.")
        reply_message = f"Thank you for contacting us. We have received your message and will get back to you shortly."
        plain_message = (
            f"Dear {name},"
            f"\n\n{reply_message},"
            f"\n\nBest regards,\nDipendra Team"
        )
        html_message = render_to_string( "email.html", {'name': name, 'reply_message': reply_message})
        send_email(
            subject="Thank you for contacting Dipendra",
            message=plain_message,
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=html_message,
            fail_silently=False,
        )   
        admin_subject = f"New Contact Form Submission"
        admin_message = f"New contact form submission from {name} ({email}):\n\nSubject: {subject}\n\nMessage:\n{message}"
        send_email(
            admin_subject,
            admin_message,
            DEFAULT_FROM_EMAIL,
            [DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
    return render(request, "contact.html",)


def service(request):
    return render(request, "service.html")


def product(request):
    return render(request, "product.html")


def gallery(request):
    return render(request, "gallery.html")


def HomePage(request):
    chef = AddChef.objects.all()
    icecreams = Icecreams.objects.all()
    services = BestService.objects.all()
    return render(request, "index.html", {'chefs': chef, 'icecreams': icecreams, 'services': services})


def about(request):
    chef = AddChef.objects.all().distinct()
    return render(request, "about.html", {'chefs': chef})

def post(request):
    url = 'https://dummyjson.com/posts'
    posts = []
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # dummyjson returns a dict with key 'posts'
            posts = data.get('posts', []) if isinstance(data, dict) else []
    except Exception:
        posts = []
    return render(request, "show_post.html", {'posts': posts})