#!/usr/bin/python3
# rss feed teminal reader

import feedparser


feedlist = {'zdnet': 'https://www.zdnet.com/news/rss.xml',
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
            link = feed[int(x)]['link']
            print("\n{}\n".format(feed[int(x)]['title']))
            print("\n{}".format(summary))
            print("\n{}".format(link))
            wait = input("\nPress Enter to continue.")
        except:
            exit
