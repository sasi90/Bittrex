# Bittrex-API

**`INFO`**
>This micro services app is used too fetch crypto currency market updates from below
site.
* https://bittrex.github.io/api/v3
* https://bittrex.github.io/api/v3#tag-Markets 
>backend directory contains the flask api with simple authentication methods

Usage
Clone the repo
```
git clone https://github.com/sasi90/Bittrex.git
cd Bittrex
```

Install the backend related requirements and run. The following will start a flask-server on localhost:8000
```
pip install -r requirements.txt
python app.py
```

**API Documentation** postman collection is available in ```api_docx```
* For user login use the below default credential and it will return ```token``` as a session key to access further api's
```{"URL": "http://127.0.0.1:8000", "username":"demo@gmail.com", "password":"demo@123"}```
* API to return all market summary ```http://127.0.0.1:8000/v3/markets/all_summaries?token=M734ARnzRj59miTyiGWiiUhveYc```
* API to return specific market summary ```http://127.0.0.1:8000/v3/markets/individual_summary?market_symbol=ltc-btc&token=M734ARnzRj59miTyiGWiiUhveYc```

**Run the container**
Create a container from the image.
* ```$ docker build --tag bittrex_api .```
* ```$ docker run --name bittrex_api -p 8000:8000 bittrex_api```
* ```Now visit http://localhost:8080```
