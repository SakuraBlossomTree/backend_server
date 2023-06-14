__author__ = "eskyozar"

from bs4 import BeautifulSoup
import urllib.request


class Booru:
    @staticmethod
    def get_url(url):
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response,features="xml")
        return soup

    def parse(self):
        raise NotImplementedError("parse() method not implemented.")


class Gelbooru(Booru):
    base_url = "http://gelbooru.com"
    api_url = "/index.php?page=dapi&s=post&q=index&tags={0}&limit={1}"

    def __init__(self, tags, limit):
        self.url = self.base_url + self.api_url.format(tags, limit)

    def parse(self):
        img_key = 'post'
        data = super().get_url(self.url)
        links = [dict(post.attrs)['file_url'] for post in data.findAll(img_key)]
        return links


class SafeBooru(Gelbooru):
    base_url = "http://safebooru.org"

    def __init__(self, tags, limit):
        super().__init__(tags, limit)

