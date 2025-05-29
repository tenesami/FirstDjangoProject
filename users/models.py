from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])]
    )
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
        # return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#         # This method overrides the save method to resize the image if it exceeds 300x300 pixels.
#         # The image is resized to fit within a 300x300 pixel box while maintaining its aspect ratio.
#         # The resized image is then saved back to the same path.
#         # This ensures that profile pictures are optimized for web use, reducing file size and loading times.
#         # The image is resized to fit within a 300x300 pixel box while maintaining its aspect ratio.
#         # This ensures that profile pictures are optimized for web use, reducing file size and loading times.