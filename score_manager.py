from twitter_service import TwitterService
from score_service import ScoreService 

class ScoreManager:

  def __init__( self ):
    self.max_tweets = 1000

  def score( self, data ):
    url = data['url']

    if not url:
      return 1 # consider businesses without a website to be high risk
    else:
      k_recent_tweets = TwitterService().do_search( url, self.max_tweets )
      print "k_recent_tweets is %s" % k_recent_tweets
      score = ScoreService().score( k_recent_tweets, self.max_tweets )
      return score