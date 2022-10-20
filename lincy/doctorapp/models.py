from django.db import models


STATUS_SIZES = (
                 ('A','active'),
                 ('I','inactive'),
                )
                
ITEM_SIZES = (
            ('D','doctor'),
            ('P','patient'),
            )
                

class states(models.Model):
    statename = models.CharField(max_length=100,null=True)
    
class hospitallist(models.Model):
    
    hosptname = models.CharField(max_length=100,null=True)
    stateid = models.ForeignKey(states, on_delete=models.CASCADE, null=True)
    
    contactno = models.IntegerField(null=True)
    
    status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
    cdate = models.DateTimeField()
    mdate = models.DateTimeField()
    
class department(models.Model):

    deptname = models.CharField(max_length=100,null=True)
    status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
    cdate = models.DateTimeField()
    mdate = models.DateTimeField()
    
class user_reg(models.Model):
        fname = models.CharField(max_length=100,null=True)
        lname = models.CharField(max_length=100,null=True)
        username=models.CharField(max_length=100,null=True)
        pword=models.CharField(max_length=100,null=True)
        Gender = models.CharField(max_length=200,null=True)
        state = models.ForeignKey(states, on_delete=models.CASCADE,null=True)
        phone =models.CharField(max_length=100,null=True)
        email = models.EmailField()
        dob =  models.DateField(null=True)
        status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
        cdate = models.DateTimeField(null=True)
        mdate = models.DateTimeField(null=True)
        usertype = models.CharField(choices=ITEM_SIZES,max_length=1,null=True)
        
class consultation(models.Model):
    hospitalid = models.ForeignKey(hospitallist, on_delete=models.CASCADE,null=True)
    deptid = models.ForeignKey(department, on_delete=models.CASCADE,null=True)
    doctorid = models.IntegerField(null=True)
    patientid = models.IntegerField(null=True)
    consult_day = models.CharField(max_length=200,null=True)
    payment = models.CharField(max_length=100,null=True)
    status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
    cdate = models.DateTimeField()
    mdate = models.DateTimeField()
    
class doctor_availability(models.Model):
    doctorid = models.ForeignKey(user_reg, on_delete=models.CASCADE,null=True)
    hospitalid = models.ForeignKey(hospitallist, on_delete=models.CASCADE,null=True)
    deptid =models.ForeignKey(department, on_delete=models.CASCADE,null=True)
    available_days= models.CharField(max_length=200,null=True)
    status = models.CharField(choices=STATUS_SIZES,max_length=1,null=True)
    cdate = models.DateTimeField()
    mdate = models.DateTimeField()
    

    
   
    
    
    
    
    
    
    
    
    
    
    
    


    
 
    
    
    
   