# Locate Traffic Lights

_Locate Traffic Lights_ detects traffic lights and their locations from images using computer vision.


## Features

The results is a map with junctions having traffic lights. A list of identified traffic lights in a structured format is also generated.

<img src="https://github.com/aavista/locate-traffic-lights/blob/master/locate-traffic-lights-example-map.png?raw=true" width="410">


Main features:

- Detect traffic lights from images, for example taken by mobile phone.
- Locate the location based on image's [Exif](https://en.wikipedia.org/wiki/Exif) properties
- Create a map with locations having traffic lights (HTML format)
- Create a summary of locations with traffic lights and their confidence levels (CSV and JSON formats)  


## Sample

Sample images are found under [samples/images](https://github.com/aavista/locate-traffic-lights/tree/master/samples/images). 

An example map and summary from a test run are available in [samples/results](https://github.com/aavista/locate-traffic-lights/tree/master/samples/results).


## Prerequisites

The following prerequisites apply to images to be analyzed:

- Location services must be enabled before taking the photos.
- WiFi must be enabled before taking the photos. Nearby WiFi stations may improve the location accuracy.
- Images must be placed to a directory.
- Images must be in JPG or PNG format.


## Limitations

The following limitations exist when detecting objects from images:

- All the GPS features may not be available in all the mobile phone models. For example GPS direction or GPS positioning error included in the image properties are not always present in the image's Exif details.
- Accuracy of the location depends on several factors such as GPS signal, vicinity of operator's base stations, nearby buildings etc.
- Images taken without active SIM card will get more inaccurate location.


## Installation

Verify the following prerequisites:

- Python 3.6 or newer is required. 
- [Virtual environment](https://docs.python.org/3/tutorial/venv.html) `venv` is recommended, but not mandatory. 

The scripts use the following machine learning libraries:

- [OpenCV](https://docs.opencv.org/master/index.html)
- [TensorFlow](https://www.tensorflow.org)

Install required Python packages:

```
pip3 install -r requirements.txt
```


## Usage

Update directory paths and other settings in `config.ini` file.

Place the images to be analyzed to the directory specified in `config.ini`. 

Run the following command to analyze the images.

```python
python3 analyze-images.py
```

The analysis results will be created in the directory as specified in `config.ini`.

**Note!** During the first run, loading the computer vision library can take several minutes. The initialization of the library happens only once so subsequent processing will be faster. 


## Roadmap

Roadmap includes the following items.

- **Identify different types of traffic lights** - Identify different types of traffic lights: vehicle vs. tram vs. cyclist vs. arrow traffic lights
- **Blur images to comply to GDPR requirements** - All persons and vehicle licence plates detected on the images must be blurred.
- **More accurate image clustering** - The same objects might appear on multiple images. Improve the clustering mechanism to remove duplicate images from the results.


## Questions and feedback

Feature requests and issues can be provided via the project's [issue tracker](https://github.com/aavista/locate-traffic-lights/issues).


## Contributing

Anyone is welcome to contribute to this repository. If you would like to make a change, open [a pull request](https://github.com/aavista/locate-traffic-lights/pulls) for the repository.


## Credits

The scripts were developed by [Aavista](https://aavista.com) during UrbanSense 5G Edge pilot. The pilot was part of [UrbanSense 5G Innovation Platform](https://forumvirium.fi/en/urbansense-5g-innovation-platform/) from [Forum Virium Helsinki](https://forumvirium.fi/en/).


