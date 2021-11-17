from TikTokApi import TikTokApi
import pprint
from datetime import datetime
import requests
import json
import time
import pytz

api = TikTokApi()

project = requests.get('')
json_project = project.json()
idkeyword = json_project['idkeyword']
idproject = json_project['idproject']
alias = json_project['alias_kyword']
keyword = json_project['keyword_tiktok']
project_name = json_project['project_name']

user_videos = api.by_username(keyword)

user_id = user_videos[0]['author']['id']
avatar = user_videos[0]['author']['avatarLarger']
username = user_videos[0]['author']['uniqueId']
bio = user_videos[0]['author']['signature']
video_count = user_videos[0]['authorStats']['videoCount']
followers = user_videos[0]['authorStats']['followerCount']

inputanprof = {

  }
print(inputanprof)
postprofile = requests.post("", data=json.dumps(inputanprof))


count_videos = len(user_videos)
i = 0
while i < count_videos:
  print(i)
  i += 1
  var_id = str(user_videos[i]['id'])+"_"+str(idproject)
  var_code = str(user_videos[i]['id'])
  var_image = str("")
  var_text = str(user_videos[i]['desc'])
  var_like = int(user_videos[i]['stats']['diggCount'])
  var_comment = int(user_videos[i]['stats']['commentCount'])
  var_view = int(user_videos[i]['stats']['playCount'])
  var_share = int(user_videos[i]['stats']['shareCount'])
  var_keyword = str(alias)
  split_postingtime = str("")
  datepost=int(user_videos[i]['createTime'])
  utcdate = pytz.utc.localize(datetime.utcfromtimestamp(datepost))
  dtp=str(utcdate)
  splitdate=dtp.split(" ")
  postingdate=splitdate[0]

  posts = {

    }
  print(posts)
  res = requests.post("", data=json.dumps(posts))
  time.sleep(5)