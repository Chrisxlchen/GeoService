class GeocodingBase:
    def __init__(self):
        pass

    def retrieve_address(self, lat: float, lng: float) -> dict:
        raise Exception('Not Implemented')
