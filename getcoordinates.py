from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS
from PIL import Image
import math

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):

    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):
    
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):

    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    direction = get_image_direction(geotags)
    pos_error = get_positioning_error(geotags)

    return lat, lon, direction, pos_error

def get_image_direction(geotags):

    # If image does not include direction, initialize with default value (-1 denotes here uninitialized value)
    degree = -1

    # Direction is a value from 0 - 360, from magnetic North clockwise
    if 'GPSImgDirection' in geotags:    
        dir1, dir2 = geotags['GPSImgDirection']
        degree = round((dir1 / dir2), 0)
    return degree

def get_positioning_error(geotags):

    # If image does not include positioning error, initialize with default value (-1 denotes here uninitialized value)
    error = -1

    if 'GPSHPositioningError' in geotags:
        err1, err2 = geotags['GPSHPositioningError']
        error = round((err1 / err2), 1)
    return error
