from curses import flash
from email.policy import default
from enum import unique
from hashlib import blake2b
from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Mtumiaji(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    
    def str(self):
        return self.username
    
    
class Mwanachama(models.Model):
    MACHAGUZI = (
        (0, ('MWENYEKITI')),
        (1, ('M/MSAIDIZI')),
        (2, ('MWANACHAMA')),
    )
    JINSIA = (
        (0, ('MALE')),
        (1, ('FEMALE')),
    )
    # mtumiajiID = models.ForeignKey(Mtumiaji, on_delete=models.CASCADE)  
    mwanachama_jina = models.CharField(max_length=30, null=False) 
    mwanachama_phone = models.CharField(max_length=20, null=False)
    mwanachama_cheo = models.IntegerField(choices=MACHAGUZI, default=2, verbose_name=("Nafasi Yako"))
    mwanachama_jinsia = models.IntegerField(choices=JINSIA, default=0, verbose_name=("Jinsia Yako"))
    pichayamwanachama = models.ImageField(upload_to="uploads/",null=True, blank=True)
    
    
    def str(self):
        return self.mwanachama_phone
    
    
    
class Dharura(models.Model):
    # dharuraid = models.BigIntegerField(primary_key=True)
    mwanachamaID = models.ForeignKey(Mwanachama, on_delete=models.CASCADE)
    # kichwachadharura = models.CharField(max_length=10, null=True, blank=True)
    sababuyadharura = models.TextField()
    tareheyadharura = models.DateTimeField(null=True, blank=True)
    sikuyadharurakuombwa = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return self.dharuraid
    
    
class Mkopo(models.Model):
    mwanachamaID = models.ForeignKey(Mwanachama, on_delete=models.CASCADE, null=True)  
    kiasichamkopo = models.IntegerField()
    tareheyakuombwa = models.DateTimeField(null=False)
    tareheyakurudishwa = models.DateTimeField(null=True, blank=True)
    # sikuyakuombwamkopo = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return self.kiasichamkopo  

class Madeni(models.Model):
    mwanachamaID = models.ForeignKey(Mwanachama, on_delete=models.CASCADE)
    mkopoID = models.ForeignKey(Mkopo, on_delete=models.CASCADE)
    kiasikilichowekwa = models.IntegerField()
    tareheyakuwekapesa = models.DateField()
    kiasichamkopokilichobaki = models.IntegerField()
    
    
    def str(self):
        return self.kiasikilichowekwa
        
    
class Ratibayavikao(models.Model):
    # kikaoid = models.IntegerField(null=False, blank=True)
    kikaoagenda = models.TextField()
    sikuyakikao = models.CharField(max_length=30)
    mudawakikao = models.TimeField(null=False)
    mahalipakikao = models.CharField(max_length=30) 
    tareheyakikao = models.DateTimeField(null=False)   
    
    
    def str(self):
        return self.kikaoid
    
    
class Umojawetu(models.Model):
    mwanachamajina = models.CharField(max_length= 100)
    taarifahusika = models.TextField()
    sikuyatukio = models.DateTimeField(null=False)
    
    def str(self):
        return self.mwanachamajina    