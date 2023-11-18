import requests
from lxml import etree

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Referer': 'http://www.baidu.com/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
out_url = 'https://www.fancai.com/cxi1030300'
source_url = 'https://www.fancai.com/'
result_list = []


for i in range(0,2):
	if i == 0:
		out_url = out_url
	else:
		out_url = out_url + '_' + str(i)



	'''找菜名'''
	r = requests.get(out_url, headers=headers)
	content = r.content.decode('utf-8')
	# print(r.content.decode('utf-8'))

	html = etree.HTML(content)
	titles = html.xpath('//div[@class="pic"]/a/@title')
	hrefs = html.xpath('//div[@class="pic"]/a/@href')
	# print(hrefs)


	'''点进去找主料+做法'''
	for j in range(len(hrefs)):
		data_dict = {}
		data_dict['id'] = hrefs[j]
		data_dict['name'] = titles[j]

		inr  = requests.get(source_url+hrefs[j],headers=headers)
		incontent = inr.content.decode('utf-8')
		# print(incontent)
		inhtml = etree.HTML(incontent)

		main_foods = inhtml.xpath('//div[@class="ddd_div clearfix"]//li[@class="shi_list_name"]/a/text()')
		# print(main_food)
		how_to_dos = inhtml.xpath('//table[@class="menucont_step"]//td/p/text()')
		# print(how_to_dos)

		data_dict['main_food'] = main_foods
		data_dict['how_to_do'] = how_to_dos

		result_list.append(data_dict)

print(result_list)


