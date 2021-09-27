# Project 2 - APIs
EC601-test for twitter apis  
# Phase1 - Twitter APIs
I use TweetAPI to test several functions to my twitter ID.  
## Python version
Before testing, make sure you have the latest version of python. I found my Mac's default version of python is 2.7, so I run the command to open bash_profile：
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

