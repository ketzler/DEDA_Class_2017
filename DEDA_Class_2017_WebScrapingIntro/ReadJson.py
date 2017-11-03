import requests
import json

response = requests.get("http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000352-001")
content = response.content
json_tree = json.loads(content)

for bike_rent_records in json_tree["result"]["records"]:
    leftRatio = float(bike_rent_records["sbi"]) / float(bike_rent_records["tot"]) * 100
    print("ID:{0} Left:{2:%0.1f} Name:{1}".format(bike_rent_records["sno"], bike_rent_records["aren"], leftRatio))