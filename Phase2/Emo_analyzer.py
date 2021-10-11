#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template#The template engine, renders templates
from flask import request
from flask_restful import Api,Resource
import requests
import json
import os,re
import requests
from bs4 import BeautifulSoup
# Imports the Google Cloud client library
from google.cloud import language_v1
import tweepy
import Keys  # .py file that store all necessary keys
#python -m pip i

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')


# save the byte->json problem
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


# news ingester: search with key words and return relevent content in today's news from CBS
@app.route('/useremo', methods = ['GET', 'POST'])
def useremo():
    def Google_senti(file_name):
        client = language_v1.LanguageServiceClient()
        output = []
        out_filename = "biden.json"
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
        return output

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

    User = request.form.get('wd3')
    API = Authorization_Setup()
    User_Tweets = Get_User_Timeline(API,User,10)
    output = Google_senti('user_tweets.json')
    return json.dumps(output,indent=4,ensure_ascii=False)

@app.route('/happynews', methods = ['GET', 'POST'])
def happynews():
    def news_cbs():
        url = 'http://www.cbsnews.com'
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text,'html.parser')  # 'html.parser':the HTML parser of the BeautifulSoup library, parse HTML
        # Use loop output to crawl to all news headlines on the page
        cbs = {}
        for a in soup.find_all('a', href=True): 
            if a.get_text(strip=True): 
                if a['href'][0] == 'h':
                    cbs[a.text] = a['href']
        return cbs

    #use google nlp to calculate each new's emotion
    def cal_emo(text):
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        emo = {}
        emo['score'] = sentiment.score
        emo['magnitude'] = sentiment.magnitude
        return emo
    keyword2 = request.form.get('wd2')
    number = request.form.get('wd3')
    cbs = news_cbs()
    search_result = {}
    i = 1
    if keyword2 == '':
        return {'Search result':'Please choose happy or sad.'}
    if keyword2 == 'sad':
        for keys in cbs:
            #此处输出每条新闻的text,情感,链接
            emo = cal_emo(keys)
            if float(emo['score']) < 0:
                search_result[keys] = cal_emo(keys)
                #search_result[i]['emo'] = cal_emo(keys)
                i = i + 1
                if i >= int(number):
                    break
    if keyword2 == 'happy':
        for keys in cbs:
            #此处输出每条新闻的text,情感,链接
            emo = cal_emo(keys)
            if float(emo['score']) > 0.2:
                search_result[keys] = cal_emo(keys)
                #search_result[i]['emo'] = cal_emo(keys)
                i = i + 1
                if i >= int(number):
                    break
    if not bool(search_result):
        return {'Search result':'No relevant news today'}
    result = {'Relevant news today': search_result}
    return json.dumps(result,indent=4,ensure_ascii=False)


#make it restful
class UserView(Resource):
    def get(self):
        get_url = 'http://127.0.0.1:5000'
        params = {
        "param_one": "XXX",
        "param_two": "XXX",
        }
        request = requests.get(get_url, params=params)
        return json.dumps(request.content,cls=MyEncoder,indent=4)


    def post(self):
        post_url = 'http://127.0.0.1:5000'
        params = {
            "param_one": "XXX",
            "param_two": "XXX",
        }
        request = requests.post(post_url, json=params)
        return request.content

    def delete(self):
        delete_url = 'http://127.0.0.1:5000'
        unique_identifier = 'Unique identifier'    
        result = requests.delete(delete_url + unique_identifier)
        return result.content

    def put(self):
        params = {
            "param_one": "XXX",
            "param_two": "XXX",
        }
        put_url = 'your url'
        request = requests.put(put_url, json=params)
        return request.content

api.add_resource(UserView,'/user')

if __name__ == '__main__':
    app.run(debug = True)