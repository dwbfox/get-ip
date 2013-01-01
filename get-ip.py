'''
	Author: Biru
	Date: 12/20/2011	
'''

def get_ip():
    import re
    import urllib2
    try:
        data = urllib2.urlopen('http://checkip.dyndns.org/').read()
        match = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').search(data)
        return match.group(0)
    except:
    	return False




if __name__ == '__main__':
    print "Your current IP address is: %s" % get_ip()