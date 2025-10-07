from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact,GalleryImage,Testimonial

def index_view(request):
    gallery_images = GalleryImage.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {
        'gallery_images': gallery_images,
        'testimonials': testimonials,
    })

def interior_view(request):
    gallery_images = GalleryImage.objects.filter(category='interior')
    return render(request, "interior.html", {
        'gallery_images': gallery_images,
        'category': 'interior'
    })

def sliding_view(request):
    gallery_images = GalleryImage.objects.filter(category='sliding')
    return render(request, "sliding.html", {
        'gallery_images': gallery_images,
        'category': 'sliding'
    })

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        Contact.objects.create(name=name, email=email, message=message)

        # Send email (Mailtrap)
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email="noreply@sbd.com",
            recipient_list=["subashbuildanddesignstudio@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "✅ Your message has been sent successfully!")
        return redirect("index")  # back to home page

    return redirect("index")
