import json
from collections import Counter

from graphviz import Digraph

from src.crawler import Crawler


class LinkMiner:
    data = None

    def __init__(self, sources: list, targets: list):
        self.crawler = Crawler(sources=sources, targets=targets)
        self.graph = Digraph(strict=True, engine='circo')
        self.graph.graph_attr['overlap'] = 'false'

    def extract(self):
        self.data = self.crawler.run()
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

    def export_json(self, filename):
        string = json.dumps(self.data['edges'])
        with open(f'{filename}.json', 'w') as file:
            file.write(string)
