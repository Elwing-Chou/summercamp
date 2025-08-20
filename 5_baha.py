import json
import urllib.request as req
import pandas as pd

pageurl = "https://ani.gamer.com.tw/animeVideo.php?sn=36632"
r = req.Request(pageurl)
r.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0")
f = req.urlopen(r)
content = f.read()
print(content)

# 上個的
# list+dict: JSON
url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=36632&geo=TW%2CHK"
f = req.urlopen(url)
content = f.read()
content = json.loads(content)

danmu = content["data"]["danmu"]
df = pd.DataFrame(danmu)
# print(df)
df.to_excel("danmu.xlsx")