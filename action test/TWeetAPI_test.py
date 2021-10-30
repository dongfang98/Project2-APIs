import unittest
import TWeetAPI as TA
# import Keys
import json
import sys

api = TA.Authorization_Setup()
class TestSum(unittest.TestCase):
    def test_homeline(self):
        with open('my_tweets.json','r') as f:
            data_home = json.load(f)
        self.assertEqual(TA.GET_My_Home_tweets(api),data_home,"Error")

    def test_user_time_line(self):
        with open('user_tweets.json','r') as f:
            data_user = json.load(f)
        #Correct user ID
        self.assertEqual(TA.Get_User_Timeline(api,'@taylorswift13',10),data_user,"Error")
        #Incorrect user ID -> Shold throw exception -> return False
        self.assertEqual(TA.Get_User_Timeline(api,'@taylorswift13',10),False,"Error")
    
    def test_Search_Tweets(self):
        with open('test_Search_1.json','r') as f:
            data_search_1 = json.load(f)
        #Expected behaviour -> Right argument -> return text
        self.assertEqual(TA.GET_Search_Tweets(api, "Joe Biden", "recent", 1, "2021-10-29"),data_search_1,"Error")


if __name__ == '__main__':
    print("Start testing")
    print('TweetAPI testing')
    unittest.main()
