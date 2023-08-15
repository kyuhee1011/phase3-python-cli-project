from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Character, Enemy
import ipdb; ipdb.set_trace()

from faker import Faker
fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///mini_survival_game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Character).delete()


#create a random enemies name
for _ in range (5):
    name=fake.name()
    enemy = Enemy (name=fake.name())
    session.add(enemy)
    session.commit()