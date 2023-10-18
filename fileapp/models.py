from django.db import models

class file_upload(models.Model):
    file=models.FileField()    

class file_column(models.Model):    
    OEM=models.CharField(max_length=500,null=True)
    Hardware_Type=models.CharField(max_length=500,null=True)
    Equipment_description=models.CharField(max_length=500,null=True)
    Supported_Cards=models.CharField(max_length=500,null=True) 
    Technology_Supported =models.CharField(max_length=500,null=True) 
    Techninal_Description =models.CharField(max_length=500,null=True) 
    Capacity =models.CharField(max_length=500,null=True) 
    MAX_POWER =models.CharField(max_length=500,null=True) 
    Remarks =models.CharField(max_length=500,null=True) 

    def __str__(self):
        return (self.OEM)


# class student_database(models.Model):
#     name=models.CharField(max_length=100)
#     roll_no=models.IntegerField()
#     subject=models.CharField(max_length=100)
    

