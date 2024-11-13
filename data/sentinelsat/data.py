from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

# Connect to the API using your Copernicus credentials
api = SentinelAPI('your_username', 'your_password', 'https://scihub.copernicus.eu/dhus')

# Define area of interest as a GeoJSON file
footprint = geojson_to_wkt(read_geojson('area_of_interest.geojson'))

# Query Sentinel-2 data
products = api.query(footprint,
                     date=('20240101', '20240131'),  # specify date range
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))  # only images with up to 30% cloud cover

# Download data
api.download_all(products)
