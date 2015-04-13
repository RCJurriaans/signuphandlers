from django.db import models

class SummerSchoolSignUp(models.Model):
    CITY_CHOICES = (
        ('AM', 'Amsterdam'),
        ('UT', 'Utrecht'),
        ('AR', 'Arnhem'),
    )
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=2, choices=CITY_CHOICES)
    message = models.TextField()
    
    def __repr__(self):
        return str(self)

    def __unicode__(self):
        return u'%s' % (self.name,)

    def __str__(self):
        return unicode(self).encode('utf-8')
