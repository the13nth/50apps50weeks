import http.client
import json
#import timer
import time
#start timer

start_time = time.time()
#
conn = http.client.HTTPSConnection("irembo.gov.rw")
payload = ''
headers = {
  'plateNumber': '',
  'tin': ''
}
conn.request("GET", "/irembo/rest/public/police/request/retrieve/traffic-fines-by-plate-number-and-tin", payload, headers)
print('Hold on while we check your vehicle data')
res = conn.getresponse()
data = res.read()
#print(data.message)
json_object = json.loads(data)
print(json_object["message"])
#display timer
print("data fetched in"" %s seconds " % (time.time() - start_time))
