# Libraries for reading environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Libraries for post requesting and json manipulating 
import requests
import json

# Libraries for data visualization
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Using ".env" file to obtain credentials 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables
vision_base_url = os.getenv('vision_base_url')
subscription_key = os.getenv('subscription_key')
assert subscription_key

# Using OCR service
analyze_url = vision_base_url + "analyze"

# Set image_path that you want to analyze
image_path = "broadway.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}

# Put the byte array into your post request
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(json.dumps(response.json()))
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(image_path)
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()