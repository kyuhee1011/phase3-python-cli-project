from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Character (Base): 
    __tablename__='characters'
    id = Column (Integer(), primary_key=True)
    name = Column(String())
    class_job= Column(String())
    health_point = Column(Integer())
    attack_point = Column(Integer())

    def __repr__(self):
        return f"Character {self.id}: " \
            + f"{self.name}, " \
            + f"class {self.class_job}"\
            + f"HP {self.health_point}"\
            + f"AP {self.attack_point}"

class Enemy (Base): 
    __tablename__='enemies'
    id = Column (Integer(), primary_key=True)
    name = Column(String())
    type= Column(String())
    health_point = Column(Integer())
    attack_point = Column(Integer())
    room_id = Column(String(), ForeignKey ("rooms.id"))

    def __repr__(self):
        return f"Enemy {self.id}: " \
            + f"{self.name}, " \
            + f"type {self.type}"\
            + f"HP {self.health_point}"\
            + f"AP {self.attack_point}"\
            + f"room number {self.room_id}"

class Room (Base): 
    __tablename__='rooms'
    id = Column (Integer(), primary_key=True)
    name = Column(String())
    room_type= Column(String())
  

    def __repr__(self):
        return f"Room {self.id}: " \
            + f"{self.name}, " \
            + f"type {self.room_typetype}"
            
   

