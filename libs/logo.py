# coding=utf-8
#!/usr/bin/env python3

from libs.animation import colorText

logo = '''

[[black-bright-background]][[red]] ██▓ [[green]]███▄    █  [[blue]] ██████ [[magenta]]▄▄▄█████▓ [[cyan]]▄▄▄         [[red]] ██▀███  [[green]]▓█████ [[blue]] ██▓███   [[magenta]]▒█████   [[cyan]]██▀███  [[yellow]]▄▄▄█████▓[[reset]]
[[black-bright-background]][[red]]▓██▒ [[green]]██ ▀█   █ ▒[[blue]]██    ▒ [[magenta]]▓  ██▒ ▓▒▒[[cyan]]████▄       [[red]]▓██ ▒ ██▒[[green]]▓█   ▀ [[blue]]▓██░  ██▒▒[[magenta]]██▒  ██▒▓[[cyan]]██ ▒ ██▒[[yellow]]▓  ██▒ ▓▒[[reset]]
[[black-bright-background]][[red]]▒██▒▓[[green]]██  ▀█ ██▒░[[blue]] ▓██▄   [[magenta]]▒ ▓██░ ▒░▒[[cyan]]██  ▀█▄     [[red]]▓██ ░▄█ ▒[[green]]▒███   [[blue]]▓██░ ██▓▒▒[[magenta]]██░  ██▒▓[[cyan]]██ ░▄█ ▒[[yellow]]▒ ▓██░ ▒░[[reset]]
[[black-bright-background]][[red]]░██░▓[[green]]██▒  ▐▌██▒ [[blue]] ▒   ██▒[[magenta]]░ ▓██▓ ░ ░[[cyan]]██▄▄▄▄██    [[red]]▒██▀▀█▄  [[green]]▒▓█  ▄ [[blue]]▒██▄█▓▒ ▒▒[[magenta]]██   ██░▒[[cyan]]██▀▀█▄  [[yellow]]░ ▓██▓ ░ [[reset]]
[[black-bright-background]][[red]]░██░▒[[green]]██░   ▓██░▒[[blue]]██████▒▒[[magenta]]  ▒██▒ ░  [[cyan]]▓█   ▓██▒   [[red]]░██▓ ▒██▒[[green]]░▒████▒[[blue]]▒██▒ ░  ░░[[magenta]] ████▓▒░░[[cyan]]██▓ ▒██▒[[yellow]]  ▒██▒ ░ [[reset]]
[[black-bright-background]][[red]]░▓  ░[[green]] ▒░   ▒ ▒ ▒[[blue]] ▒▓▒ ▒ ░[[magenta]]  ▒ ░░    [[cyan]]▒▒   ▓▒█░   [[red]]░ ▒▓ ░▒▓░[[green]]░░ ▒░ ░[[blue]]▒▓▒░ ░  ░░[[magenta]] ▒░▒░▒░ ░[[cyan]] ▒▓ ░▒▓░[[yellow]]  ▒ ░░   [[reset]]
[[black-bright-background]][[red]] ▒ ░░[[green]] ░░   ░ ▒░░[[blue]] ░▒  ░ ░[[magenta]]    ░     [[cyan]] ▒   ▒▒ ░   [[red]]  ░▒ ░ ▒░[[green]] ░ ░  ░[[blue]]░▒ ░      [[magenta]] ░ ▒ ▒░  [[cyan]] ░▒ ░ ▒░[[yellow]]    ░    [[reset]]
[[black-bright-background]][[red]] ▒ ░ [[green]]  ░   ░ ░ ░[[blue]]  ░  ░  [[magenta]]  ░       [[cyan]] ░   ▒      [[red]]  ░░   ░ [[green]]   ░   [[blue]]░░       ░[[magenta]] ░ ░ ▒   [[cyan]] ░░   ░ [[yellow]]  ░      [[reset]]
[[black-bright-background]][[red]] ░   [[green]]        ░  [[blue]]     ░  [[magenta]]          [[cyan]]     ░  ░   [[red]]   ░     [[green]]   ░  ░[[blue]]          [[magenta]]   ░ ░   [[cyan]]  ░     [[yellow]]         [[reset]]
                                                                                                  

                                           [[black-bright-background]][[white]]Codded By losinguh[[reset]]
                                            [[black]]Version :- 3.01[[reset]]

                                           [[red]]Telegram :- [[blue]]@losinguhhh[[reset]]
                                       [[red]]Instagram:- [[blue]]@losinguh[[reset]]
'''

def print_logo():
    print(colorText(logo))