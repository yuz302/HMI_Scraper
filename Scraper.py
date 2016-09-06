import urllib2
import re


def getHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


def getProductName(html):
    prod_re = r'<p id="prod">(.*?)</p>'
    prod_match = re.findall(prod_re, html,re.S|re.M)
    return prod_match

def getProductBatchNumber(html):
    prod_re = r'<p id="prodbatch">(.*?)</p>'
    prod_match = re.findall(prod_re, html, re.S | re.M)
    return prod_match

if __name__ == '__main__':
    url = 'http://10.10.10.123/user/andon.htm'
    html = getHtml(url)
    print getProductName(html)[0]
    print getProductBatchNumber(html)[0]

