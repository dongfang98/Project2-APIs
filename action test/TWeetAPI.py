import tweepy
#import Keys  # .py file that store all necessary keys
import json  # To write file as json format
import os
import sys

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
def Authorization_Setup():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except Exception:
        sys.exit("Reach limit, cannot connect to API")


# Print out tweets' text.!!!
def Display_tweets(Input_list):
    tweet_text_list = []
    for status in Input_list:
        tweet_text_list.append(status.text)
        print(status.text, end="\n\n")
    return tweet_text_list


# Write tweets information to file as json format.!!!
def Write_tweets_to_File(Input_list, target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w')
    for status in Input_list:
        data.append(status._json)
    json.dump(data, Tweets_text, indent=4)
    Tweets_text.close


# return tweets sent by author(me),use api.home_timeline() from tweepy!
def GET_My_Home_tweets(api):
    My_Home_tweets = api.home_timeline()
    #print (My_Home_tweets)
    # store result in a jason file called 'my_tweets'
    Write_tweets_to_File(My_Home_tweets, 'my_tweets')
    data = []
    for status in My_Home_tweets:
        data.append(status._json)
    return data


# get several numbers of tweets from a certain user, use api.user_timeline() from tweepy!
def Get_User_Timeline(api, ID, Count_Number):
    user_tweets_list = api.user_timeline(id=ID, count=Count_Number)#id is user name
    # store result into a jason file
    #print (user_tweets_list)
    Write_tweets_to_File(user_tweets_list, 'user_tweets')
    return user_tweets_list


# search tweets according to content, use api.search_tweets from tweepy
def GET_Search_Tweets(api, Target_content, search_type, Count_Number, Time):
    Result_Tweets = api.search_tweets(q=Target_content, result_type=search_type, count=Count_Number, until=Time)
    Display_tweets(Result_Tweets)
    Write_tweets_to_File(Result_Tweets, 'Search_tweets')
    data = []
    for status in Result_Tweets:
        data.append(status._json)
    return data


# Search tweets based on Hashtag and time.
def GET_Hashtag_Search_Tweets(Local_API, Hashtag, Count_Number, Time_before):
    Hashtag_Tweets = tweepy.Cursor(Local_API.search_tweets, q=Hashtag, count=Count_Number, since=Time_before)
    Write_tweets_to_File(Hashtag_Tweets.items(), 'Hashtag_Tweets')
    for status in Hashtag_Tweets.items():
        print(status.text)
    return Hashtag_Tweets

# Update the authenticated user’s status
def update_tweets(api, content):
    api.update_status(content)
    print('sucessfully sended')
    return content

# Add and delete friends
def add_friends(api, ID):
    api.create_friendship(id = ID)
    print('sucessfully added')
    return ID

def delete_friends(api, ID):
    api.destroy_friendship(id = ID)
    print('sucessfully deleted')
    return ID

if __name__ == "__main__":
    API = Authorization_Setup()
    Home_Tweets = GET_My_Home_tweets(API)
    User_Tweets = Get_User_Timeline(API,'@taylorswift13',10)
    Result_Tweets = GET_Search_Tweets(API, "Joe Biden", "recent", 1, "2021-10-29")
    #print(Result_Tweets)
    #GET_Hashtag_Search_Tweets(API,"#Trump",5,"2020-09-30")
    #add_friend = add_friends(API, '@keduck250')
    #delete_friend = delete_friends(API, '@keduck250')
    #API.create_list(name = 'ldf')
    #Update_Status = update_tweets(API, 'Happy everyday!')
