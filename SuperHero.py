import requests
import json


def superhero(heroes):
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    results = {}
    for one_hero in heroes:
        responce = requests.get(url + one_hero)
        text = json.loads(responce.text)
        for name_hero in text['results']:
            if name_hero['name'] == one_hero:
                results[one_hero] = int(name_hero['powerstats']['intelligence'])
                break
    return max(results, key=results.get)


heroes_dist = {'Hulk', 'Captain America', 'Thanos'}
print(superhero(heroes_dist))
