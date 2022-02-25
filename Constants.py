import tweepy

consumer_key = 'XgM18uUM7uZUBhvGTp694AZfG'
consumer_secret = 'vJw8Of4eZYgCXN72YSrMrf55flp55lgJ7VWNHcCOwdFn1emSrX'
access_token = '1497006055695343616-UCjxlJKcSUsZBD5O0meC7mQX9oJSZV'
access_secret = 'QeAdmvVX7aBTXDBEVh9qcefHwovz2qlMBFRBIo8OlODS1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# //////////////////////////////////////////////////////////////
