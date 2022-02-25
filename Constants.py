# import tweepy

consumer_key = 'zMsQqOKxWTyRlO0k0NLa7nsNt'
consumer_secret = 'sdcjRbxwri3jKxkrb46SinJ4U3zzmrk9PRJupfCTUHsE8PefT2'
# access_token = "AAAAAAAAAAAAAAAAAAAAAGpxZgEAAAAA8%2FUqiFCEi1bdNe%2BSj6UnbjLYmMs%3D7GN9mNss1xhWsqZejkWfyJepddCDwMP1OZ1w4LkUCcRLrOPPzV"
# access_secret = 'YOUR ACCESS SECRET'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)
# //////////////////////////////////////////////////////////////

# from tweepy.auth import OAuthHandler

# oauth1_user_handler = tweepy.OAuth1UserHandler(
#     "zMsQqOKxWTyRlO0k0NLa7nsNt", "sdcjRbxwri3jKxkrb46SinJ4U3zzmrk9PRJupfCTUHsE8PefT2",
#     callback="https://stetsondone.com"
# )

# print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

# ///////////////////////////////////////////////////////////////

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)