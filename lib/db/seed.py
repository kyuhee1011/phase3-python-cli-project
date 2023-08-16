from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Character
# import ipdb; ipdb.set_trace()

# from faker import Faker
# fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///mini_survival_game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Character).delete()

characters= [
    Character (name="James Park", class_job= "knight",health_point= "70", 
               combat_word= "Fight", attack_point = "25"),
    Character (name="Karen Smith", class_job= "priest", health_point= "40",
               combat_word= "Holy Fire", attack_point = "10"),
    Character (name="Harry Dime", class_job= "mage",
               health_point= "50", combat_word= "Ice Storm", attack_point = "20"),
    Character (name="Nick Super", class_job= "archer",
               health_point= "60", combat_word= "Quick Shot",attack_point = "15"),

]

session.bulk_save_objects (characters)
session.commit ()

characters =session.query (Character).all()


#create a random enemies name
# for _ in range (5):
#     name=fake.name()
#     enemy = Enemy (name=fake.name())
#     session.add(enemy)
#     session.commit()