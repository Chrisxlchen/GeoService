from restapi.retrieve_address_handler import RetrieveAddressHandler


class TestRetrieveAddressHandler:
    def test_get(self):
        expected = {'Label': '425 W Randolph St, Chicago, IL 60606, USA', 'HouseNumber': '425',
                    'Street': 'W Randolph St', 'District': 'West Loop', 'City': 'Chicago',
                    'County': 'Cook County', 'State': 'IL', 'Country': 'US', 'PostalCode': '60606'}
        rah = RetrieveAddressHandler()
        r = rah.get(41.8842, -87.6388)
        print(r)
        assert(r == expected)

    def test_get_parameter_error(self):
        expected = ('Invalid input or gps location, lat (-90, 90), lng (-180, 180)', 400)
        rah = RetrieveAddressHandler()
        r = rah.get(41.8842, -187.6388)
        print(r)
        assert(r == expected)

