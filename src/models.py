import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

# OPCION 2: Ejercicio con tabla de asociaciones

# crear tabla de asociciones para todas las relaciones

association_table = Table('association', Base.metadata,
    Column('User', String, ForeignKey('user.id'), primary_key=True),
    Column('Movies', String, ForeignKey('movies.id'), primary_key=True),
    Column('Planets', String, ForeignKey('planets.id'), primary_key=True),
    Column('People', String, ForeignKey('people.id'), primary_key=True),
)

# Crear tabla: user, planets, movies y people.

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String())
    firtname = Column(String())
    email = Column(String(), nullable=False)
    password = Column(String(10), nullable=False)
    subscription_date = Column(Date)
    # Añadimos los "hijos" asociando a la tabla los id
    # El atributo secondary se utiliza para especificar la tabla de asociación que conecta las dos tablas principales en una relación muchos a muchos
    # Back ref relaciona planets con User.
    children = relationship('Planets', secondary=association_table, backref='User')
    children = relationship('Movies', secondary=association_table, backref='User')
    children = relationship('People', secondary=association_table, backref='User')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)        
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface_water = Column(Integer, nullable=False)
    url = Column(String, nullable=False) 
    movies = Column(String, nullable=False)
    # Padre = User
    parent_id = Column(Integer, ForeignKey('User.id'))            
 
class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    year  = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey('User.id'))  

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('User.id'))  

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    # Hay que definir la columna = clave foránea
    user_id = Column(Integer, ForeignKey(User.id))
    # Definir la relación de esa FK
    user = relationship(User) # Aquí se debe definir que FK utiliza esta relación
    planet_id = Column(Integer, ForeignKey(Planets.id))
    planet = relationship (Planets)

        ## Draw from SQLAlchemy base




render_er(Base, 'diagram.png')
