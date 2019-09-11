# Libraries
from dotenv import load_dotenv              # Load env file
from os import getenv                       # Get env variables
from sys import argv                        # Argument vector
from requests import post, get              # Post to endpoint, get remote image
import json                                 # Transform respond to json format
from io import BytesIO                      # Convert bytes-like objects to bytes objects
from PIL import Image                       # Open image to display
import matplotlib.pyplot as plt             # Show image and extracted text

# Load values of env file
load_dotenv(".env")
base_endpoint = getenv('base_endpoint')
subscription_key = getenv('subscription_key')

# Local and remote images
local_image = "input/explosion.jpg"
remote_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

# Post request and response
source = argv[1]
analyze_url = base_endpoint + "analyze"
params = {'visualFeatures': 'Categories,Description,Color'}
if source == "local":
    image_data = open(local_image, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = post(analyze_url, headers=headers, params=params, data=image_data)
else:
    data = {'url': remote_image}
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    response = post(analyze_url, headers=headers, params=params, json=data)
resp_json = response.json()

# Print response on JSON format
#print(json.dumps(resp_json, indent=4, sort_keys=True))

# Extract and print text
text = resp_json["description"]["captions"][0]["text"].capitalize()
print(text)

# Write output text
output_file = "output/" + source + ".txt"
f = open(output_file,"w") 
f.write(text) 
f.close()

# Display the image and the captions
if source == "local":
    image = Image.open(local_image)
else:
    image = Image.open(BytesIO(get(remote_image).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(text, size="x-large", y=-0.1)
plt.show()