# linkminer
A simple tool to find and visualise links between two sets of websites built with Scrapy and Graphviz

## About
`linkminer` uses the power of Scrapy to build a higher-level network graph based on two sets of URLs which is then visualised with Graphviz. We are using this tool internally for Competitive Intelligence, i.e. when we want to find out which customers
have some kind of relationship with specific competitors.

## Getting started
Install via PyPi:
```bash
pip install linkminer
```
Install via Git:
```bash
git clone https://github.com/INNOVINATI/linkminer.git
cd linkminer-master
virtualenv venv #Optional
source venv/bin/activate #Optional
pip setup.py install
```
## Usage
Extract links from 2 given sets of URLs:
```python
from linkminer.miner import LinkMiner

source_urls = [...]
target_urls = [...]

m = LinkMiner(source_urls, target_urls)
m.extract()
```
Render the graph:
```python
m.render('testfile')
```
Export graph and data as JSON file:
```python
m.export_json('testfile')
```