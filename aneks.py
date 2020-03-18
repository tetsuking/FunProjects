# -*- coding: utf-8 -*-
говно ебаное

import base_class
import requests
import lxml.html
class acb(base_class.public_command):
    """docstring for ."""
    #html_tree = ""
    command = "!анек"
    resourse = ""
    anek =""
    def __init__(self, url="https://baneks.ru/random"):
        self.url = url

    def get_anek (self):
        self.anek = ""
        r = requests.get(self.url)
        html = lxml.html.fromstring(r.content)
        title = html.xpath('.//article//p//text()')
        with open('fit_ha.txt', 'w', encoding='utf-8') as f:
            for text in title:
                self.anek += text
        return self.anek

    def load(self):
        return {"command": self.get_anek}

    def exec(self):
        print ("lol")


def main():
    p = acb()
    p.get_anek()

if __name__ == '__main__':
    main()
