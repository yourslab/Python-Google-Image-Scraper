import urllib2
import urllib
import simplejson
from urlparse import urlparse
from os.path import splitext, basename

my_file = open("list.txt", "r")

increment = 0;
for line in my_file:
	url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
	'v=1.0&rsz=8&start=0&q='+line)
	url = urllib.quote(url, safe="%/:=&?~#+!$,;'@()*[]")

	request = urllib2.Request(url, None, {'Referer': 'facebook.com'})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)
	# now have some fun with the results...
	for i in range(0, 8):
		picture = results['responseData']['results'][i]['unescapedUrl']
		disassembled = urlparse(picture)
		filename, file_ext = splitext(basename(disassembled.path))
		urllib.urlretrieve(results['responseData']['results'][i]['unescapedUrl'], 
		str(increment)+'_'+str(i)+file_ext)

	increment = increment + 1


my_file.close()