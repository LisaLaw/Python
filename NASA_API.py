import requests, json

api_key = 'cird5aG2wNKg8dru4KbyB8e9BZ8veQLC3AM5FzPl'
account_id = '5fa22a2b-1a5b-4c48-891b-05eaa5670bb2'

api_url = 'https://api.nasa.gov/neo/rest/v1/feed?'

print("")
user_date = input('Enter a date in the format of YYYY-MM-DD: ')

params = {
    'start_date' : user_date,
    'end_date' : user_date,
    'api_key' : api_key,
}

response = requests.get(api_url, params=params) #get data from webpage, encoding the params dictionary above

obj = json.loads(response.text) #serialize data
#print(json.dumps(obj, indent=2)) #print all data in readable fashion

print('On ' + user_date + ' there were ' + str(obj['element_count']) + ' asteroids registered with NASA.') #access total amount of asteroids on user_date
print("")

hazardous_count = 0 #initialize count for hazardous asteroids

for item in obj['near_earth_objects'][user_date]: #access all data under user_date
    hazard = item['is_potentially_hazardous_asteroid'] #access hazardous data
    if hazard == True :
        hazardous_count = hazardous_count + 1

print('Of those, ' + str(hazardous_count) + ' were potentially hazardous.')