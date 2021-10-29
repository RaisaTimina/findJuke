import diff as diff
from flask import Flask, jsonify, render_template
import requests
from collections import Counter

app = Flask(__name__)


@app.route('/searchBySettingsId')
def searchBySettingsId():
    jsonJuke = requests.get('http://my-json-server.typicode.com/touchtunes/tech-assignment/jukes')
    jsonJuke.raise_for_status()
    jsonResponseJuke = jsonJuke.json()

    jsonSettings = requests.get('http://my-json-server.typicode.com/touchtunes/tech-assignment/settings')
    jsonSettings.raise_for_status()
    jsonResponseSettings = jsonSettings.json()
    groundZero = jsonResponseSettings['settings']

    settingID = "9ac2d388-0f1b-4137-8415-02b953dd76f7"
    RequiredSettings = []

    for y in groundZero:
        if y['id'] == settingID:
            print(y['requires'])
            for j in y['requires']:
                RequiredSettings.append(j)
    for y in jsonResponseJuke:
        CheckedComponentSet = set()
        for component in y['components']:
            CheckedComponentSet.add(component['name'])
        c = list((Counter(CheckedComponentSet) & Counter(RequiredSettings)).elements())

        if RequiredSettings == c:
            print("found: ")
            print(y['id'])
            print()

    return "found"


@app.route('/searchByModel')
def searchByModel():
    jsonJuke = requests.get('http://my-json-server.typicode.com/touchtunes/tech-assignment/jukes')
    jsonJuke.raise_for_status()
    jsonResponseJuke = jsonJuke.json()

    jsonSettings = requests.get('http://my-json-server.typicode.com/touchtunes/tech-assignment/settings')
    jsonSettings.raise_for_status()
    jsonResponseSettings = jsonSettings.json()
    groundZero = jsonResponseSettings['settings']

    jukeModel = "angelina"
    RequiredSettings = []

    for x in jsonResponseJuke:
        if x['model'] == jukeModel:
            # print(x['id'])
            # print(x['model'])
            # print()
            CheckedComponentSet = set()
            for y in groundZero:
                for j in y['requires']:
                    RequiredSettings.append(j)
            for component in x['components']:
                CheckedComponentSet.add(component['name'])
                # print(CheckedComponentSet)
        c = list((Counter(CheckedComponentSet) & Counter(RequiredSettings)).elements())
            # print(c)
        if RequiredSettings == c:
            print("found: ")
            print(y['id'])
            print()

    return "found"


if __name__ == '__main__':
    app.run()
