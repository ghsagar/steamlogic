from django.db import models

class Information(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')



    def __str__(self):
        return self.title



class Gallery(models.Model):
    title=models.CharField(max_length=25,default='mainweb/image')
    
    gal_img=models.ImageField(upload_to='mainweb/images')

    def __str__(self):
        return self.title
     



class Testimonianls(models.Model):
    name=models.CharField(max_length=25)
    desc=models.CharField(max_length=2000 )
    company=models.CharField(max_length=25 )
    
    img=models.ImageField(upload_to='mainweb/images')

    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=25 )
    position=models.CharField(max_length=20 )
    desc=models.CharField(max_length=2500 )
    
    img=models.ImageField(upload_to='mainweb/images')

    def __str__(self):
        return self.name
     