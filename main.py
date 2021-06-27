from tika import parser
import requests
import os

file_data = parser.from_file("C:/Users/DUAN/Desktop/ningen_shikkaku.pdf")
text = file_data["content"].replace("\n", "")
print(text)

parameter = {
    "key":os.environ.get("key"),
    "hl":"ja-jp",
    "c":"MP3",
    "v":"Hina",
    "src": text[26:200],
}

response = requests.get(url="http://api.voicerss.org?", params=parameter)
print( response.url)

