from django.db import models

class Contact(models.Model):
    """
    Model representing a contact message.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the Contact instance.
        """
        return self.name