from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nationality")

    def __str__(self):
        return self.name


class Reg(models.Model):
    name = models.CharField(max_length=255, verbose_name='Region')
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
 

class Zon(models.Model):
    name = models.CharField(max_length=255, verbose_name='Zone')
    reg = models.ForeignKey(Reg,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class Wored(models.Model):
    name = models.CharField(max_length=255,verbose_name='Woreda')
    zon = models.ForeignKey(Zon,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class ServiceDelivery(models.Model):
    name = models.CharField(max_length=255,verbose_name='ServiceDeliveryOffice')
    phone = models.CharField(max_length=255)
    description = models.TextField()
    nationality = models.ForeignKey(Nation,on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Reg,on_delete=models.CASCADE)
    zone = models.ForeignKey(Zon,on_delete=models.CASCADE)
    woreda = models.ForeignKey(Wored,on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.name
  
    