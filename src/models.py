import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

#Usando modelo con tabla de relaciones:
association_table = Table('association', Base.metadata,
    Column('Users', String, ForeignKey('users.id'), primary_key=True),
    Column('Movies', String, ForeignKey('movies.id'), primary_key=True),
    Column('Planets', String, ForeignKey('planets.id'), primary_key=True),
    Column('Character', String, ForeignKey('characters.id'), primary_key=True),
)

# Crear tabla: users, planets, movies y character.
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String())
    firtname = Column(String())
    email = Column(String(), nullable=False)
    password = Column(String(10), nullable=False)
    subscription_date = Column(Date)
    children = relationship('Planets', secondary=association_table, backref='Users')
    children = relationship('Movies', secondary=association_table, backref='Users')
    children = relationship('Characters', secondary=association_table, backref='Users')

class Profiles(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(20))
    firtname = Column(String(20))
    nickname = Column(String(6))
    imgurl = Column(String())
    users_id = Column(Integer, ForeignKey('users.id'), unique=True) #Define un user a un perfil únicamente
    users = relationship(Users)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)        
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    url = Column(String, nullable=False) 
    movies = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('Users.id'))            
 
class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    year  = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey('Users.id'))  

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    parent_id = Column(Integer, ForeignKey('Users.id'))  

#Creamos las tablas de favoritos. Opción1:
class FavoriteCharacters(Base):
    __tablename__ = "favorite_characters"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    users = relationship(Users) 
    characters = relationship (Characters)

class FavoritePlanets(Base):
    __tablename__ = "favorite_planets"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(Users) 
    planets = relationship (Planets)




render_er(Base, 'diagram.png')