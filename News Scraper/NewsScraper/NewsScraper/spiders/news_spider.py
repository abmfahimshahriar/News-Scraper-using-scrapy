import scrapy
from ..items import NewsscraperItem


class NewsSpider(scrapy.Spider):
    name = 'spidy'

    #start_urls = ['https://www.bbc.com/']

    # user will input the website url
    start_urls = [input("Enter the website url:")]


    # parser function that will crawl the website
    def parse(self, response):

        items = NewsscraperItem()

        all_blocks = response.css("li.media-list__item")

        for q in all_blocks:

            # CSS selector to fetch specific data from website
            news_title = str(q.css("a.block-link__overlay-link::text").extract())
            news_link = str(q.css("a.block-link__overlay-link").xpath("@href").extract())
            news_article = str(q.css("div.media__content").css("p.media__summary::text").extract())
            news_tag = str(q.css("div.media__content").css("a.media__tag::text").extract())

            if ('corona' or 'Corona' or 'virus' or 'Covid') in news_title:
                # data will be stored in the items
                items['news_title'] = news_title
                items['news_link'] = news_link
                items['news_article'] = news_article
                items['news_tag'] = news_tag
                yield items

            elif ('corona' or 'Corona' or 'virus' or 'Covid') in news_article:
                     # data will be stored in the items
                    items['news_title'] = news_title
                    items['news_link'] = news_link
                    items['news_article'] = news_article
                    items['news_tag'] = news_tag
                    yield items







# cd NewsScraper
# scrapy crawl spidy

