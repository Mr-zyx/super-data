import scrapy
import bs4
from ..items import JavbooksItem


class JavbooksSpider(scrapy.Spider):
    name = 'javbooks'
    allowed_domains = ['https://zz2143.com', "zz2143.com"]
    start_urls = ['https://zz2143.com/content_censored/1.htm']

    page = 1
    page_url = 'https://zz2143.com/content_censored/%d.htm'

    def parse(self, response):
        print('start parse # %d av' % self.page)
        javbook_item = JavbooksItem()
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        javbook_item['url'] = self.page_url % self.page
        javbook_item['title'] = bs.find('div', id='title').find('b').string
        javbook_item['cover_img'] = bs.find('div', class_='info_cg').find('img')['src']

        info_boxs = bs.find_all('div', class_='infobox')
        javbook_item['serial'] = info_boxs[0].find('a').string if info_boxs[0].find('a') is not None else None
        javbook_item['publish_time'] = info_boxs[1].contents[1] if len(info_boxs[1].contents) > 1 else None
        javbook_item['duration'] = info_boxs[2].contents[1] if len(info_boxs[2].contents) > 1 else None
        director_info = info_boxs[3].find('a')
        if director_info is not None:
            javbook_item['director'] = {"name": director_info.string, "url": director_info['href']}
        producer_info = info_boxs[4].find('a')
        if producer_info is not None:
            javbook_item['producer'] = {"name": producer_info.string, "url": producer_info['href']}
        publisher_info = info_boxs[5].find('a')
        if publisher_info is not None:
            javbook_item['publisher'] = {"name": publisher_info.string, "url": publisher_info['href']}
        series_info = info_boxs[6].find('a')
        if series_info is not None:
            javbook_item['series'] = {"name": series_info.string, "url": series_info['href']}
        categories = info_boxs[7].find_all('a')
        if categories is not None:
            javbook_item['categories'] = list(map(lambda i: {"name": i.string, "url": i['href']}, categories))

        actresses = info_boxs[8].find_all('div', class_='av_performer_cg_box')
        if actresses is not None:
            javbook_item['actress'] = []
            for actress in actresses:
                if actress.find('div', class_='av_performer_name_box') is not None and \
                        actress.find('div', class_='av_performer_name_box').find('a') is not None:
                    javbook_item['actress'].append(
                        {"name": actress.find('div', class_='av_performer_name_box').find('a').string,
                         "img": actress.find('img')['src'],
                         "url": actress.find('div', class_='av_performer_name_box').find('a')['href']})

        gallery_info = bs.find('div', class_='gallery')
        if gallery_info is not None:
            galleries = gallery_info.find_all('div', class_='hvr-grow')
            if galleries is not None:
                javbook_item['galleries'] = list(map(lambda i: i.find('a')['href'], galleries))

        yield javbook_item

        if javbook_item['title'] is not None:
            self.page += 1
            next_page_url = self.page_url % self.page
            yield scrapy.Request(url=next_page_url, callback=self.parse)
