#!/usr/bin/env python

# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
import os

command = 'twurl -t ' + '\"' + '/1.1/search/tweets.json?q=nra&geocode=33.509045,-86.836930,500mi' + '\"' + ' > out.json'
os.system(command)
