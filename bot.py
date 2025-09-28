import gspread
from oauth2client.service_account import ServiceAccountCredentials

import datetime
import tweepy
import time
import pandas

def convert(date_time):
    format = '%m/%d/%Y %H:%M:%S' # The format
    datetime_str =  pandas.to_datetime(date_time, format=format).replace(tzinfo=None) - datetime.timedelta(hours=8, minutes=0)

    return datetime_str

def processing():
  
  ACCESS_KEY = '1485209990721908736-PPj1QijddKVBsEBfggqBIwBcO37skp'
  ACCESS_SECRET = 'lBD4mjKVZ10dgqGC7jtDBYhbSoPtNxioVCPRntqiGXcSK'
  CONSUMER_KEY = 'bGXl7IRLNw7hXCK15sTPscKmo'
  CONSUMER_SECRET = '6AbCrIvmurnNklc1XqvT8ZirlVFsgGs42hm23B1rWQsu3TqM10'
  
  scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
           "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
  
  
  # Assign credentials ann path of style sheet
  creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
  client = gspread.authorize(creds)
  sheet = client.open("Twitter").sheet1
  
  dateofpublishing = sheet.col_values(1)
  tweet = sheet.col_values(2)
  url = sheet.col_values(3)
  hashtag = sheet.col_values(4)
  status = sheet.col_values(5)
  
  print(status)

  while len(dateofpublishing) != 1:
      for index, date in enumerate(dateofpublishing):
          if date == "Date Time":
              continue
          print(date, convert(date).replace(tzinfo=None) )
          if convert(date).replace(tzinfo=None) == datetime.datetime.utcnow().replace(microsecond=0) or (convert(date).replace(tzinfo=None) <= datetime.datetime.utcnow().replace(microsecond=0) and status[index] != "Posted"):
              api = tweepy.Client(access_token=ACCESS_KEY,
                                  access_token_secret=ACCESS_SECRET,
                                  consumer_key=CONSUMER_KEY,
                                  consumer_secret=CONSUMER_SECRET)
              hashtags = " #".join(list(hashtag[index].replace(" ", "").split(",")))
  
              api.create_tweet(text=f"{tweet[index]}\n{url[index]}\n#{ hashtags }")
              sheet.update(f'F{index+1}', 'Posted')
              print("done")
              dateofpublishing = sheet.col_values(1)
              tweet = sheet.col_values(2)
              url = sheet.col_values(3)
              hashtag = sheet.col_values(4)
              status = sheet.col_values(5)
  
      time.sleep(10)
