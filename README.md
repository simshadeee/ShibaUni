# ShibaUni
Resy.com Reservation Bot written in Python! 
Sends an email notification when the reservation you are looking for is available. 

## Sample Run Command: 
$ python ShibaUni.py --name nami-nori --seats 2 --range 5 --want 8:00PM

## Inputs
Name: Restaurant Name. Subsitute spaces with dashes     
Seats: Number of seats for your party      
Range: How many days from today are you willing to wait     
Want: What time are you looking for      

## Email
Add a Gmail username and password to the file. The information will be used to authenticate to the Gmail servers to send the alert.

> Note: you will have to allow "Less secure app access" in your [Gmail settings](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account) to allow for the above. 

