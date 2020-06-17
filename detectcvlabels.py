import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os

TRAFFIC_LIGHT_LABEL = 'traffic light'
BOXED_PREFIX = 'boxed-'
RESULT_SUBDIR = 'images'

def verify_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def detect_cv_labels(photo, result_path):
    im = cv2.imread(photo)
    bbox, label, conf = cv.detect_common_objects(im)
    prediction = get_cv_labels(photo, bbox, label, conf)

    # Verify that result directory exists
    verify_directory(result_path + RESULT_SUBDIR)

    # Create image with bounding boxes
    boxed_image = draw_bbox(im, bbox, label, conf)
    cv2.imwrite(result_path + RESULT_SUBDIR + os.path.sep + BOXED_PREFIX + photo, boxed_image)
    return prediction


def get_cv_labels(photo, boxes, labels, confidences):
    trafficLightCount = 0
    confidenceMean = 0
    confidenceMax = 0
    all = []
    i = 0
    for label in labels:
        if label == TRAFFIC_LIGHT_LABEL:
            trafficLightCount = trafficLightCount + 1
            confidenceMean = confidenceMean + confidences[i]
            if confidences[i] > confidenceMax:
                confidenceMax = confidences[i]
        label = {
            'label': label,
            'confidence': confidences[i],
            'boundingBox': boxes[i]
        }
        i = i + 1
        all.append(label)

    if trafficLightCount > 0:
        confidenceMean = round ((confidenceMean / trafficLightCount), 3)
    prediction = {
        'image': photo,
        'boxedImage': BOXED_PREFIX + photo,
        'labelCount': len(labels),
        'trafficLightCount': trafficLightCount,
        'trafficLightConfidenceMax': round(confidenceMax, 3),
        'trafficLightConfidenceMean': confidenceMean,
        'labels': labels,
        'response': all
    }
    return prediction
