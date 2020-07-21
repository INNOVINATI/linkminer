from collections import Counter
from urllib.parse import urlparse

from graphviz import Digraph

from src.crawler import Crawler


class Miner:
    data = None

    def __init__(self, from_urls, to_domains):
        self.sources = set([urlparse(url).netloc for url in from_urls])
        self.crawler = Crawler(urls=from_urls, domains=to_domains)
        self.graph = Digraph(strict=True, engine='circo')
        self.graph.graph_attr['overlap'] = 'false'

    def extract(self):
        self.data = self.crawler.run()
        nodes = Counter(self.data['nodes'])
        top = max(nodes.values())
        for node in nodes.keys():
            self.graph.node(node, node, **{
                'size': str(max([nodes[node], top / 4])),
                'fontsize': str(max([nodes[node], top / 4]))
            })
        for edge in self.data['edges']:
            self.graph.edge(edge['source'], edge['target'])

    def render(self, filename='untitled'):
        self.graph.render(f'{filename}.gv', view=True)

    def export(self, filename, ftype='csv'):
        pass
