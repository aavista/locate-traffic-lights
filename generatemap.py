import pandas as pd 

import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium import IFrame
import os
import base64

RESULT_SUBDIR = 'images'

def drop_empty_images(df):

    # Drop images which do not include any traffic lights
    df_updated = df[df['trafficLightCount'] > 0]
    return df_updated

def create_clustered_map(image_path, df, result_path, topic):
    tiles = 'cartodbpositron'
    color = 'Blue'
    center = (60.19, 24.94)

    df_updated = drop_empty_images(df)
    m = folium.Map(location=center, zoom_start=3, tiles=tiles, attr=tiles)

    marker_cluster = MarkerCluster().add_to(m)

    # Add points to the map
    for idx, row in df_updated.iterrows():
        Marker([row['lat'], row['lon']], popup=add_popup(result_path, row)
        ).add_to(marker_cluster)

    # Display the map
    html_file = topic + '.html'
    m.save(os.path.join(result_path, html_file))

def add_popup(image_path, row):
    image = row['image']
    boxedImage = 'boxedImage'
    if boxedImage in row and row['boxedImage'] is not 'None':
        image = RESULT_SUBDIR + os.path.sep + row['boxedImage'] 
    encoded = base64.b64encode(open(image_path + image , 'rb').read())

    # Produce content for popup with embedded image
    text = '<p>Traffic lights: ' + str(row['trafficLightCount']) + '</p><p>Max confidence: ' + str(row['trafficLightConfidenceMax']) +\
        '</p><p>Direction: ' + str(row['direction']) + '</p><p>' + row['image'] + '</p>'
    header = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
    image = '<img src="data:image/JPEG;base64,{}" class="rounded float-left img-thumbnail">'
    content = header + text + image
    html = content.format

    iframe = IFrame(html(encoded.decode("UTF-8")), width=960, height=540)
    popup = folium.Popup(iframe, max_width=1920)

    return popup
