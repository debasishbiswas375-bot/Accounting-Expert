from django.db import models

class ExcelToTallyLog(models.Model):
    file_name = models.CharField(max_length=255)
    converted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Success")

    def __str__(self):
        return f"{self.file_name} - {self.converted_at}"
