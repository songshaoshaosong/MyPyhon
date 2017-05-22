import urllib
import urllib2
url='wwww.baidu.com'
request=urllib.urlopen(url)
print request.read()