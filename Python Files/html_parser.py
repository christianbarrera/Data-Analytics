from bs4 import BeautifulSoup

f = open("pge_meter_details.html", encoding='utf-8')
file = f.read()


soup = BeautifulSoup(file, 'html.parser')

# data = []
div = soup.find('div', {'class': 'module-body sa-info'})
print(type(div))
i = 0
# while True:
# 	if "Service ID:" in div.find_all('li')[i].text.strip():
# 		break
# 	value = div.find_all('li')[i]
# 	print(value.text.strip().replace("\n", " ").replace("  ", ""))
# 	i += 1
while "Service ID:" not in div.find_all('li')[i].text.strip():
	value = div.find_all('li')[i]
	print(value.text.strip().replace("\n", " ").replace("  ", ""))
	i += 1
	
	

# value1 = div.find_all('li')[0]
# print(value1.text.strip())

# value2 = div.find_all('li')[1]
# # value2.sub(r"\n", " ")
# # value2 = value2.replace(" ", "")
# value2 = value2.text.strip().replace("\n", " ").replace("  ", "")
# print(value2)

# print(type(value2.text.strip()))


rates = soup.find('div', {'class': 'module-body', 'style': 'padding-bottom: 60px;'})
# print(rates)
# print(rates.find('h3'))
# for rate in rates.find('h3'):
# 	print("\n" + rate.strip())
print("\n" + rates.find('h3').text.strip())