import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta    # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# same_ages = list(db.users.find({'title': '월-E'}))
# print(same_ages)
# all_data=db.movies.find_many({})
# print(all_data)

wallE = db.movies.find_one({'title': '월-E'})
print(wallE['star'])




# MongoDB에서 특정 조건의 데이터 모두 보기

# same_ages = list(db.users.find({'age': 40}))

same_star = list(db.movies.find({'star': wallE['star']}, {'_id':False}))
print(same_star)

# 반복문을 돌며 모든 결과값을 보기
for mov in same_star:
    print(mov['title'])

# db.movies.update_many({ '$star': o })
db.movies.update_many({'star': '9.41' }, {'$set': {'star': '0'}})