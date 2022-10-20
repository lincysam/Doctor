from django.shortcuts import render,redirect, HttpResponse
from django.template import loader
from django.contrib import messages
from doctorapp.models import user_reg,states,department,hospitallist
from datetime import *
import re
from datetime import timedelta
import datetime,time

# Create your views here.
def patient(request):
    
    return render(request,'patientlogin.html')
 
def doctor(request):
    
    return render(request,'doctorlogin.html')
    
def doctorreg(request):
    stateobjs=states.objects.all()
    return render(request,'doctorreg.html',{'statedatas':stateobjs})
    
def patientreg(request):
    
    stateobj=states.objects.all()
    
    return render(request,'patientreg.html',{'statedata':stateobj})

    

    

    #,{'deptdata':deptobj},{'hosptdata':hosptobj}
def registerpatient(request):
    if request.method == 'POST':
        firstname = request.POST['pfname']
        lastname = request.POST['lname']
        uname = request.POST['username']
        password = request.POST['password']
        gender = str(request.POST["gender"])
        state = request.POST['statename']
        mystate=states(id=state)
        #print("state name: ",mystate)
        email = request.POST['email']
        phone = request.POST['contact']
        dob=request.POST['dob']
        now=datetime.datetime.now()
        todays = str(datetime.date.today())
        try:
            formatted_date1 = time.strptime(dob, "%Y-%m-%d")
            formatted_date2 = time.strptime(todays, "%Y-%m-%d")
        
            if(formatted_date1 > formatted_date2 or dob ==""):
        
        
                datemsg="Please Enter valid dob"
                return render(request,'patientreg.html',{'dmsg':datemsg})
        except ValueError as e:
            print('ValueError:', e)
        
        
        if user_reg.objects.filter(username=uname):
            usermsg="User already taken"
            return render(request,'patientreg.html',{'umsg':usermsg})
            
         
        elif((re.search(r'^[a-zA-Z]{3,15}$',firstname)) and (re.search(r'^[a-zA-Z]{3,15}$',lastname))):
            if(re.search(r'^[0-9]{10}$',phone)):
                if((re.search(r'[a-z]\w{3,15}@[a-z]{3,7}.[a-z]{2,5}',email))):
                    user_register = user_reg(fname=firstname,lname=lastname,username=uname,pword=password,
                    Gender=gender,state=mystate,dob=dob,email=email,phone=phone,status='A',cdate=now,mdate=now,usertype='P')
                    user_register.save()
                    print("user created")
                    return render(request,'patientlogin.html')
                else:
                    emailmsg="Enter Valid Emailaddress"
                    return render(request,'patientreg.html',{'emsg':emailmsg})
            else:
                mobilemsg="Enter valid Mobile Number"
                return render(request,'patientreg.html',{'mobmsg':mobilemsg})
        else:
            namemsg=("Enter Valid Name")
            return render(request,'patientreg.html',{'nmsg':namemsg})
            
def registerdoctor(request):

    if request.method == 'POST':
        firstname = request.POST['dfname']
        lastname = request.POST['dlname']
        uname = request.POST['dusername']
        password = request.POST['dpassword']
        gender = str(request.POST["dgender"])
        state = request.POST['dstatename']
        mystate=states(id=state)
        dob=request.POST['dob']
        email = request.POST['demail']
        phone = request.POST['dcontact']
       
        now=datetime.datetime.now()
        todays = str(datetime.date.today())
        try:
            formatted_date1 = time.strptime(dob, "%Y-%m-%d")
            formatted_date2 = time.strptime(todays, "%Y-%m-%d")
        
            if(formatted_date1 > formatted_date2 or dob ==""):
        
        
                datemsgdoctor="Please Enter valid dob"
                return render(request,'patientreg.html',{'dmsg':datemsgdoctor})
                 
        except ValueError as e:
            print('ValueError:', e)
        
        
        if user_reg.objects.filter(username=uname):
            #messages.info(request,'User already Created')
            mystr="User already Taken"
            return render(request,'doctorreg.html',{'result':mystr})
            
        else:
            user_register = user_reg(fname=firstname,lname=lastname,username=uname,pword=password,
            Gender=gender,email=email,phone=phone,state=mystate, dob=dob,status='A',cdate=now,mdate=now,usertype='D')
            user_register.save()
            #messages.info(request,'User Created')
            mystr="User Created"
            return render(request,'doctorlogin.html',{'result':mystr})
            
    
    

    

