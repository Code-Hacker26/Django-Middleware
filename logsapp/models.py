from django.db import models

class RequestLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    error_message = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code}"


class LogEntry(models.Model):
    path = models.CharField(max_length=255, help_text="The URL path accessed.")
    method = models.CharField(max_length=10, help_text="HTTP method (GET, POST, etc.).")
    status_code = models.IntegerField(help_text="HTTP status code returned.")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Time when the request was made.")

    def __str__(self):
        return f"{self.method} {self.path} [{self.status_code}]"