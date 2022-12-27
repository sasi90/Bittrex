# API Endpoint

**`INFO`**
>This micro services app is used to handle employee attendance report relating with database (Mysql)
>backend directory contains the flask api with authentication methods

Usage
Clone the repo
```
git clone https://github.com/sasi90/employee_reports.git
cd employee_reports
```

Install the backend related requirements and run the server. The following will start a flask-server on localhost:8000
```
pip install -r requirements.txt
python app.py
```
**API Documentation** postman collection is available in the folder ```api_document```
* For user login use the below default credential and it will return ```token``` as a session key to access further api's
```{"URL": "http://127.0.0.1:8000", "username":"hr@gmail.com", "password":"hr@123"}```
