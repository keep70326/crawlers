import requests


re = requests.get('https://airtw.epa.gov.tw/json/AQI/Taiwan_2022070413.json')
if re.status_code == requests.codes.ok:
    data = re.json()
    # pprint.pprint(data)
    # print(data[0]['txt'])

    for AQI in data:
        area, aqi = (AQI['txt'].split())

        if '(二氧化氮)' in aqi:
            aqi, no2 = aqi.split('(')

        print(f'地區:{area}   aqi:{aqi}')

