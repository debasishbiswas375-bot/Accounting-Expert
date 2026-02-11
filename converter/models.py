from django.db import models

# This simple model will now show up in your Accounting Expert Admin Portal
class ExcelToTallyLog(models.Model):
    file_name = models.CharField(max_length=255)
    # Fixed the typo: removed the extra 'auto_'
    converted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Success")

    def __str__(self):
        return f"{self.file_name} - {self.converted_at}"
