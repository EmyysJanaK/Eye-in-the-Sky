import numpy as np

# Load the cropped image and normalize pixel values
with rasterio.open('cropped_image.tif') as src:
    image = src.read().astype(np.float32)
    normalized_image = (image - image.min()) / (image.max() - image.min())

    # Save the normalized image
    normalized_meta = src.meta
    with rasterio.open('normalized_image.tif', 'w', **normalized_meta) as dest:
        dest.write(normalized_image)
