This is the finished project for the Bitnovia coins website

URL = http://localhost:8000 or the name given to it after deployment.

# Note: there is no frontend to the api created.

The routes below have been tested and confirmed working, below are how You can use the routes with the provided URL


# Note: After every succeccful login or register of a user, a token is generated. 
# For the user the token does not do much unless when about to change some details, The user has to be logged in to make and changes in the info. already provided.
# Note: For all changes made by the admin the your generated token is needed to perform all functions.


1. # URL/api/login 
The above route is to login already registered users 
A form is required to be submitted to this route, which includes
# Email
# Password


2. # URL/api/register
The above route is to Register users 
A form is required to be submitted to this route, which includes
# Email
# mobile_no
# name
# Password


3. # URL/api/users
The above route is a get Request no authentications is need for this.
This only gets the users and the information


4. # URL/logout
The above route is to logout from the api or the website,
The name should be explanatory.
Only the generated token for the user that wants to log out is required.

5. # URL/admin/update-wallet/{name}/{amount}
The above Route can only be assessed by the admin therefore the admin token is required to perform this action.
The name of the user has to be specified and also the amount


6. # URL/admin/updateProfit/{name}/{amount}
The above is route is to chnage the Bonus_profits column
the Net_Profits colums is updated automatically.


7. # URL/update-credentials
The above route is to make changes to Only
- email_address
- Password
so in that case a form has to be submitted.


7. # URL/update-profile
The above route is to make changes to Only
- mobile_no
- name
so in that case a form has to be submitted.



Any other information needed please consult me at 
# jesseugboh@gmail.com
