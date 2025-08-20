import json
import urllib.request as req
import pandas as pd
import bs4 as bs

pageurl = "https://ani.gamer.com.tw/animeVideo.php?sn=36632"
r = req.Request(pageurl)
r.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0")
f = req.urlopen(r)
content = f.read()
# print(content)
html = bs.BeautifulSoup(content)
links = html.find_all("a")
# !!!!!!!
total = []
for l in links:
    href = l["href"]
    if href.startswith("?sn="):
        # print(href)
        # !!!!
        sn = href.split("=")[-1]
        url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=" + sn + "&geo=TW%2CHK"
        print(url)
        f = req.urlopen(url)
        content = f.read()
        content = json.loads(content)
        # !!!
        danmu = content["data"]["danmu"]
        total = total + danmu
df = pd.DataFrame(total)
# df.to_excel("danmu.xlsx")
df.to_csv("danmu.csv", encoding="utf-8")