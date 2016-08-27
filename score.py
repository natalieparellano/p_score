from math import log

class ScoreService:

  def score( self, total ):
    return log( total, 10 )