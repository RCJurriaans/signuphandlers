from django.db import models

class SummerSchoolSignUp(models.Model):
    CITY_CHOICES = (
        ('AM', 'Amsterdam (6-10 Juli)'),
        ('A2', 'Amsterdam (13-17 Juli)'),
        ('UT', 'Utrecht (17-21 Augustus)'),
        ('AR', 'Arnhem (24-28 Augustus)'),
    )
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=2, choices=CITY_CHOICES)
    age = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(blank=True)
    parent = models.CharField(max_length=255, null=True, blank=True)
    parent_phone = models.CharField(max_length=255, null=True, blank=True)
    
    def __repr__(self):
        return str(self)

    def __unicode__(self):
        return u'%s' % (self.name,)

    def __str__(self):
        return unicode(self).encode('utf-8')
