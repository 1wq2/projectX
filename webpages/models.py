from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

# Create your models here.

class Sample(models.Model):
    user = models.ForeignKey(User, default=1)
    sample_logo = models.FileField()
    sample_title = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('webpages:detail', kwargs={'pk': self.pk})

    def __str__(self):
        #return self.template_logo + '-' + self.template_title
        return self.sample_title


#class Template_change(models.Model)
    #template = models.ForeignKey(Template, on_delete=models.CASCADE)
