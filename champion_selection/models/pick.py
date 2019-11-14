from datetime import datetime
from sqlalchemy import Date, cast

from django.db import models
from src.db.models.team_composition import TeamComposition
from src.models.team import Team

class Pick(models.Model):
  __tablename__ = 'picks'

  id = db.Column(db.Integer, primary_key=True)

  screenshot_width = db.Column(db.Integer)
  screenshot_height = db.Column(db.Integer)

  blue_team_id = db.Column(db.Integer, db.ForeignKey('team_compositions.id'), index=True)
  red_team_id = db.Column(db.Integer, db.ForeignKey('team_compositions.id'), index=True)

  player = db.Column(db.String(10))

  ana = models.BooleanField(default=False)
  ashe = models.BooleanField(default=False)
  bastion = models.BooleanField(default=False)
  baptiste = modelsBooleanField(default=False)
  brigitte = models.BooleanField(default=False)
  doomfist = models.BooleanField(default=False)
  dva = models.BooleanField(default=False)
  genji = models.BooleanField(default=False)
  hammond = models.BooleanField(default=False)
  hanzo = models.BooleanField(default=False)
  junkrat = models.BooleanField(default=False)
  lucio = models.BooleanField(default=False)
  mcree = models.BooleanField(default=False)
  mei = models.BooleanField(default=False)
  mercy = models.BooleanField(default=False)
  moira = models.BooleanField(default=False)
  orisa = models.BooleanField(default=False)
  pharah = models.BooleanField(default=False)
  reaper = models.BooleanField(default=False)
  reinhardt = models.BooleanField(default=False)
  roadhog = models.BooleanField(default=False)
  sigma = models.BooleanField(default=False)
  soldier76 = models.BooleanField(default=False)
  sombra = models.BooleanField(default=False)
  symmetra = models.BooleanField(default=False)
  torbjorn = models.BooleanField(default=False)
  tracer = models.BooleanField(default=False)
  widowmaker = models.BooleanField(default=False)
  winston = models.BooleanField(default=False)
  zarya = models.BooleanField(default=False)
  zenyatta = models.BooleanField(default=False)

  screenshot = models.FilePathField()

  uploaded_at = models.DateTimeField(auto_now_add=True)
  blumodels.ForeignKey(ChampionComposition, on_delete=models.CASCADE,
                               blank=True, null=True)

  blue_team = db.relationship('ChampionComposition', foreign_keys=blue_team_id)
  red_team = db.relationship('ChampionComposition', foreign_keys=red_team_id)

  class Meta:
    # name of db table for this Model
    db_table = 'champion_picks'

  def __init__(self, **kwargs):
    self.uploaded_at = datetime.utcnow()
    self.__dict__.update(kwargs)

  def blue_heroes(self):
    if self.blue_team:
      return self.blue_team.heroes()
    return []

  def red_heroes(self):
    if self.red_team:
      return self.red_team.heroes()
    return []

  # Returns the count of how many heroes were suggested to the user.
  def num_suggestions(self):
    valid_names = Team.hero_names.keys()
    suggestions = [name for name in valid_names if name in self.__dict__ and self.__dict__[name]]
    return len(suggestions)

  # Returns a list of the names of the heroes suggested for the user to pick.
  def heroes(self):
    valid_names = Team.hero_names.keys()
    suggestions = [name for name in valid_names if name in self.__dict__ and self.__dict__[name]]
    suggestions.sort()
    return suggestions

  def heroes_str(self):
    return ','.join(self.heroes())

  def blue_heroes_str(self):
    return ','.join(self.blue_heroes())

  def red_heroes_str(self):
    return ','.join(self.red_heroes())

  # Returns a list of the other players on the blue team, excluding the player
  # if the player is known.
  def allies(self):
    if self.player is None:
      return self.blue_heroes()
    result = []
    hero_counts = self.blue_team.counts()
    for hero, count in hero_counts.iteritems():
      if (hero != self.player and count > 0) or (hero == self.player and count > 1):
        result.append(hero)
    return result

  # Returns a string to be used to uniquely represent this Pick in a URL.
  def slug(self):
    date = self.uploaded_at.strftime('%Y%m%d')
    if self.player:
      return self.player + '.' + str(self.id) + '.' + date
    else:
      return 'unknown.' + str(self.id) + '.' + date

  # Given a slug like ana.1.20170115, this will return the Pick record that matches,
  # or None if it does not exist.
  @classmethod
  def find_by_slug(cls, slug):
    parts = slug.split('.')
    if len(parts) != 3:
      return None
    player = parts[0]
    id = int(parts[1])
    date_str = parts[2]
    row = Pick.query.filter_by(id=id).limit(1).first()
    if row and (row.player == player or row.player is None and player == 'unknown'):
      expected_date_str = row.uploaded_at.strftime('%Y%m%d')
      if date_str == expected_date_str:
        return row
    return None

  @classmethod
  def find_today_with_attrs(cls, attrs):
    valid_names = Team.hero_names.keys()
    for hero in valid_names:
      if hero not in attrs:
        attrs[hero] = False
    today = datetime.utcnow().date()
    row = Pick.query.filter_by(**attrs).\
      filter(cast(Pick.uploaded_at, Date) == today).limit(1).first()
    if row:
      return row
    return None

  # Returns True if the hero the user was playing is a suggested pick for the
  # known team composition.
  def player_ok(self):
    if self.player is None:
      return True
    return self.player in self.heroes()
