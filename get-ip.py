def get_ip():
    import re
    import urllib.request as req
    try:
        data = req.urlopen('http://checkip.dyndns.org/').read()
        match = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').search(data.decode('utf-8'))
        return match.group(0)
    except Exception as err:
    	raise Exception("Error: {}".format(err))




if __name__ == '__main__':
    print ("Your current IP address is: %s" % get_ip())
