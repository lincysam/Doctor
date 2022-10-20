
function pagevalidation()
{
	let pfname=document.forms["registration"]["dfname"].value;
	let plname=document.forms["registration"]["dlname"].value;
	let phname=document.forms["registration"]["dhname"].value;
	let pcityname=document.forms["registration"]["dcityname"].value;
	let pstatename=document.getElementById("states").value;
	
	let pdob=document.forms["registration"]["dob"].value;
	let pemail=document.forms["registration"]["demail"].value;
	let pcontact=document.forms["registration"]["dcontact"].value;
	let pusername=document.forms["registration"]["dusername"].value;
	let ppwd=document.forms["registration"]["dpassword"].value;
	alert(pstatename);
	
	if(fname_validation(pfname))
	{
	if(lname_validation(plname))
	{
	if(hname_validation(phname))
	{
	if(cityname_validation(pcityname))
	{
	if(statename_validation(pstatename))
	{
	if(email_validation(pemail))
	{
	if(contact_validation(pcontact))
	{
	if(username_validation(pusername,4,12))
	{
	if(pwd_validation(ppwd,7,12))
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
	
	//return false;
	
}

function fname_validation(fname)
{	
	mytext=/^[a-zA-Z]{3,10}$/;
	if(mytext.test(fname))
	{
		return true;
	}
	else
	{
		alert("FirstName must be characters only");
		return false;
	}
}

function lname_validation(lname)
{	
	mytext=/^[a-zA-Z]{3,10}$/;
	if(mytext.test(lname))
	{
		return true;
	}
	else
	{
		alert("LastName must be characters only");
		return false;
	}
}
function hname_validation(hname)
{	
	mytext=/^[0-9a-zA-Z]{3,10}$/;
	if(mytext.test(lname))
	{
		return true;
	}
	else
	{
		alert("Housename must be AlphaNumeric characters only");
		return false;
	}
}
function cityname_validation(cityname)
{	
	mytext=/^[a-zA-Z]{3,10}$/;
	if(mytext.test(cityname))
	{
		return true;
	}
	else
	{
		alert("CityName must be characters only");
		return false;
	}
}
function statename_validation(statename)
	{ alert("statename is: ",statename);
		if(statename == "select")
		{
			alert("Select Your State ");
			
			return false;
		}
		else
		{
			return true;
		}
	}
function email_validation(pemail)
	{
		myemail= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})$/;
		if(myemail.test(pemail))
		{
			return true;
		}
		else
		{
			alert("You have given Invalid Email");
			
			return false;
		}
	}
function contact_validation(contact)
	{	
		mytext= /^[0-9]{10}$/;
		if(mytext.test(contact))
		{
			return true;
		}
		else
		{
			alert("Enter valid Mobile Number");
			
			return false;
		}
	}
function username_validation(uid,mi,ma)
	{
		let uid_length=uid.length;
		if(uid_length==0||uid_length < mi||uid_length > ma)
		{
			alert("Username should not be empty/It should be between"+mi+" and "+ma);
			
			return false;
		}
		return true;
	}
function pwd_validation(pwd,minval,maxval)
	{
		let pwd_length=pwd.length;
		if(pwd_length == 0||pwd_length < minval||pwd_length > maxval)
		{
			alert("password should not be empty and it should be between "+minval+" and "+maxval );
			
			return false;
		}
		return true;
	}	

