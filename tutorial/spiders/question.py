import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import QuestionItem


class QuestionSpider(scrapy.Spider):
    """docstring for QuestionSpider."""
    name = 'question'

    start_urls = [
    'https://produto.mercadolivre.com.br/MLB-1276156185-corpo-borboleta-tbi-gol-fox-10-flex-030133062d-original-t-_JM'
    ]

    def parse(self, response):
        for question in response.xpath("//li[@class='questions__group  questions__group--1 ']"):
            l = ItemLoader(item=QuestionItem(), selector=question)
            l.add_xpath('content', ".//div[@class='questions__content']/p")
            l.add_xpath('url', ".//div[@class='questions__content']/a/@href")
        yield l.load_item()

    print('asdfasdfa')

