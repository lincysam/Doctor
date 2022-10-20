function test_details()
{
	alert("testing")
	return false;
}





function pagevalidation()
{
	let pfname=document.forms["registration"]["pfname"].value;
	let plname=document.forms["registration"]["lname"].value;
	let phname=document.forms["registration"]["hname"].value;
	let pcityname=document.forms["registration"]["cityname"].value;
	let pstatename=document.getElementById("states").value;
	
	let pdob=document.forms["registration"]["dob"].value;
	let pemail=document.forms["registration"]["email"].value;
	let pcontact=document.forms["registration"]["contact"].value;
	let pusername=document.forms["registration"]["username"].value;
	let ppwd=document.forms["registration"]["password"].value;
	
	
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
	if(contact_validation(pcontact))
	{
	
	
	if(email_validation(pemail))
	{
	
	if(user_validation(pusername,4,12))
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



	function user_validation(uid,mi,ma)
	{
		let uid_length=uid.length;
		if(uid_length==0||uid_length < mi||uid_length > ma)
		{
			alert("Username should not be empty/It should be between"+mi+" and "+ma);
			//uid.focus();
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
			//pwd.focus();
			return false;
		}
		return true;
	}	
	function fname_validation(fname)
	{
		mytext= /^[a-zA-Z]{3,10}$/;
		if(mytext.test(fname))
		{
			return true;
		}
		else
		{	
			alert("Name must be Characters only");
			
			return false;
		}
		
	}
	function lname_validation(lname)
	{
		mytext= /^[A-Za-z]+$/;
		if(mytext.test(lname))
		{
			return true;
		}
		else
		{
			alert("enter valid Lastname");
			//lname.focus();
			return false;
		}
	}
	function house_validation(hname)
	{
		mytext= /^[0-9A-Za-z]+$/;
		if(mytext.test(hname))
		{
			return true;
		}
		else
		{
			alert("HouseName must be AlphaNumeric Characters only");
			
			return false;
		}
	}
	
	function city_validation(cityname)
	{
		mytext= /^[A-Za-z]+$/;
		if(mytext.test(cityname))
		{
			return true;
		}
		else
		{
			alert("CityName must be Characters only");
			
			return false;
		}
	}
	function state_validation(pstatename)
	{
		if(pstatename == "select")
		{
			alert("Select Your State ");
			
			return false;
		}
		else
		{
			return true;
		}
	}
	function gender_validation()
	{
		let chosenOption= "";
		let genderlen = document.getElementsByName('gender').length;
		for (i = 0; i < len; i++) {
			if(document.registration.gender[i].checked){
				chosenOption = document.registration.gender[i].value
				
			}
		}
		if (chosenOption == "") {
			alert("Please choose your gender!");
			return false;
		}
		
	}
	function dob_validation(pdob)
	{	var today = new Date();
		var mymonth= today.getMonth();
		const myarray = pdob.split("-");
		if(today.getFullYear() == pdob.getFullYear())
		{
			
		}
		
		if(today.getFullYear()- pdob.getFullYear() < 99)
		{
			return true;
		}
		else
		{
			alert("Select Valid Date")
			return false;
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