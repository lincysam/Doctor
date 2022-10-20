function pagevalidation()
{
	/*let pfname=document.registration.pfname;
	let plname=document.registration.lname;
	let phname=document.registration.hname;
	let pcityname=document.registration.cityname;
	let pstatename=document.registration.statename;
	let pgender=document.registration.gender;
	let pdob=document.registration.dob;
	let pemail=document.registration.email;
	let pcontact=document.registration.contact;
	let pusername=document.registration.username;
	let ppwd=document.registration.password;
	
	if(user_validation(pusername,4,12))
	{
	if(pwd_validation(ppwd,7,12))
	{
	if(fname_validation(pfname))
	{
	if(lname_validation(plname))
	{
	if(house_validation(phname))
	{
	if(city_validation(pcityname))
	{
	if(state_validation(pstatename))
	{
	if(gender_validation(pgender))
	{
	if(dob_validation(pdob))
	{
	if(email_validation(pemail))
	{
	if(contact_validation(pcontact))
	{
	
	}
	}		
	}
	}
	}
	}
	}
	}
	}
	}
	}
	return false;
}
	function user_validation(uid,mi,ma)
	{
		let uid_length=uid.value.length;
		if(uid_length==0||uid_length < mi||uid_length > ma)
		{
			alert("Username should not be empty/It should be between"+mi+" and "+ma);
			uid.focus();
			return false;
		}
		return true;
	}
	
	
	function pwd_validation(pwd,minval,maxval)
	{
		var pwd_length=pwd.value.length;
		if(pwd_length==0||pwd_length<minval||pwd_length>maxval)
		{
			alert("password should not be empty and it should be between "+minval+" and "+maxval );
			pwd.focus();
			return false;
		}
		return true;
	}
	function fname_validation(fname)
	{
		mytext= /^[A-Za-z]+$/;
		if(fname.value.match(mytext))
		{
			return true;
		}
		else
		{
			alert("Name must be Characters only");
			fname.focus();
			return false;
		}
	}
	function lname_validation(lname)
	{
		mytext= /^[A-Za-z]+$/;
		if(lname.value.match(mytext))
		{
			return true;
		}
		else
		{
			alert("Name must be Characters only");
			lname.focus();
			return false;
		}
	}
	function house_validation(hname)
	{
		mytext= /^[0-9A-Za-z]+$/;
		if(hname.value.match(mytext))
		{
			return true;
		}
		else
		{
			alert("HouseName must be AlphaNumeric Characters only");
			hname.focus();
			return false;
		}
	}
	
	function city_validation(cityname)
	{
		mytext= /^[A-Za-z]+$/;
		if(cityname.value.match(mytext))
		{
			return true;
		}
		else
		{
			alert("CityName must be Characters only");
			cityname.focus();
			return false;
		}
	}
	function state_validation(pstatename)
	{
		if(pstatename.value=="select")
		{
			alert("Select Your State ");
			pstatename.focus();
			return false;
		}
		else
		{
			return true;
		}
	}
	
	function gender_validation(pgender)
	{
		if(pgender.checked)
			
			{
				return true;
			}
		else
		{   alert("Select Your gender"); 
			pgender.focus();
			return false;
		}
	}
	
	function dob_validation(pdob)
	{
		if(pdob.value=="")
		{
			alert("Seelct DOB from calender");
			pdob.focus();
			return false;
		}
		else
		{
		return true;
		}
	}
	function email_validation(pemail)
	{
		myemail= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		if(pemail.value.match(myemail))
		{
			return true;
		}
		else
		{
			alert("You have given Invalid Email");
			pemail.focus();
			return false;
		}
	}
	function contact_validation(pcontact)
	{
		num_format=/^[0-9]{10}+$/;
		if(pcontact.value.match(num_format))
		{
			return true;
		}
		else
		{
			alert("Enter valid Mobile Number");
			pcontact.focus();
			return false;
		}*/
		alert("Welcome to Javascript");
	}
	
	
	
	
	
	
	
	
	
