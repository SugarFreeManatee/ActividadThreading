from collections import namedtuple

# Carga los tweets del archivo entregado en path
# Retorna una lista de namedtuples
def cargar_tweets(path):
    Tweet = namedtuple("Tweet", ['enojo', 'texto'])
    tweets = []

    with open(path, 'r', encoding='utf-8') as archivo:
        for line in archivo.readlines()[1:]:
            line = line.rstrip().split(';')
            tweet = Tweet(int(line[0]), line[1])
            tweets.append(tweet)
    return tweets
