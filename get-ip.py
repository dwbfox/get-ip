'''
	Author: Biru
'''

import re
import urllib2

def get_ip():

    try:
        data = urllib2.urlopen('http://checkip.dyndns.org/').read()
        match = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').search(data)
        return match.group(0)
    except:
    	return False




if __name__ == '__main__':

    address = get_ip()

    if address:
        print "Your current IP address is: %s" % address
    else:
        print "Unable to determine your IP address"