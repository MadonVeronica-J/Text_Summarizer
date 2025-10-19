from django.db import models
from django.contrib.auth.models import User

class Summary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    input_text = models.TextField()
    summary_text = models.TextField()
    summary_type = models.CharField(max_length=10, choices=[('extract','Extractive'),('abstract','Abstractive')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary by {self.user.username} on {self.created_at}"

