import sqlite3

import pymongo

client = pymongo.MongoClient('mongodb://st:askldjwq@185.93.109.237:27019/?authSource=goscatalog')
db = client.goscatalog  # Выбираем базу данных
myc = db.chebykina
conn = sqlite3.connect('netflix.sqlite')
# for row in conn.execute("select * from netflix_titles"):
#  show_id, type, title, director, cast, country, date_added,
#  release_year, rating, duration, listed_in, description = row
#  res = myc.insert_one({"show_id" : show_id, "type" : type, "title" : title, "director": director,
#                     "cast": cast, "country": country, "date_added":date_added, "release_year":release_year,
#                    "rating": rating, "duration":duration, "listed_in": listed_in, "description": description})
one = myc.find()
one = list(one)
for i in one:
    print(i)
