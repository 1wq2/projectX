from django.db import models

# Create your models here.

class Sample(models.Model):
    sample_logo = models.CharField(max_length=100)
    sample_title = models.CharField(max_length=100)

    def __str__(self):
        #return self.template_logo + '-' + self.template_title
        return self.sample_title
#class Template_change(models.Model)
    #template = models.ForeignKey(Template, on_delete=models.CASCADE)