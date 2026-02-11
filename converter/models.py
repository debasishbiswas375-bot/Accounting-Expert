from django.db import models

# By leaving this file without a custom User class, we fix the E304 error.
# This allows Django to use its built-in, secure User model for your Admin Portal.

class ExcelToTallyLog(models.Model):
    """
    Optional: A simple model to track your file conversions.
    This will show up in your 'Accounting Expert Admin Portal'.
    """
    file_name = models.CharField(max_length=255)
    converted_at = models.DateTimeField(auto_auto_now_add=True)
    status = models.CharField(max_length=50, default="Success")

    def __str__(self):
        return f"{self.file_name} - {self.converted_at}"
