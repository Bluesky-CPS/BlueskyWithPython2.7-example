import httplib, urllib, urllib2

# Identify your bluesky domain
# Example: localhost
your_bluesky_domain = 'localhost:8189'
# Identify your embedded device IP address
your_local_ed_ip = '172.16.4.222'

# Get the connecting devices. Return data as the JSON format.
#params = urllib.urlencode({'instruction': 'ls', 'opt1': 'noneFix', 'opt2': 'edconnected'})
conn = httplib.HTTPConnection(your_bluesky_domain)
conn.request("GET", "/ETLog?instruction=ls&opt1=noneFix&opt2=edconnected", headers={'Content-Type':'text/html'})
r1 = conn.getresponse()
data = r1.read()
print data
print "---------------------------------------------"

# Login to the system as public account
for num in range(2):
    url = 'http://' + your_bluesky_domain + '/doLogin.ins'
    values = {'username' : 'guest',
          'password' : 'guest',
          'mode' : 'signin'}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    signinResult = response.read()
    print signinResult

print "---------------------------------------------"

# Do something by API
conn = httplib.HTTPConnection(your_bluesky_domain)
conn.request("GET", "/ETLog?instruction=sensornetwork&opt1=" + your_local_ed_ip + "&opt2=gpio&opt3=set&opt4=22&opt5=0", headers={'Content-Type':'text/html'})
r2 = conn.getresponse()
data = r2.read()
print data

print "---------------------------------------------"


# Logout from the system public account
for num in range(2):
    url = 'http://' + your_bluesky_domain + '/doLogout.ins'
    values = {'username' : 'guest',
              'mode' : 'signout'}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    signoutResult = response.read()
    print signoutResult

print "---------------------------------------------"
