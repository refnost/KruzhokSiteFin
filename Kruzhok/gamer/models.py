from django.db import models
from django.conf import settings

# Create your models here.
class user(models.Model):
    talent = models.CharField('talentid', max_length=16)
    mail = models.CharField('mail', max_length=128)
    epicid = models.CharField('epicid', max_length=128, default='', blank=True)
    overwatchname = models.CharField('overwatch_name', max_length=128, default='', blank=True)
    teamplay = models.CharField('TeamPlay', max_length=8, default='', blank=True)
    teamplayfn = models.CharField('TeamPlay_Fortnite', max_length=8, default='', blank=True)
    teamplayow = models.CharField('TeamPlay_Overwatch', max_length=8, default='', blank=True)
    nickfn = models.CharField('Fortnite_nickname', max_length=128, default='', blank=True)
    icon = models.CharField('Icon', blank=True, max_length=512, default='https://st2.depositphotos.com/5266903/8135/v/600/depositphotos_81358350-stock-illustration-client-flat-icon.jpg')
    date = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.talent

    class Meta:
        verbose_name = 'Talentovec'
        verbose_name_plural = 'Talentovci'
