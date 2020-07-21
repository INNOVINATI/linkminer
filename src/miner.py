from collections import Counter

from graphviz import Digraph

from src.crawler import Crawler


class Miner:
    data = None

    def __init__(self, sources: list, targets: list):
        self.crawler = Crawler(sources=sources, targets=targets)
        self.graph = Digraph(strict=True, engine='circo')
        self.graph.graph_attr['overlap'] = 'false'

    def extract(self, deep=False):
        self.data = self.crawler.run(deep=deep)
        nodes = Counter(self.data['nodes'])
        top = max(nodes.values())
        for node in nodes.keys():
            self.graph.node(node, node, **{
                'size': str(max([nodes[node], int(top/4)])),
                'fontsize': str(max([nodes[node], int(top/4)]))
            })
        for edge in self.data['edges']:
            self.graph.edge(edge['source'], edge['target'])

    def render(self, filename='untitled'):
        self.graph.render(f'{filename}.gv', view=True)

    def export(self, filename, ftype='csv'):
        pass
