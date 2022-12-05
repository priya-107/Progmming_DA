print("Hello World")
import requests
url='https://www.the-numbers.com/market/2022/summary'
r=requests.get(url)
# headers={'<tr><th>Rank</th><th>Movie</th><th>Release<br>Date</th><th>Distributor</th><th>Genre</th><th>2022<br>Gross</th><th>Tickets<br>Sold</th></tr>'}
# r=requests.get(url,headers=headers)
print(r.content)
