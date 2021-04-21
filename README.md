 Simple Django REST API application that works with a collection of restaurants.
 
 
 Implemented the following endpoints:
 
 1. http://127.0.0.1:8000/restaurants/  - (GET) get all restaurants
 2. http://127.0.0.1:8000/restaurants/  - (POST) add new restaurant
 3. http://127.0.0.1:8000/restaurants/sorted/  - (GET) sort restaurants in descending order
 4. http://127.0.0.1:8000/restaurants/luxury/  - (GET) get restaurant with max average bill
 5. http://127.0.0.1:8000/restaurants/with-item?itemName=cola  - (GET) get restaurants with some itemName
 
 To use it:
 
 - git clone ...
 - python -m venv venv
 - venv\Scripts\activate
 - pip install -r requirements.txt
 - move to restapi folder
 - manage.py runserver
 - for requests, use Postman
