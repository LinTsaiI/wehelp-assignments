# 要求一：Python 取得網路上的資料並儲存到檔案中
import urllib.request as requests
import json
src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
with requests.urlopen(src) as response:
  data = json.load(response)

attractions = data['result']['results']

with open('data.csv', 'w', encoding = 'utf-8') as file:
  for i in range(len(attractions)):
    img = attractions[i]['file'].replace('https', ' https').split()
    result = (attractions[i]['stitle']+', '
              + attractions[i]['address'][5:8]+', '
              + attractions[i]['longitude']+', '
              + attractions[i]['latitude']+', '
              + img[0] + '\n')
    file.write(result)