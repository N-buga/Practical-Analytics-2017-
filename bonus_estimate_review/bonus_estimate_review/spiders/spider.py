import scrapy

class ScrappyBanks(scrapy.Spider):
    name = "bank_spider"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ScrappyBanks, self).__init__(*args, **kwargs)
        for i in range(1, 1000):
            self.start_urls.append('https://www.banki.ru/services/responses/list/?page={}'.format(i))
    
    def parse(self, response):
        for link in response.css("div.responses__item__message > a::attr(href)"):
            yield response.follow(link, self.review_parse)

    def review_parse(self, response):
        url = response.url
        text = response.css("div.article-text::text").extract_first()
        mark = response.css("span.rating-grade > meta::attr(content)").extract_first()
        yield {
            'url': url,
            'text': text,
            'mark': mark
        }
