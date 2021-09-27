# Project 2 - APIs
EC601-test for twitter apis  
# Phase1 - Twitter APIs
I use TweetAPI to test several functions to my twitter ID, and save some of the results in json files.  
## Python version
Before testing, make sure you have the latest version of python. I found my Mac's default version is python2.7, so I run the command to open bash_profile：
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
## Key
Log into your Twitter develop account and create an app.  
Then generate the key to access twitter API. Store the keys in file 'Keys.py', with the following format.  
```
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
Bearer_token ='Your bearer token'
```
## Tweepy
To import tweepy, run the command bellow to make sure it is installed into python3's package.
```
python3 -m pip install tweepy --user
```
## Functions
### Timeline methods
I use 'home_timeline' to return the 20 most recent statuses, including retweets, posted by the authenticating user and that user’s friends. This is the equivalent of /timeline/home on the Web.  
```
API.home_timeline([since_id][, max_id][, count][, page])
```
Results are saved in my_tweets.json.  
