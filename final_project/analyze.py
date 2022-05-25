import re
import typing
import csv
from dataclasses import dataclass
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist
from nltk.util import bigrams

url_pattern = re.compile(r"https?://[^\s]+")

@dataclass
class TweetData:
    author: str
    content: str

def read_csv(iter: typing.Iterable[str]) -> typing.Iterator[TweetData]:
    reader = csv.reader(iter)
    next(reader)
    for row in reader:
        yield TweetData(*row[0:2])


def main():
    nltk.download('punkt')
    with open("katyperry_known.csv", "rt") as f:
        tweets = list(read_csv(f))
    tt = TweetTokenizer()
    dic = FreqDist()
    for tweet in tweets:
        token = tt.tokenize(tweet.content)
        for gram in bigrams(token):
            dic[gram] = dic.get(gram, 0) + 1
    print(dic.most_common(50))
    # bigram見ていって、頻度と比べてみてどっちが近いか的な

if __name__ == "__main__":
    main()

# nltk UnigramTagger