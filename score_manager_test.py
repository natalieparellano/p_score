import unittest

from score_manager import ScoreManager

class ScoreManagerTest( unittest.TestCase ):

  def test_do_score( self ):
    data = {
      "bus_name": "CNN", 
      "owner_name": "John Smith",
      "url": "cnn" # cnn.com
    }
    self.assertEqual( 0, int( round( ScoreManager().score( data ))))

if __name__ == '__main__':
    unittest.main()
