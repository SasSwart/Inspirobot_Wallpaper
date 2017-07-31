import urllib.request as request

site= "http://inspirobot.me/api?generate=true"  # This is the api link that returns a link to the generated image

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

# I'm just printing the string to terminal. I suggest you use it to get the image into a python image object
# and use your existing code from there.
print(content)
