import requests
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14719441169074583706"

r = requests.get(url.format(72650))

data = r.text

soup = BeautifulSoup(data, 'lxml')

usr = soup.find('div', id='gs_sa_ccl')
indusr = soup.findAll("usr", {"class": "gsc_1usr"})
sing = indusr[1]
print(sing)
