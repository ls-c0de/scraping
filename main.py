#!/usr/bin/env/python3
import tools
import workshop
import datetime

base_url = "https://www.zalando.de/tiger-of-sweden/" #This is the base url from where the program starts feeding URLs
filter = "https://www.zalando.de/tiger-of-sweden"

raw_urls = workshop.feeder(base_url, filter)
urls_to_parse = []

counter = 0
for x in raw_urls:
    if counter % 2 == 0:
        urls_to_parse.append(raw_urls[counter])
        #print(urls_to_parse)
    counter += 1

counter = 0
while counter < 80:
    print('URL :', urls_to_parse[counter])
    tools.download_and_parse(urls_to_parse[counter])
    counter += 1

x = datetime.datetime.now()
print('Finished Script - Next in 24 hours')
print(x)

