
import urllib2
response = urllib2.urlopen('http://10.10.10.123/user/andon.htm')
html = response.read()
print html
