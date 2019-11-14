from team import Team

class RedTeam(Team):
  """
  assume red team is always enemy team
  """
  def player(self):
    return None
