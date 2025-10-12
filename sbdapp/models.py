from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('interior', 'Interior'),
        ('sliding', 'Sliding'),
        ('construction', 'Construction'),  # Added construction option
    ]
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='interior')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.review[:30]}"