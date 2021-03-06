from octogone import db
from octogone.models.base_model import BaseModel

octogones_game_rule_profile_association = db.Table(
    'octogones_game_rule_profile_association',
    db.Column('octogone_id',
              db.Integer,
              db.ForeignKey("octogone.id"),
              primary_key=True
              ),
    db.Column('game_rule_profile_id',
              db.Integer,
              db.ForeignKey("game_rule_profile.id"),
              primary_key=True
              )
)


class GameRuleProfile(BaseModel):
    """
    GameRuleProfile Model
    """

    # Attributes

    mmr = db.Column(db.Float(), default=0.0, nullable=False)
    octogone_accepted = db.Column(db.Integer(), default=0, nullable=False)
    octogone_refused = db.Column(db.Integer(), default=0, nullable=False)

    # Relationships

    game_rule_id = db.Column(db.Integer, db.ForeignKey("game_rule.id"), nullable=False)
    game_profile_id = db.Column(db.Integer, db.ForeignKey("game_profile.id"), nullable=False)
    octogones = db.relationship("Octogone",
                                secondary=octogones_game_rule_profile_association,
                                lazy='subquery',
                                backref=db.backref('game_rule_profiles', lazy=True)
                                )
