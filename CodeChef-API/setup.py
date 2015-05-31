try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(
    name='codechef',
    version='0.1.0',
    description='Fetches and parses data from CodeChef',
    long_description=long_description,
    author='vicky002',
    url='https://github.com/vicky002/CodeChef-API',
    packages=['codechef'],
    install_requires=[
        "beautifulsoup4 == 4.3.2",
        "feedparser == 5.1.3",
        "requests == 2.5.0"
    ]
)
