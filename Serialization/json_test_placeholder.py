import requests
import csv

url = 'https://jsonplaceholder.typicode.com/users'
data = requests.get(url)
dataJ = data.json()

for x in dataJ:
    name = x['name']
    address = x['address']
    city = address['city']
    gpsCord = address['geo']
    gpsLat = gpsCord['lat']
    gpsLong = gpsCord['lng']
    company = x['company']
    companyName = company['name']
    gpsCordf = f'({gpsLat},{gpsLong})'
    with open('jsontest1.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        csvdata = (name, city, companyName, gpsCordf)
        print(csvdata)
        writer.writerow(csvdata)



