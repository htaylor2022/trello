# Written by Hayden Taylor, 8/27/2018
import requests
import json

# Authentication
api_key = ''
TOKEN = ''


# Functions
def getBoards():
    req = requests.get('https://api.trello.com/1/members/me/boards?key={}&token={}'.format(api_key, TOKEN))
    jresponse = json.loads(req.text)

    boards = []

    for i in jresponse:
        boards.append({"name" : i['name'], "id" : i['id'], "link" : i['url']})

    return boards
def getLists(boardID):
    req = requests.get('https://api.trello.com//1/boards/{}/lists?key={}&token={}'.format(boardID, api_key, TOKEN))
    jresponse = json.loads(req.text)

    lists = []

    for i in jresponse:
        lists.append({"name" : i['name'], "listId" : i['id']})

    return lists
def getCards(boardID, listID):
    req = requests.get('https://api.trello.com/1/lists/{}/cards?key={}&token={}'.format(listID, api_key, TOKEN))
    jresponse = json.loads(req.text)
    cards = []

    for i in jresponse:
        cards.append({"cardId" : i['id'], "name" : i['name'], "description" : i['desc'], "link" : i['shortUrl']})

    return cards
