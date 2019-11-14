from geo_service.geocoding_service import GeoService
from geo_service.google_geocoding import GoogleGeocoding
from geo_service.here_geocoding import HereGeocoding


class TestGeocoding:
    def test_here_decoding(self):
        expected = {'Label': '425 W Randolph St, Chicago, IL 60606, United States',
                    'Country': 'USA', 'State': 'IL', 'County': 'Cook', 'City': 'Chicago', 'District': 'West Loop',
                    'Street': 'W Randolph St', 'HouseNumber': '425', 'PostalCode': '60606'}
        h = HereGeocoding()
        r = h.retrieve_address(41.8842, -87.6388)
        print(r)
        assert(r == expected)

    def test_google_decoding(self):
        expected = {'Label': '425 W Randolph St, Chicago, IL 60606, USA', 'HouseNumber': '425',
                    'Street': 'W Randolph St', 'District': 'West Loop', 'City': 'Chicago',
                    'County': 'Cook County', 'State': 'IL', 'Country': 'US', 'PostalCode': '60606'}
        g = GoogleGeocoding()
        r = g.retrieve_address(41.8842, -87.6388)
        assert(r == expected)

    def test_service(self):
        expected = {'Label': '425 W Randolph St, Chicago, IL 60606, USA', 'HouseNumber': '425',
                    'Street': 'W Randolph St', 'District': 'West Loop', 'City': 'Chicago',
                    'County': 'Cook County', 'State': 'IL', 'Country': 'US', 'PostalCode': '60606'}
        gs = GeoService()
        r = gs.retrieve_address(41.8842, -87.6388)
        assert(r == expected)
