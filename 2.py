import os
import sys
import pygame
import requests

f = input()
geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
response = requests.get(geocoder_request)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
f = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
response = requests.get(geocoder_request, )
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
qwe = toponym['boundedBy']['Envelope']
w = list(map(float, qwe['lowerCorner'].split()))
q = list(map(float, qwe['upperCorner'].split()))
x = (q[0] - w[0]) / 2
c = (q[1] - w[1]) / 2
map_request = "http://static-maps.yandex.ru/1.x/?ll=" + toponym_coodrinates.replace(" ", ",") + "&spn=" + str(
    x) + ',' + str(c) + "&l=map"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()

screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN and event.key == 119 and x < 10 and c < 10:
            x += 0.01
            c += 0.01
            map_request = "http://static-maps.yandex.ru/1.x/?ll=" + toponym_coodrinates.replace(" ",
                                                                                                ",") + "&spn=" + str(
                x) + ',' + str(c) + "&l=map"
            response = requests.get(map_request)
            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
        if event.type == pygame.KEYDOWN and event.key == 115 and x > 0.02 and c > 0.02:
            x -= 0.01
            c -= 0.01
            map_request = "http://static-maps.yandex.ru/1.x/?ll=" + toponym_coodrinates.replace(" ",
                                                                                                ",") + "&spn=" + str(
                x) + ',' + str(c) + "&l=map"
            response = requests.get(map_request)
            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()
os.remove(map_file)