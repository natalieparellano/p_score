import unittest

from twitter import TwitterService

class TwitterServiceTest( unittest.TestCase ):

  def test_search( self ):
    self.assertEqual( 
      "<class 'TwitterAPI.TwitterAPI.TwitterResponse'>",
      str( TwitterService().search( "cnn" ).__class__ )
    )

  def test_search_high_count( self ):
    ts    = TwitterService()
    batch = ts.search( "cnn" )
    count = ts.tally_search( batch )[0]

    self.assertEqual( 100, count )

  def test_do_search_high_count( self ):
    ts    = TwitterService()
    count = ts.do_search( "cnn", 200 )

    self.assertEqual( 200, count )    

if __name__ == '__main__':
    unittest.main()
