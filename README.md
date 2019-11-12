# GeoService
The documentation will cover following topics
- How to run program
- How use api provided by the service
- How to run unit test with coverage

## How to run program
1. From pycharm
   - Open GeoService from pycharm.
   - Go to, File | Settings | Project: GeoService | Project Interpreter, choose venv in the project.
   - run main.py

2. From command line:
   - cd GeoService
   - vevn/bin/python src/main.py
   
## How use api provided by the service
Only one api supported by service for now.

###1. retrieve address API:
    - API:
        http://<your ip>:12632/api/v1/geocoding/retrieveaddress?lat=<latitude>&lng=<longitude>
        
    - Note:
        Provide your ip and latitude and longitude to the <>. 
        It will try first with google geocoding service, if fail will try here geocoding service.
        
    - Return Values:
        Err Code 500 if all the service are unavailabe
        Err Code 400 if the parameters or api contains error is wrong
        Json obj if successfully retrieved address. The result format as following:
            {'Label': '425 W Randolph St, Chicago, IL 60606, United States',
             'Country': 'USA', 'State': 'IL', 'County': 'Cook', 'City': 'Chicago', 'District': 'West Loop',
             'Street': 'W Randolph St', 'HouseNumber': '425', 'PostalCode': '60606'} 

    - Example:
        using post man to send get http://localhost:12632/api/v1/geocoding/retrieveaddress?lat=41.8842&lng=-87.6388
        or using curl
        curl -v  "http://localhost:12632/api/v1/geocoding/retrieveaddress?lat=41.8842&lng=-87.6388"
        will return:
        {"Label": "425 W Randolph St, Chicago, IL 60606, USA", "HouseNumber": "425", "Street": "W Randolph St", 
        "District": "West Loop", "City": "Chicago", "County": "Cook County", "State": "IL", 
        "Country": "US", "PostalCode": "60606"}
        
        For python code example please check file google_geocoding.py in the this project.
        
        
## How to run unit test with coverage
    cd Geoservice
    ./run_unittest.sh
 