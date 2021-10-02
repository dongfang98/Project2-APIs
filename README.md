# Project 2 - APIs
EC601 - Test for Twitter/Google APIs.  
# Phase1 - Twitter APIs
I use TweetAPI to test several Twitter API's function with my twitter ID, and save some of the results in json files.  
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
https://github.com/dongfang98/Project2-APIs/blob/main/my_tweets.json

I use 'user_timeline' to return the 20 most recent statuses posted from the authenticating user or the user specified. It’s also possible to request another user’s timeline via the id parameter.  
```
API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
```
Results are saved in user_tweets.json.  
https://github.com/dongfang98/Project2-APIs/blob/main/user_tweets.json

### Status methods
I use 'update_status' to update the authenticated user’s status. Statuses that are duplicates or too long will be silently ignored.
```
API.update_status(status[, in_reply_to_status_id][, lat][, long][, source][, place_id])
```
![image](https://user-images.githubusercontent.com/78338843/134862590-6cf5f11f-40c2-4ff4-b35a-1bd8fb9d4cd6.png)
![image](https://user-images.githubusercontent.com/78338843/134862680-8fcd0464-1108-4839-9057-4163be7bd241.png)

### Friendship Methods
Create a new friendship with the specified user (aka follow).  
```
API.create_friendship(id/screen_name/user_id[, follow])
```
Destroy a friendship with the specified user (aka unfollow).  
```
API.destroy_friendship(id/screen_name/user_id)
```
I test this with my roomate's ID.  
![image](https://user-images.githubusercontent.com/78338843/134863447-7875179c-1b58-4644-a5ad-c44297cdfeae.png)
![image](https://user-images.githubusercontent.com/78338843/134863407-37e7a92f-c85e-4295-887f-36169e74dc3d.png)

### List Methods
Creates a new list for the authenticated user. Accounts are limited to 20 lists.  
```
API.create_list(name[, mode][, description])
```
![image](https://user-images.githubusercontent.com/78338843/134863879-0826fc5a-42ca-4362-9ab3-ff4a3d07e24a.png)

### Search Tweets
Returns a collection of relevant Tweets matching a specified query.  
```
API.search_tweets()
```
Results are stored in Search_tweets.json.  
https://github.com/dongfang98/Project2-APIs/blob/main/Search_tweets.json

# References
Document of tweety3.5.0:  
https://docs.tweepy.org/en/v3.5.0/api.html#API.update_with_media  
Document of latest tweety:  
https://docs.tweepy.org/en/latest/api.html  
NiantongDong Unit test home tweets:  
https://github.com/NiantongDong/EC601/tree/master/Project%202  


'''
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
'''
