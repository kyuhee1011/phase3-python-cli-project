from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Character, Player, Enemy, room
# import ipdb; ipdb.set_trace()

# from faker import Faker
# fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///mini_survival_game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Character).delete()
    session.query(Player).delete()
    session.query(Enemy).delete()
    


characters= [
    Character (name="James Park", class_job= "knight",health_point= "70", 
               combat_word= "Fight", attack_point = "25"),
    Character (name="Karen Smith", class_job= "priest", health_point= "40",
               combat_word= "Holy Fire", attack_point = "10"),
    Character (name="Harry Dime", class_job= "mage",
               health_point= "50", combat_word= "Ice Storm", attack_point = "20"),
    Character (name="Nick Super", class_job= "archer",
               health_point= "60", combat_word= "Quick Shot", attack_point = "15"),

]
session.add (characters)
session.commit ()

characters =session.query (Character).all()

players = [
    Player (name="Kyuhee Lee", number_of_win= "1", number_of_lose="0")
]

session.add (players)
session.commit ()

players =session.query (Player).all()

enemies = [
    Enemy (name="Xamir", type="Venom Man", health_point="60",attack_point = "10"),
    Enemy (name="Goldnails", type="Goblin", health_point="30",attack_point = "7"),
    Enemy (name="Elrel", type="Demon", health_point="40",attack_point = "15"),
    Enemy (name="Kumonga", type="Giant Spider", health_point="50",attack_point = "12"),
    Enemy (name="Toothless", type="Dragon", health_point="70",attack_point = "15")
]

session.add (enemies)
session.commit ()

enemies =session.query (Enemy).all()

room_character_enemy=[
    room (room_name ="Creepy Dark Desert", room_type="Forest "),
    room (room_name ="The Glory Plaza", room_type="Plaza"),
    room (room_name ="Daily Tasty Food", room_type="Kitchen"),
    room (room_name ="Main Public Library", room_type="Library"),
    room (room_name ="Midstable Hallway", room_type="Corridor")
]

session.add (room_character_enemy)
session.commit ()

enemies =session.query (room).all()



#create a random enemies name
# for _ in range (5):
#     name=fake.name()
#     enemy = Enemy (name=fake.name())
#     session.add(enemy)
#     session.commit()