# GeoService
The documentation will cover following topics
- How to run program
- How use api provided by the service
- How to run unit test with coverage

## How to run program
1. From pycharm
   - Open GeoService from pycharm.
   - Go to, File | Settings | Project: GeoService | Project Interpreter, add new venv in the project.
   - pip install -r requirements.txt
   - run main.py

2. From command line:
   - cd GeoService
   - sudo pip3 install virtualenv
   - virtualenv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
   - cd app 
   - ../vevn/bin/python main.py
   
3. Use docker for Production
   - cd GeoService
   - docker build . -t geo_service_image
   - docker run -d --name geo_container -p 80:80 geo_service_image
   
## How use api provided by the service
Only one api supported by service for now.

1. retrieve address API:
    - API:
        - In production mode use:   http://<your ip>/api/v1/geocoding/retrieveaddress/<latitude>/<longitude>
        - In development mode use:  http://<your ip>:5000/api/v1/geocoding/retrieveaddress/<latitude>/<longitude>
        
    - Note:
    
        Provide your ip and latitude and longitude to the <>. 
        It will try first with google geocoding service, if fail will try here geocoding service.
        
    - Return Values:
    
        - Return Err Code 500 if all the service are unavailabe
        - Return Err Code 400 if the parameters or api contains error is wrong
        - Return Json obj if successfully retrieved address. The result format as following:
            {'Label': '425 W Randolph St, Chicago, IL 60606, United States',
             'Country': 'USA', 'State': 'IL', 'County': 'Cook', 'City': 'Chicago', 'District': 'West Loop',
             'Street': 'W Randolph St', 'HouseNumber': '425', 'PostalCode': '60606'} 

    - Example:
        - using post man to send get http://localhost:5000/api/v1/geocoding/retrieveaddress/41.8842/-87.6388
        - or using curl
        curl -v  "http://localhost/api/v1/geocoding/retrieveaddress/41.8842/-87.6388" which will return:
        
        {"Label": "425 W Randolph St, Chicago, IL 60606, USA", "HouseNumber": "425", "Street": "W Randolph St", 
        "District": "West Loop", "City": "Chicago", "County": "Cook County", "State": "IL", 
        "Country": "US", "PostalCode": "60606"}
        
        For python code example please check file google_geocoding.py in the this project.
        
        
## How to run unit test with coverage
 - cd Geoservice/app
 - ./run_unittest.sh
 