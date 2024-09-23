from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

class newStocks(models.Model):
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=10, default="game_account")

    def clean(self):
        # Ensure you have an image before checking its dimensions
        if self.image:
            img = Image.open(self.image)
            width, height = img.size
            width_limit, height_limit = 335, 150  # Integer values for pixel dimensions

            # Check if the image exceeds the defined limits
            if width > width_limit or height > height_limit:
                raise ValidationError(f"Image size should not exceed {width_limit}px by {height_limit}px.")

    def __str__(self):
        return self.alt

    


class stockQuotes(models.Model):
    new_stock = models.OneToOneField(newStocks, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="Title")
    text = models.CharField(max_length=200, default="Some description stuff.")

class socialSites(models.Model):
    ...


