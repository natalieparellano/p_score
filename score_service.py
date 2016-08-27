from math import log

class ScoreService:

  def score( self, val, max_val ):
    max_score   = log( max_val, 10 )
    found_score = log( val, 10 )
    return 1 - ( found_score / max_score )