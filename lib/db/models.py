from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

player_character=Table (
    "player_character",
    Base.metadata,
    Column ("player_character_id", Integer, primary_key=True),
    Column ("character_id", ForeignKey("character.id")),
    Column ("player_id", ForeignKey("player.id"))
)

room =Table(
    "room_character_enemy",
    Base.metadata,
    Column ("room_id", Integer, primary_key=True),
    Column ("room name",String()),
    Column ("room type",String()),
    Column ("character_id", ForeignKey("character.id")),
    Column ("enemy_id", ForeignKey("enemy.id"))
)

class Player(Base):
    __tablename__='players'
 
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    number_of_win= Column (Integer())
    number_of_lose=Column (Integer())
    
    characters=relationship("Character", secondary=player_character, backref="the_players")

    def __repr__(self):
        return f"Players {self.id}: " \
            + f"{self.name}, " \
            + f"Winning Score {self.number_of_win}"\
            + f"Losing Score {self.number_of_lose}"
    
   

class Character (Base): 
    __tablename__='characters'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    class_job= Column(String())
    health_point = Column(Integer())
    combat_word = Column (String())
    attack_point = Column(Integer())

    players=relationship("Player", secondary=player_character, backref="the_characters")
    enemies=relationship("Enemy", secondary=room, backref="the_enemies")

    def __repr__(self):
        return f"Character {self.id}: " \
            + f"{self.name}, " \
            + f"class {self.class_job}"\
            + f"HP {self.health_point}"\
             + f"Combat Word {self.combat_word}"\
            + f"AP {self.attack_point}"
    
class Enemy (Base): 
    __tablename__='enemies'
    id = Column (Integer(), primary_key=True)
    name = Column(String())
    type= Column(String())
    health_point = Column(Integer())
    attack_point = Column(Integer())
    characters=relationship("Character", secondary=room, backref="the_characters")

    def __repr__(self):
        return f"Enemy {self.id}: " \
            + f"{self.name}, " \
            + f"type {self.type}"\
            + f"HP {self.health_point}"\
            + f"AP {self.attack_point}"\
            

        
# class Room (Base): 
#     __tablename__='rooms'
#     id = Column (Integer(), primary_key=True)
#     name = Column(String())
#     room_type= Column(String())
#     char_id =Column(Integer(), ForeignKey("enemies.id"))
#     enemy_id=Column(Integer(), ForeignKey ("characters.id"))
  

#     def __repr__(self):
#         return f"Room {self.id}: " \
#             + f"{self.name}, " \
#             + f"type {self.room_type}"\
#             + f"Character Id {self.char_id}"\
#             + f"Enemy Id {self.enemy_id}"

