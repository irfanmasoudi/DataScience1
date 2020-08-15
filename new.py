from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020,8,14)
end_date = dt.date(2020,8,15)

limit = 1000
lang = 'english'

tweets = query_tweets("AC Milan", begindate=begin_date,enddate=end_date,limit=limit,lang=lang)


