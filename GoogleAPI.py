# Imports the Google Cloud client library
from google.cloud import language_v1
import tweepy
import Keys  # .py file that store all necessary keys
import json  # To write file as json format

# I use Google NLP to score the sentiment of Taylor Swift
def Google_senti(file_name):
    client = language_v1.LanguageServiceClient()
    output = []
    out_filename = "taylor.json"
    Tweets_text = open(out_filename, 'w')
    with open(file_name) as f:
        data = json.loads(f.read())
        for tw in data:
            try:
                tw_data = {}
                # The text to analyze
                text = tw['text']
                document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                # Detects the sentiment of the text
                sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
                tw_data['name'] = tw['user']['name']
                tw_data['moment'] = tw['created_at'][0:19]
                tw_data['text'] = tw['text']
                tw_data['sentiment.score'] = sentiment.score
                tw_data['sentiment.magnitude'] = sentiment.magnitude
                #print("Text: {}".format(text))
                #print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
                output.append(tw_data)
            except:
                pass
    json.dump(output, Tweets_text, indent=4)
    Tweets_text.close

def Authorization_Setup():
    auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret) #pass customer keys
    auth.set_access_token(Keys.access_token, Keys.access_token_secret) #pass access_token and access_token_secret
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api #generate the api

# Write tweets information to file as json format.!!!
def Write_tweets_to_File(Input_list, target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w')
    for status in Input_list:
        data.append(status._json)
    json.dump(data, Tweets_text, indent=4)
    Tweets_text.close

# get several numbers of tweets from a certain user, use api.user_timeline() from tweepy!
def Get_User_Timeline(api, ID, Count_Number):
    user_tweets_list = api.user_timeline(id=ID, count=Count_Number)#id is user name
    # store result into a jason file
    #print (user_tweets_list)
    Write_tweets_to_File(user_tweets_list, 'user_tweets')
    return user_tweets_list

if __name__ == "__main__":
    API = Authorization_Setup()
    User_Tweets = Get_User_Timeline(API,'@taylorswift13',10)
    output = Google_senti('user_tweets.json')
