from django.db import models

# Create your models here.

class Template(models.Model):
    template_logo = models.CharField(max_length=100)
    template_title = models.CharField(max_length=100)

#class Template_change(models.Model)
    #template = models.ForeignKey(Template, on_delete=models.CASCADE)
