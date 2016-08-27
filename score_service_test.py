import unittest

from score_service import ScoreService

class ScoreServiceTest( unittest.TestCase ):

  def test_score( self ):
    self.assertEqual( 0, int( round( ScoreService().score( 1000, 1000 ))))

if __name__ == '__main__':
    unittest.main()

