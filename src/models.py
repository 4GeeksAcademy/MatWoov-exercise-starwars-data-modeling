import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    suscription_date = Column(Integer)


class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(planet)

    def to_dict(self):
        return {}


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    gravity = Column(String(250))
    terraine = Column(String(250))
    climate = Column(String(250))


class FavoriteCharacter(Base):
    __tablename__= 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship(Character)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    height = Column(String(250))
    weight = Column(String(250))
    birth_day = Column(String(250))
    gender = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))


class FavoriteStarship(Base):
    __tablename__ = 'favorite_starship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    user = relationship(User)
    starship = relationship(Starship)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    passengers = Column(String(250))
    manufacturer = Column(String(250))
    starship_class = Column(String(250))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
