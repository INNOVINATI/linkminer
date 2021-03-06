from urllib.parse import urlparse

from scrapy import Request, Item, Field
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider as BaseSpider
from scrapy.linkextractors import LinkExtractor


NODES = []
EDGES = []


class Link(Item):
    from_subpage = Field()
    to_subpage = Field()
    source = Field()
    target = Field()


class Pipeline:
    def process_item(self, item, spider):
        item['source'] = urlparse(item['from_subpage']).netloc
        item['target'] = urlparse(item['to_subpage']).netloc
        NODES.extend([item['source'], item['target']])
        EDGES.append(item)


class Spider(BaseSpider):
    name = 'linkminer'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={'root': url})

    def parse(self, response):
        extract_links = LinkExtractor(allow_domains=self.allowed_domains, unique=True).extract_links(response)
        follow_links = LinkExtractor(allow=(), deny_domains=self.allowed_domains, unique=True).extract_links(response)
        for link in follow_links:
            yield Request(link.url, callback=self.parse, meta=response.meta)
        for link in extract_links:
            item = Link()
            item['from_subpage'] = response.url
            item['to_subpage'] = link.url
            yield item


class Crawler:
    def __init__(self, sources, targets):
        self.sources = sources
        self.targets = [urlparse(url).netloc for url in targets]
        self.engine = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
            'LOG_LEVEL': 'INFO',
            'ITEM_PIPELINES': {'src.crawler.Pipeline': 100},
            'COOKIES_ENABLED': False,
            'DOWNLOAD_TIMEOUT': 15,
            'RETRY_ENABLED': False,
        })

    def run(self):
        self.engine.crawl(Spider, start_urls=self.sources, allowed_domains=self.targets)
        self.engine.start()
        return {'nodes': NODES, 'edges': EDGES}

