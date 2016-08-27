import io
import json

from TwitterAPI import TwitterAPI

class TwitterService:
  def __init__( self ):
    self.connection = self.__connect()

  def do_search( self, string, limit=1000 ):
    """
    Fetches tweets in batches of 100, up to limit,
    and returns the total number of tweets.
    """
    total  = 0
    max_id = ''

    while total < limit:
      batch = self.search( string, max_id )
      count, max_id = self.tally_search( batch )
      # print "max_id is %s" % max_id 

      total += count

      if count < 100:
        break

    return total    

  def search( self, string, max_id='' ):
    """
    Returns up to 100 tweets containing the search string, 
    from the last 7 days.
    """
    query = { 'q': string, 'count': 100 }
    if max_id:
      query['max_id'] = max_id - 1

    return self.connection.request( 
      'search/tweets', 
      query
    )

  def tally_search( self, response_obj ):
    """
    Counts the total number of tweets returned by 
    a single API call.
    """
    count  = 0
    max_id = ''

    for tweet in response_obj:
      # print "id is %s" % tweet['id']
      count += 1
      max_id = tweet['id']

    return [count, max_id]

  def __connect( self ):
    print "Connecting..."

    with io.open( 'config/twitter_secret.json' ) as cred:
      creds = json.load( cred )

    return TwitterAPI(
      creds['twitter_consumer_key'], 
      creds['twitter_consumer_secret'], 
      creds['twitter_token'], 
      creds['twitter_token_secret']
    )    
