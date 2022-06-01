---README--------------------------------------------------------------------
Team member: s1270013 Kota Tashiro, s1260229 Reo Yamaguchi
-----------------------------------------------------------------------------
#create_dataset.py(Final project: Data functions)
  Tweets dataset URL: https://dataverse.harvard.edu/dataset.xhtml?id=3047332
  Import tweets datasets by Justin Bieber and Katy Perry.
  Divide each datasets randomly into 90% known and 10% questioned.
  
#analyze.py(Final project: Feature extraction and analyze)
  Preprocess
    Using TweetTokenizer(), remove URL pattern from tweets.
    Combine "@~" and "#~" into a single token.

  Analyze
    Create two lists of bigrams from Katie and Justin's tweet dataset.
    Sort by frequency of use.

    Create a list of bigrams from Katie or Justin's questioned tweet dataset.
      To switch questioned dataset, rewrite the filename on Line64.
    
    For each bigrams in the questioned tweet, verify whether Katie or Justin has more frequency in the known dataset and count it.
    For each tweet in questioned dataset, predict the name with the larger count as the author of that tweet.
    If the counts of bigrams in a tweet are equal, assume the author is unknown.

    For tweets with unknown authors, tokenize with unigrams and perform the same process.

    Output counts "Katie", "Justin", "Unknown".
--------------------------------------------------------------------------------



