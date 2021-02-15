import os
import sys
import pygame
import requests

pygame.init()

screen = pygame.display.set_mode((600, 490))
screen.fill((44, 47, 51))
pygame.display.flip()
run = 1
font = pygame.font.Font(None, 20)
f2 = 1
m = ''
while run:
    if f2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.KEYDOWN and 58 > event.key > 47:
                m += str(event.key - 48)
            if event.type == pygame.KEYDOWN and event.key == 44:
                m += ','
            if event.type == pygame.KEYDOWN and event.key == 46:
                m += '.'
            if event.type == pygame.KEYDOWN and event.key == 8:
                m = m[:-1]
            if event.type == pygame.KEYDOWN and event.key == 13:
                try:
                    f = m
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
                    response = requests.get(geocoder_request)
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    f = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
                    response = requests.get(geocoder_request, )
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"].split()
                    qwe = toponym['boundedBy']['Envelope']
                    w = list(map(float, qwe['lowerCorner'].split()))
                    q = list(map(float, qwe['upperCorner'].split()))
                    x = (q[0] - w[0]) / 2
                    c = (q[1] - w[1]) / 2
                    q = 'map'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
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
                    f2 = 0
                except Exception:
                    pass
            screen.fill((44, 47, 51))
            text = font.render(m, True, (240, 240, 240))
            screen.blit(text, (0, 0))
            pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 55 and event.pos[0] <= 123 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'sat'
                    toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) - 0.05)
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request)
                    if not response:
                        print("Ошибка выполнения запроса:")
                        print(map_request)
                        print("Http статус:", response.status_code, "(", response.reason, ")")
                        sys.exit(1)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                if event.pos[0] >= 137 and event.pos[0] <= 185 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'map'
                    toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) - 0.05)
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request)
                    if not response:
                        print("Ошибка выполнения запроса:")
                        print(map_request)
                        print("Http статус:", response.status_code, "(", response.reason, ")")
                        sys.exit(1)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                if event.pos[0] >= 191 and event.pos[0] <= 239 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'sat,skl'
                    toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) - 0.05)
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request)
                    if not response:
                        print("Ошибка выполнения запроса:")
                        print(map_request)
                        print("Http статус:", response.status_code, "(", response.reason, ")")
                        sys.exit(1)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 276 and float(toponym_coodrinates[0]) > 0.5:
                toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) - 0.05)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 275 and float(toponym_coodrinates[0]) < 179.5:
                toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) + 0.05)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 274 and float(toponym_coodrinates[1]) > 0.5:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) - 0.025)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 273 and float(toponym_coodrinates[1]) < 89.5:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) + 0.025)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
        pygame.draw.rect(screen, (39, 42, 46), [(55, 460), (68, 20)])
        text = font.render("Спутник", True, (240, 240, 240))
        screen.blit(text, (59, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(133, 460), (48, 20)])
        text = font.render("Схема", True, (240, 240, 240))
        screen.blit(text, (137, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(191, 460), (58, 20)])
        text = font.render("Гибрид", True, (240, 240, 240))
        screen.blit(text, (195, 462))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
pygame.quit()
os.remove(map_file)