import requests
import json
import datetime
import csv



def parodyk_ora(vieta, kiek_dienu=1):
    # API_RAKTAS = "107920573936472908188x1695"
    HTP = "https://geocode.xyz/"
    payload = {'locate': f'{vieta}', "json" :1 ,"auth" :API_RAKTAS}
    r = requests.get(HTP, params=payload)
    r.url
    r.text
    res = json.loads(r.text)
    # print(res)
    long = res["longt"]
    lat =res["latt"]

    HTP = "https://api.open-meteo.com"
    endpoint = "/v1/forecast"
    payload = {"latitude": f"{lat}", "longitude": f"{long}", "forecast_days": kiek_dienu,
               "hourly": "temperature_2m,rain", "current_weather": True}
    r = requests.get(HTP + endpoint, params=payload)
    r.url
    res = json.loads(r.text)
    #     print(res)
    oras_codas = res["current_weather"]["weathercode"]

    orai = {"0": "Clear sky",
            "1": "Mainly clear, partly cloudy, and overcast",
            "2": "Mainly clear, partly cloudy, and overcast",
            "3": "Mainly clear, partly cloudy, and overcast",
            "45": "Fog and depositing rime fog",
            "48": "Fog and depositing rime fog",
            "51": "Drizzle: Light, moderate, and dense intensity",
            "53": "Drizzle: Light, moderate, and dense intensity",
            "55": "Drizzle: Light, moderate, and dense intensity",
            "56": "Freezing Drizzle: Light and dense intensity",
            "57": "Freezing Drizzle: Light and dense intensity",
            "61": "Rain: Slight, moderate and heavy intensity",
            "63": "Rain: Slight, moderate and heavy intensity",
            "65": "Rain: Slight, moderate and heavy intensity",
            "66": "Freezing Rain: Light and heavy intensity",
            "67": "Freezing Rain: Light and heavy intensity",
            "71": "Snow fall: Slight, moderate, and heavy intensity",
            "73": "Snow fall: Slight, moderate, and heavy intensity",
            "75": "Snow fall: Slight, moderate, and heavy intensity",
            "77": "Snow grains",
            "80": "Rain showers: Slight, moderate, and violent",
            "81": "Rain showers: Slight, moderate, and violent",
            "83": "Rain showers: Slight, moderate, and violent",
            "85": "Snow showers slight and heavy",
            "86": "Snow showers slight and heavy",
            "95 *": "Thunderstorm: Slight or moderate",
            "96": "Thunderstorm with slight and heavy hail",
            "99": "Thunderstorm with slight and heavy hail"}
    dabar_oras = orai[str(oras_codas)]
    dabar_valanda = str(datetime.datetime.now())[10:13]

    x = 0
    for data in res["hourly"]["time"]:
        laikas = str(data)[11:13]
        if int(dabar_valanda) == int(laikas):
            l = f'{data}, Temperatura: {res["hourly"]["temperature_2m"][x]}, Krituliai: {res["hourly"]["rain"][x]}, {dabar_oras}'
            return l
        x += 1


def temp_val(vieta, kiek_dienu=1):
    # API_RAKTAS = "107920573936472908188x1695"
    HTP = "https://geocode.xyz/"
    payload = {'locate': f'{vieta}', "json": 1, "auth": API_RAKTAS}
    r = requests.get(HTP, params=payload)
    r.url
    r.text
    res = json.loads(r.text)
    # print(res)
    long = res["longt"]
    lat = res["latt"]

    HTP = "https://api.open-meteo.com"
    endpoint = "/v1/forecast"
    payload = {"latitude": f"{lat}", "longitude": f"{long}", "forecast_days": kiek_dienu,
               "hourly": "temperature_2m,rain", "current_weather": True}
    r = requests.get(HTP + endpoint, params=payload)
    r.url
    res = json.loads(r.text)
    #     print(res)
    oras_codas = res["current_weather"]["weathercode"]

    orai = {"0": "Clear sky",
            "1": "Mainly clear, partly cloudy, and overcast",
            "2": "Mainly clear, partly cloudy, and overcast",
            "3": "Mainly clear, partly cloudy, and overcast",
            "45": "Fog and depositing rime fog",
            "48": "Fog and depositing rime fog",
            "51": "Drizzle: Light, moderate, and dense intensity",
            "53": "Drizzle: Light, moderate, and dense intensity",
            "55": "Drizzle: Light, moderate, and dense intensity",
            "56": "Freezing Drizzle: Light and dense intensity",
            "57": "Freezing Drizzle: Light and dense intensity",
            "61": "Rain: Slight, moderate and heavy intensity",
            "63": "Rain: Slight, moderate and heavy intensity",
            "65": "Rain: Slight, moderate and heavy intensity",
            "66": "Freezing Rain: Light and heavy intensity",
            "67": "Freezing Rain: Light and heavy intensity",
            "71": "Snow fall: Slight, moderate, and heavy intensity",
            "73": "Snow fall: Slight, moderate, and heavy intensity",
            "75": "Snow fall: Slight, moderate, and heavy intensity",
            "77": "Snow grains",
            "80": "Rain showers: Slight, moderate, and violent",
            "81": "Rain showers: Slight, moderate, and violent",
            "83": "Rain showers: Slight, moderate, and violent",
            "85": "Snow showers slight and heavy",
            "86": "Snow showers slight and heavy",
            "95 *": "Thunderstorm: Slight or moderate",
            "96": "Thunderstorm with slight and heavy hail",
            "99": "Thunderstorm with slight and heavy hail"}
    dabar_oras = orai[str(oras_codas)]
    dabar_valanda = str(datetime.datetime.now())[10:13]

    x = 0
    listas = []
    for data in res["hourly"]["time"]:
        # return f' Data: {data}, Temperatura: {res["hourly"]["temperature_2m"][x]}'
        stringasoro = f'Data: {data}, Temperatura: {res["hourly"]["temperature_2m"][x]}'
        listas.append(stringasoro)
        # print(data, res["hourly"]["temperature_2m"][x])
        x += 1
    return listas


# tempval = temp_val("Vilnius")
# print(tempval)
#
# tempval2 = parodyk_ora("Vilnius")
# print(tempval2)