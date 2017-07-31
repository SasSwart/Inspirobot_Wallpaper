from urllib import request
from PIL import Image
import requests
from io import BytesIO

# This function gets the modal colour of the image
def get_main_color(img_colour):
    colors = img_colour.getcolors(2048000) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

site = "http://inspirobot.me/api?generate=true"# This is the api link that returns a link to the generated image
# These headers are required for the api to return an image. If they are not included an Error 403 (Forbidden) is returned
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


req = request.Request(site, headers=hdr)  # Create the appropriate request
page = request.urlopen(req)               # Download the file that contains the link to the image
content = page.read().decode('utf-8')     # Decode the link from a byte string to str using utf-8

response = requests.get(content)
img = Image.open(BytesIO(response.content))# This enables PIL to get the image from a URL

old_size = img.size
new_size = (1366, 768) # Change to your respective screen dimensions
new_img = Image.new('RGB', new_size, get_main_color(img))
new_img.paste(img, ((new_size[0] - old_size[0]) // 2, (new_size[1] - old_size[1]) // 2))
new_img.save('/home/rob/Downloads/NewBack.jpg') # Change to respective system directory, and make sure bash script points to the same directory.
