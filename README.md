# How other computers can connect to the website (local)
Changes value ALLOWED_HOSTS = ['IPv4_Address_của_máy_mình', '.localhost', '127.0.0.1']
Run py .\manage.py runserver 0.0.0.0:8000
Other computers: enter the host's IPv4 address (including port)
https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts

---

## screenshots
### Homepage
![homepage snap](https://github.com/pgk15/Picture-/blob/master/Picture1.png)
### Admin Dashboard
![dashboard snap](https://github.com/pgk15/Picture-/blob/master/Picture2.png)
### Policy 
![doctor snap](https://github.com/pgk15/Picture-/blob/master/Picture3.png)
---
## Functions
### Admin
- Admin account can be created using createsuperuser command.
- After login, admin can view/update/delete customer
- Can view/add/update/delete policy category like Life, Health, Motor, Travel
- Can view/add/update/delete policy
- Can view total policy holder, approved policy holder, disapproved policy holder
- Can approve policy, applied by customer
- Can answer customer question

### Customer
- Create account (no approval required by admin)
- After login, can view all policy that are added by admin.
- If customer likes any policy, then they can apply for it.
- When customer will apply for any policy, it will go into pending status, admin can approve it.
- Customer can check status of his policy under history section
- Customer can ask question from admin. 

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements.txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settings.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```


## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.
