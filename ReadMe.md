# Description
-A django rest api created to communicate with frontend applications without any stress. It has the following features:
-Authentication and User authorization,
-Generates API Key after registration in the Admin page.
-In this API all users can view the APIs created by other user, but they have no permission to update or delete it. 
-Only the author can do that


# Installation Instruction:
-First and Foremost, create venv.
-Activate the venv.
> pip install -r requirements.txt

Run the server

# Usage Instructions:
-To view the APIs, Just navigate to the home page
-To register user, navigate localhost:8000/api/auth/registration
-To login user, navigate localhost:8000/api/auth/login
-To logout user, navigate localhost:8000/api/auth/logout
-To reset password, navigate localhost:8000/api/auth/password/reset

-Note: I tried making it to print out the key at registration,but couldn't. If you find out how, kindly contribute.

# Here is a preview of it.

![](C:\Users\Faith\Pictures\Screenshots\Screenshot (16).png)
![](C:\Users\Faith\Pictures\Screenshots\Screenshot (17).png)