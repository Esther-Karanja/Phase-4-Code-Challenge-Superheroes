from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules =('-hero_powers.heroe',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    hero_powers = db.relationship('Hero_Power', backref ='hero')

    def __repr__(self):
        return f'hero name is {self.name} and super_name is {self.super_name}.'


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules =('-hero_powers.power',)

    id = db.Column(db.Integer , primary_key =True)
    name = db.Column(db.String)
    description =db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('Hero_Power' , backref='power')
    
    @validates('description')
    def validate_description(self, key,length):
        if None==False and length > 19:
            raise ValueError("Must have a description at least 20 characters long")
        return length
    
    def __repr__(self):
        return f'power name is {self.name} and description is {self.description}.'

class Hero_Power(db.Model, SerializerMixin):

    __tablename__ ='hero_powers'

    serialize_rules =('-hero.hero_powers', '-power.hero_powers',)

    id = db.Column(db.Integer , primary_key =True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer , db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime , server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('strength')
    def validate_strength(self, key, attr=['Strong,Weak,Average']):
        if not attr:
            raise ValueError("strength must be Strong, Weak or Average")
        return attr
    
    def __repr__(self):
        return f'hero_powers strength is {self.strength}.'


# add any models you may need. 