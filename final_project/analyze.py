from lib2to3.pgen2 import token
import re
import typing
import csv
from dataclasses import dataclass
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.api import TokenizerI
from nltk.probability import FreqDist
from nltk.util import bigrams

url_pattern = re.compile(r"https?://[^\s]+")

@dataclass
class TweetData:
    author: str
    content: str

class KnownData:
    __slots__ = ()
    
    def __init__(self) -> None:
        pass

def read_csv(iter: typing.Iterable[str]) -> typing.Iterator[TweetData]:
    reader = csv.reader(iter)
    next(reader)
    for row in reader:
        yield TweetData(*row[0:2])

def to_bigrams(tweet: TweetData, tokenizer: TokenizerI = None):
    if tokenizer is None:
        tokenizer = TweetTokenizer()
    token = tokenizer.tokenize(tweet.content)
    return bigrams(token)

def to_unigrams(tweet: TweetData, tokenizer: TokenizerI = None):
    if tokenizer is None:
        tokenizer = TweetTokenizer()
    return tokenizer.tokenize(tweet.content)

def create_bigram_freqdist(tweets: typing.Iterator[TweetData], tokenizer: TokenizerI = None):
    dic = FreqDist()
    for tweet in tweets:
        for gram in to_bigrams(tweet, tokenizer):
            dic[gram] = dic.get(gram, 0) + 1
        for gram in to_unigrams(tweet, tokenizer):
            dic[gram] = dic.get(gram, 0) + 1
    return dic


# Todo: 関数名を後で変える
def logic(author: str):
    pass

def main():
    nltk.download('punkt')
    tt = TweetTokenizer()
    with open("katyperry_known.csv", "rt") as f1, open("justinbieber_known.csv", "rt") as f2:
        tweets1 = list(read_csv(f1))
        tweets2 = list(read_csv(f2))
    dic1 = create_bigram_freqdist(tweets1, tt)
    dic2 = create_bigram_freqdist(tweets2, tt)
    with open("katyperry_question.csv", "rt") as f1:
        tweets = list(read_csv(f1))
    count1 = 0
    count2 = 0
    count3 = 0
    tmp = []
    for tweet in tweets:
        freq1 = 0
        freq2 = 0
        for bigram in to_bigrams(tweet, tt):
            freq1 += dic1.get(bigram, 0)
            freq2 += dic2.get(bigram, 0)
        # unigram
        if freq1 > freq2:
            count1 += 1
        elif freq1 < freq2:
            count2 += 1
        else:
            freq1 = 0
            freq2 = 0
            for key in to_unigrams(tweet, tt):
                freq1 += dic1.get(key, 0)
                freq2 += dic2.get(key, 0)
            if freq1 > freq2:
                count1 += 1
            elif freq1 < freq2:
                count2 += 1
            else:
                count3 += 1
    print(count1, count2, count3)
    print("\n".join(tmp))
    

    # bigram見ていって、頻度と比べてみてどっちが近いか的な

if __name__ == "__main__":
    main()

# nltk UnigramTagger