import unittest

from score import ScoreService

class ScoreServiceTest( unittest.TestCase ):

  def test_score( self ):
    self.assertEqual( 3, int( round( ScoreService().score( 1000 ))))    

if __name__ == '__main__':
    unittest.main()

