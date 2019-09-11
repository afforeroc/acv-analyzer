---
topic: 
  - Sample
languages:
  - Python 
products:
  - Azure
---

# Sample Solution that uses image analyzer of Azure Computer Vision
This **Python** code is a quickstart that show how to use **image analyzer** of **Computer Vision API** for local and remote images

## Prerequisites
- [Python 3.7.4+](https://www.python.org/)
- [An Azure Subscription Key](https://portal.azure.com/#home)
- [A Computer Vision Instance](https://azure.microsoft.com/en-us/try/cognitive-services/?api=computer-vision)

## Setup
1. Clone or download this sample repository
2. Open your console on cloned folder
3. Install required libraries for **Python**
```
pip install -r requirements.txt
```
4. Modify the *.env* file with your **Computer Vision** credentials

## Running the sample
1. Run the sample using a local image
```
python acv-analyze.py local
```
2. Run the sample using a remote image
```
python acv-analyze.py remote
```

## Images Sources
* Local image: [Nuclear explosion on Nevada](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Quote.JPG/320px-Quote.JPG)
* Remote image: [Broadway and Times Square by night](https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg)

## Documentation
* [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
* [Quickstart: Analyze a local image using the Computer Vision REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-disk)
* [Quickstart: Analyze a remote image using the Computer Vision REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-analyze)