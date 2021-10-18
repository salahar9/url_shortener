from django.db import models
from django_countries.fields import CountryField
class ShortUrl(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    alias = models.CharField(max_length=32, unique=True, null=False, verbose_name='Alias')
    long_url = models.URLField(verbose_name='Long URL')

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    
    number_of_visits=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'ID: {self.id}, Alias: {self.alias}, {self.visits} visits.'
    class Meta:
        verbose_name = "link"
        verbose_name_plural = 'Most viewed links'
class Visit(models.Model):
    
    url = models.ForeignKey('ShortUrl',on_delete=models.CASCADE,related_name="visits")
    country=models.CharField(max_length=250)
    date_of_visit=models.DateTimeField(auto_now=True)
    os=models.CharField(max_length=50) 
    class Meta:
        verbose_name="Link stat"
        verbose_name_plural="Stats"
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
