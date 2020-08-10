import json
import glob
import os

with open('images.json', 'r') as f:
    image_config = json.load(f)

for image_filename in glob.glob('./images/*.jpg'):
    print(f"Adding {os.path.basename(image_filename)}")
    image_config['pics'].append({
        'basename': os.path.basename(image_filename),
        'date': '2020',
        'description': 'butt farts'
    })

with open('images.json', 'w+') as f:
    json.dump(image_config, f)
