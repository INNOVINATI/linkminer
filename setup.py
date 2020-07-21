from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='linkminer',
    version='0.1.0',
    description='A simple tool to find and visualise links between two sets of websites built with Scrapy and Graphviz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/INNOVINATI/linkminer',
    author='Maximilian Wolf / INNOVINATI',
    author_email='info@innovinati.com',
    keywords='link scraping, marketing, competitive intelligence, scrapy, graphviz',
    package_dir={'': 'src'},
    python_requires='>=3.5, <4',
    install_requires=['scrapy', 'graphviz'],
)
