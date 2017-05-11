#Web Crawler that goes downloads all vgcats comics

import scrapy
from requests import get

#created mysqldb vgcat.comic
#need to save comics into comics folder

class QuotesSpider(scrapy.Spider):
    name = "vgcats"
    start_urls = [
        'http://www.vgcats.com/comics/',
    ]

    def parse(self, response):
        #locates jpeg extension
        pic = response.css('div img').re(r'(images\/\d*.(gif|jpg))')
        #name of the file is the release date of the comic
        name = pic[0].split('/')
        yr, mo, da,  = name[:2], name[2:4], name[4:7]

        #combines url with jpeg extension
        comic = QuotesSpider.start_urls[0] + pic[0]

        #downloads and save comic
        a = get(comic)
        f = open("{0}".format(name[1]), 'wb')
        for chunk in a.iter_content(10000):
            f.write(chunk)
        f.close()

        #http://www.vgcats.com/comics/?strip_id=0    first comic, increments will need to check and stop download if see duplicate

        #recursion to keep download all comics
        #<div align="center">
        #<a href="?strip_id=385"><img src="next.gif" border="0"></a>
        next_page = response.css('div a::attr(href)').extract_first() #?strip_id=385
        #checks if it is the first comic
        if next_page[-1].isdigit():
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



