#!/usr/bin/python3

import feedparser


feedlist = {'footmercato': 'https://www.footmercato.net/flux-rss',
            'espn': 'https://www.espn.com/espn/rss/news',
            }

while True:
    i = 0
    for key, value in feedlist.items():
        print("{} - {}".format(i, key))
        i += 1

    x = input('\nChoose a Feed or q to quit: ')
    if x == 'q':
        break
    values = list(feedlist.values())
    try:
        feed = feedparser.parse(values[int(x)])['entries']
    except:
        exit

    while True:

        i = 0
        for value in feed:
            print("{} - {}".format(i, value['title']))
            i += 1

        x = input('\nChoose a News or press q to return: ')
        if x == 'q':
            break
        try:
            summary = feed[int(x)]['summary']
            print("\n{}".format(summary))
            wait = input("\nPress Enter to continue.")
        except:
            exit
