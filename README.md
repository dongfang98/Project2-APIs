# Project 2 - APIs
EC601 - Test for Twitter/Google APIs.  
# Phase1(A) - Twitter APIs
In this phase, I use TweetAPI to realize several Twitter API's function with my twitter ID, and save some of the results in json files.  
### Python Version
Before running the program, make sure you have the latest version of python. I found my Mac's default version is python2.7, so I run the command to open bash_profile：
```
vi ./bash_profile
```
And then add these 3 lines below to the bash_profile.  
```
PATH="/usr/bin:${PATH}"
export PATH
alias python="/Users/lidongfang/opt/anaconda3/bin/python3"
```
Save and quit by entering ```'::wq'```.  
Run the command to make the file work.  
```
source ./bash_profile
```
### Key
Log into your Twitter develop account and create an app.  
Then generate the key to access twitter API. Store the keys in file 'Keys.py', with the following format.  
```
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
Bearer_token ='Your bearer token'
```
### Tweepy
To import tweepy, run the command bellow to make sure it is installed into python3's package.
```
python3 -m pip install tweepy --user
```
## Functions
### 1.Timeline methods
I use 'home_timeline' to return the 20 most recent statuses, including retweets, posted by the authenticating user and that user’s friends. This is the equivalent of /timeline/home on the Web.  
``` python
API.home_timeline([since_id][, max_id][, count][, page])
```
Results are saved in my_tweets.json.  
https://github.com/dongfang98/Project2-APIs/blob/main/my_tweets.json

I use 'user_timeline' to return the 20 most recent statuses posted from the authenticating user or the user specified. It’s also possible to request another user’s timeline via the id parameter.  
``` python
API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
```
Results are saved in user_tweets.json.  
https://github.com/dongfang98/Project2-APIs/blob/main/user_tweets.json

### 2.Status methods
I use 'update_status' to update the authenticated user’s status. Statuses that are duplicates or too long will be silently ignored.
``` python
API.update_status(status[, in_reply_to_status_id][, lat][, long][, source][, place_id])
```
![image](https://user-images.githubusercontent.com/78338843/134862590-6cf5f11f-40c2-4ff4-b35a-1bd8fb9d4cd6.png)
![image](https://user-images.githubusercontent.com/78338843/134862680-8fcd0464-1108-4839-9057-4163be7bd241.png)

### 3.Friendship Methods
Create a new friendship with the specified user (aka follow).  
``` python
API.create_friendship(id/screen_name/user_id[, follow])
```
Destroy a friendship with the specified user (aka unfollow).  
``` python
API.destroy_friendship(id/screen_name/user_id)
```
I test this with my roomate's ID.  
![image](https://user-images.githubusercontent.com/78338843/134863447-7875179c-1b58-4644-a5ad-c44297cdfeae.png)
![image](https://user-images.githubusercontent.com/78338843/134863407-37e7a92f-c85e-4295-887f-36169e74dc3d.png)

### 4.List Methods
Creates a new list for the authenticated user. Accounts are limited to 20 lists.  
``` python
API.create_list(name[, mode][, description])
```
![image](https://user-images.githubusercontent.com/78338843/134863879-0826fc5a-42ca-4362-9ab3-ff4a3d07e24a.png)

### 5.Search Tweets
Returns a collection of relevant Tweets matching a specified query.  
``` python
API.search_tweets()
```
Results are stored in Search_tweets.json.  
https://github.com/dongfang98/Project2-APIs/blob/main/Search_tweets.json
 
# Phase1(B) - Google NLP
In this task, I use Google NLP API to score the sentiment of the tweets I searched with tweepy in phase 1.  
## Setting up authentication
To begin with, you need to login in Google Cloud Platform, and create a project: https://cloud.google.com/natural-language  
  
Next, create a service account key for the project with the following steps:  
In the Cloud Console, click the email address for the service account that you created.  
1.Click Keys.  
2.Click Add key, then click Create new key.  
3.Click Create. A JSON key file is downloaded to your computer.  
  
Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS. This variable only applies to your current shell session, so if you open a new session, set the variable again.
```
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Replace KEY_PATH with the path of the JSON file that contains your service account key.  
## GoogleAPI.py
In my code, I analyze the sentiment of Taylor Swift's last 10 tweets searched by tweepy.  
To run program, firstly you may need to impport the module 'google.cloud' with the command below:
```
python3 -m pip install google.cloud --user
```
Then run the analysis program with:
```
py GoogleNLP.py
```
A json file output(taylor.py) will be automatically generated to show each tweets' sentiment score and magnitude in the format below:
``` json
{
    "name": "Taylor Swift",
    "moment": "Fri Sep 17 13:18:53",
    "text": "Hi! Saw you guys got Wildest Dreams trending on tiktok, thought you should have my version \ud83d\ude18\ud83d\ude18\ud83d\ude18\ud83d\ude18\u2026 https://t.co/LtkfAItbUp",
    "sentiment.score": 0.5,
    "sentiment.magnitude": 1.5
}
```
# Phase2 - Emotion Analyzer
In phase2, I use Flask to make simple Emotion Analyze Website.  
In folder 'Phase2', python codes are in Emo_analyzer.py, website style are in templates/index.html.  
![image](https://user-images.githubusercontent.com/78338843/136720603-53944bc1-8331-475c-b8e0-14b94c718b8a.png)

## User Story  
A user want to see whether his/her idol is happy or sad recently.  
A user want to see all/set number of happy/sad news today from CBS.  
A user is not happy and want to see some interesting jokes.  

## Functions  
### 1.Analyze Twitter's Emotion 
Enter a User ID, and click the button 'Check His/Her Recent Emotion'. Then http://127.0.0.1:5000/useremo will show all the recent tweets and each tweet's emotion score and magnitude.  
I use tweepy's Timeline methods to put the user's tweet_text in json, and use Google NLP to analyze each tweets' emotion.  
The result will be shown in this format:  
``` json
{
    "name": "Taylor Swift",
    "moment": "Fri Sep 17 13:18:53",
    "text": "Hi! Saw you guys got Wildest Dreams trending on tiktok, thought you should have my version \ud83d\ude18\ud83d\ude18\ud83d\ude18\ud83d\ude18\u2026 https://t.co/LtkfAItbUp",
    "sentiment.score": 0.5,
    "sentiment.magnitude": 1.5
}
``` 
### 2.Get Happy/Sad News
I use BeautifulSoup to get news from www.cbs.com, and then use Google NLP to devide them with the emotion score.  
Firstly enter 'happy'/'sad' to choose the emotion of the news, then enter the number of news want to see.  
If 'happy' news are requested, http://127.0.0.1:5000/happynews will show news with sentiment.score > 0.5.  
If 'sad' news are requested, http://127.0.0.1:5000/happynews will show news with sentiment.score < 0.  
Usually most of the news are sad with low score.  
![image](https://user-images.githubusercontent.com/78338843/136734335-c5af63da-bf64-4675-be55-9bc36ba2e0b6.png)
If we search 10 sad news, we will get this:  
I‘m still working on the json line wrap, dump(indent) didn't work.  
![image](https://user-images.githubusercontent.com/78338843/136734458-caf9fb41-49d6-41c4-899b-c5a5d1af33da.png)
If the user didn't enter the emotion type, I will also give a return as below.  
![image](https://user-images.githubusercontent.com/78338843/136734515-30aadfca-08f0-4dc1-af7e-192faa8a59f5.png)
### 3.Get Jokes
When the user is sad, he can lick the button to get some interesting tweet stories with sentiment.score > 0.8.  
Json Format is the same as output of function1.  
# Unit Test
I add a python-package.yml to workflows, with all the env and commands in it. I use secrets to store the tweepy keys.
I write 3 unit test in TWeetAPI_test.py and run it in action successfully. Three function in TWeetAPI.py are tested, including 'test_homeline()', 'test_user_time_line()' and 'test_Search_Tweets()'.  
All the codes and related json files are in folder 'action test'.  
# References
Document of tweety3.5.0:  
https://docs.tweepy.org/en/v3.5.0/api.html#API.update_with_media  
Document of latest tweety:  
https://docs.tweepy.org/en/latest/api.html  
Google Cloud Natural Language:  
https://cloud.google.com/natural-language/docs/reference/libraries  
NiantongDong Unit test home tweets:  
https://github.com/NiantongDong/EC601/tree/master/Project%202 
