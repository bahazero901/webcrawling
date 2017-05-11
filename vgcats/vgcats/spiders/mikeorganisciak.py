#Web Crawler that goes downloads all vgcats comics

import scrapy
from requests import get as download


class QuotesSpider(scrapy.Spider):
    name = "mikeorganisciak"
    start_urls = [
        'http://mikeorganisciak.com/',
    ]

    def parse(self, response):
        for pics in response.css('div img::attr(src)').re(r'.*.jpg'):
            pic = download(pics)
            f = open("{0}".format(pics.split('/')[-1]), 'wb')
            for chunk in pic.iter_content(10000):
                f.write(chunk)
            f.close()

        #http://www.vgcats.com/comics/?strip_id=0    first comic, increments will need to check and stop download if see duplicate

        #recursion to keep download all comics
        #<div align="center">
        #<a href="?strip_id=385"><img src="next.gif" border="0"></a>
        next_page = response.css('div a::attr(href)').re(r'.*page.*')[0]
        #checks if it is the first comic
        if next_page is None:
            yield scrapy.Request(next_page, callback=self.parse)



