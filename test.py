import requests
import json

start_time = '2019-01-01'
end_time = '2027-01-01'


data = {
    "pet_id": 0,
    "consumer_id": 2078,
    "bill_state": 0,
    "start": start_time,
    "end": end_time,
    "project_type": 0
}


print(json.dumps(data))