import requests
import csv
import json
from collections import deque as dq
import os

mod_library = {
    '1700_1989': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271807/20131128-mod-whitehall-library-resources-1700to1989.csv'
    ,'1990_1999': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271806/20131128-mod-whitehall-library-resources-1990to1999.csv'
    ,'2000_2009': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271807/20131128-mod-whitehall-library-resources-2000to2009.csv'
    ,'2010_2013': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271807/20131128-mod-whitehall-library-resources-2010to2013.csv'
}
endpoints = {
    'court_martial': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/425580/20150501-Court_Martial_Results_Jan2010-Apr2015_MCSOM-O.csv'
    ,'non_inhabited': 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/403177/2015-non-inhabited-buildings-mod-estate-clean.csv'
}

output = []
for url in mod_library:
    data = requests.get(mod_library[url])
    #with open('mod_library/'+url+'.csv', 'w') as file:
    #    file.write(data.text)
    with open('mod_library/'+url+'.csv', 'r') as file:
        csv_reader = csv.reader(file)
        rows = [
            row for row in csv_reader if len(row) > 0
        ]
        print(rows[0:3])
    print('processed', url)