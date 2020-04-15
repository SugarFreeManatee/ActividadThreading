import os

kim_tweets = []
path_kim = os.getcwd() + '/kim_tweets.csv'

with open(path_kim, 'r') as kim_tweets_file:
	lines = kim_tweets_file.readlines()
	for line in lines:
		if not lines.index(line) == 0:
			line = line.rstrip()
			line = line.split(';')
			kim_tweets.append(line)
trump_tweets = []
path_trump = os.getcwd() + '/trump_tweets.csv'
with open(path_trump, 'r') as trump_tweets_file:
	lines = trump_tweets_file.readlines()
	for line in lines:
		if not lines.index(line) == 0:
			line = line.rstrip()
			line = line.split(';')
			trump_tweets.append(line)
tweet_dict = {
	'Dr. Pin Tong-Un' : kim_tweets ,
	'Trumpzini' : trump_tweets
}