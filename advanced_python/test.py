from PIL import Image
import time
import json
import requests
r = requests.get("https://newsapi.org/v2/everything?q=share market&apiKey=ca70daf086124e3fa70bfe6db70ba10e")
f = json.loads(r.text)
s = f["articles"]
def function_is(str):
    from win32com.client import Dispatch
    hello = Dispatch("SAPI.spVoice")
    hello.Speak(str)
def show_image(url):
    im = Image.open(requests.get(url,stream=True).raw)
    im.show()
    time.sleep(5)
    im.close()
print("""
1.titles
2.content
3.description
""")
sp = input("sir please input what you want to liste(1/2/3)")
if sp == "1":
    f = 1
    for i in s:
        print(f"the title {f}th is "+i["title"])
        function_is(f"the title {f}th is "+i["title"])
        f+=1