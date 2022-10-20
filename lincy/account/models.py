from django.db import models

# Create your models here.
class user_reg(models.Model):
        fname = models.CharField(max_length=100,null=True)
        lname = models.CharField(max_length=100,null=True)
        username=models.CharField(max_length=100,null=True)
        pword=models.CharField(max_length=100,null=True)
        Gender = models.CharField(max_length=200,null=True)
        state = models.ForeignKey(states, on_delete=models.CASCADE,null=True)
        phone = models.IntegerField(null=True)
        email = models.EmailField()
        dob =  models.DateField(null=True)
        status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
        cdate = models.DateTimeField(null=True)
        mdate = models.DateTimeField(null=True)
        usertype = models.CharField(choices=ITEM_SIZES,max_length=1,null=True)