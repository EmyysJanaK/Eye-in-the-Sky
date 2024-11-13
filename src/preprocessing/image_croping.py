import rasterio
from rasterio.mask import mask
import geopandas as gpd

# Load the downloaded image
with rasterio.open('sentinel_image.tif') as src:
    # Define the area of interest with a GeoDataFrame
    shapes = gpd.read_file('area_of_interest.geojson')
    geoms = [feature["geometry"] for feature in shapes.__geo_interface__["features"]]

    # Apply the mask (crop) and save the cropped image
    out_image, out_transform = mask(src, geoms, crop=True)
    out_meta = src.meta.copy()
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})

    with rasterio.open('cropped_image.tif', 'w', **out_meta) as dest:
        dest.write(out_image)
