from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from doctorapp.models import user_reg,states,department,hospitallist,doctor_availability
import datetime,time
from django.urls import reverse
from django.db.models import Q
from.import views
import json
# Create your views here.
#def doctor(request):
    
   # return render(request,'doctorlogin.html')

def patientdetails(request):
    if request.method == 'POST':
        uname=request.POST['pname']
        patientpwd=request.POST['pwd']
        
        
        if(uname=="" or patientpwd==""):
            msg="Invalid Credentials"
            return render(request,'patientlogin.html',{'loginmsg':msg})
        if user_reg.objects.filter(Q(username=uname) & Q(usertype='P')):
            print("Valid User")
            patient=user_reg.objects.filter(username=uname)
            pid=patient[0].id
            
            return render(request,'patient_details.html',{'patientdata':pid})
        else:
            sec_msg= "Invalid Credentials"
            return render(request,'patientlogin.html',{'invalidmsg':sec_msg})
def doctordetails(request):
    
    if request.method == 'POST':
        dname=request.POST['dname']
        doctorpwd=request.POST['dpwd']
        if(dname=="" or doctorpwd==""):
            msg="Invalid Credentials"
            return render(request,'doctorlogin.html',{'loginmsg':msg})
        if user_reg.objects.filter(Q(username=dname) & Q(usertype='D')):
            print("Valid User")
            doctor=user_reg.objects.filter(username=dname)
            did=doctor[0].id
            
            return render(request,'doctor_details.html',{'docid':did})
        else:
            sec_msg= "Invalid Credentials"
            return render(request,'doctorlogin.html',{'invalidmsg':sec_msg})
        
    
    
def consultation(request):
    
    pid=request.GET['patientid']
    print("Patientid:",pid)
    patientobj=doctor_availability.objects.all()
    
        
    for doctor in patientobj:
        val=hospitallist.objects.values_list('hosptname',flat=True).filter(id=doctor.hospitalid_id).distinct('hosptname')
        
        newval=val.values()[0]
        doctor.hospital=newval['hosptname']
        deptval=department.objects.filter(id=doctor.deptid_id).values()
        deptname=deptval.values()[0]
        doctor.deptname=deptname['deptname']
        docid=user_reg.objects.filter(id=doctor.doctorid_id).values()
        doctorname=docid.values()[0]
        doctor.doctorname=doctorname['fname']
      
    return render(request,'consultation.html',{'hosptdata':patientobj})
def doctoravail(request):
    doctorid=request.GET['doctorid']
    deptobjd= department.objects.all()
    hosptobjd = hospitallist.objects.all()
    return render(request,'doctor_availability.html',{'hosptdatad':hosptobjd,'deptdatad':deptobjd,'docid':doctorid})
def doctorschedule(request):
    doctorid=request.GET['doctorid']
    return render(request,'doctor_schedule.html',{'docid':doctorid})
def availsave(request):
    
    if request.method == 'POST':
        doctid=request.POST['docid']
        
        did=user_reg.objects.get(id=doctid)
        
        hosptname=request.POST['hospitals']
        deptname=request.POST['department']
        hostid=hospitallist.objects.get(id=hosptname)
        deptid=department.objects.get(id=deptname)
        now=datetime.datetime.now()
        days=request.POST.getlist('days[]')
        sep=','
        availdays=sep.join(days)
        deptobjd= department.objects.all()
        hosptobjd = hospitallist.objects.all()
        if doctor_availability.objects.filter(Q(doctorid=doctid) & Q(hospitalid=hostid)):
            usermsg="User Existed"
            return render(request,'doctor_availability.html',{'msg':usermsg,'docid':doctid,'hosptdatad':hosptobjd,'deptdatad':deptobjd})
        savedata=doctor_availability(doctorid=did,hospitalid=hostid,deptid=deptid,available_days=availdays,status='A',cdate=now,mdate=now)
        savedata.save()
        res=("Data Saved")
        
        return render(request,'doctor_availability.html',{'display':res,'docid':doctid,'hosptdatad':hosptobjd,'deptdatad':deptobjd})
def hosplist(request):
    docid=request.GET['doctorid']
    
    listobj=fetchfunction(docid)
    """
    listobj=doctor_availability.objects.filter(doctorid=docid)
   
    for doctor in listobj:
        val=hospitallist.objects.filter(id=doctor.hospitalid_id).values()
        newval=val.values()[0]
        doctor.hospital=newval['hosptname']
        print ("Newvalue: ",newval['hosptname']) """
    
    return render(request,'list_hospital.html',{'listdata':listobj,'docid':docid})
def deletelist(request):
    docid=request.GET.get('doctorid')
    
    eachdoctorid=request.GET['eachid']
    eachdoctor=doctor_availability.objects.get(id=eachdoctorid)
    
    eachdoctor.delete()
    listobj=fetchfunction(docid)
    return render(request,'list_hospital.html',{'listdata':listobj,'docid':docid})
   
def fetchfunction(docid):
    listobj=doctor_availability.objects.filter(doctorid=docid)
    
    for doctor in listobj:
        val=hospitallist.objects.filter(id=doctor.hospitalid_id).values()
        newval=val.values()[0]
        doctor.hospital=newval['hosptname']
    return listobj
    
    
    
def patientnewdata(request):
    print("inside Function")
    deptname = request.GET.get('dept', None)
    hosptname= request.GET.get('hospt', None)
    docobj=doctor_availability.objects.filter(Q(hospitalid=hosptname) & Q(deptid=deptname))
    #data={docobj}
    #return JsonResponse(data)
    return render(request,'consultation.html',{'data':docobj}) 