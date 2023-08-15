from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    #creating table name of SQL database table
    __tablename__ = 'students'
    #Adding columns and assign primary key
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    major = Column (String())

#repr is like print in python
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"major {self.major}"
    
if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

#manages ORM -mapped objects
    Session = sessionmaker(bind=engine)
    session = Session()

#inserting datas
    kyuhee_lee= Student(
        id ="52146",
        name="Kyuhee Lee",
        major="MTH"
    )
  
    lilly_smith= Student(
        id="75486",
        name="Lilly Smith",
        major="ART"
    )

    session.bulk_save_objects([kyuhee_lee, lilly_smith])
    session.commit()

    students = session.query(Student)
    print ([student for student in students]) 


class Grade (Base):
    __tablename__ = 'grades'

    student_id = Column(Integer(), primary_key=True)
    course_id = Column (String, ForeignKey("course_id"))
    grade = Column (String())

#repr is like print in python
    def __repr__(self):
        return f"Grade {self.student_id}: " \
            + f"{self.course_id}, " \
            + f"grades {self.grade}"
    
if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    kyuhee_lee= Grade(
        student_id="52146",
        course_id="60205", 
        grade= "A"
    )
    kyuhee_lee= Grade(
        student_id="52146",
        course_id="740102", 
        grade= "B"
    )
  
    lilly_smith= Grade(
        student_id="75486",
        course_id="20105", 
        grade= "A"
    )
    lilly_smith= Grade(
        student_id="75486",
        course_id="32101", 
        grade= "B"
    )
    lilly_smith= Grade(
        student_id="75486",
        course_id="740102", 
        grade= "C"
    )

    session.bulk_save_objects([kyuhee_lee, lilly_smith])
    session.commit()

    grades = session.query(Grade).all()
    print ([grade for grade in grades]) 

class Course (Base):
    __tablename__ = 'courses'
    
    course_id = Column (Integer, primary_key=True)
    title =Column (String())
    instructor = Column (String())
    location=Column (String())

    def __repr__(self):
        return f"Course {self.course_id}: " \
            + f"{self.title}, " \
            + f"Instructor{self.instructor}, " \
            + f"Location {self.location}"
    
if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    kyuhee_lee= Course(
        course_id="60205",
        title= "Algebra",
        instructor = "West",
        location = "B222"
    )
    kyuhee_lee= Course(
        course_id="74102",
        title= "Science",
        instructor = "Kim",
        location = "B213"
    )
    lilly_smith= Course(
        course_id="20105",
        title= "Art",
        instructor = "Kim",
        location = "B213"
    )
    lilly_smith= Course(
        course_id="320101",
        title= "Basic English",
        instructor = "Porter",
        location = "D319"
    )
    lilly_smith= Course(
        course_id="74102",
        title= "Science",
        instructor = "Kim",
        location = "B213"
    )

    session.bulk_save_objects([kyuhee_lee, lilly_smith])
    session.commit()

    courses = session.query(Course).all()
    print ([course for course in courses]) 


  
#alembic revision --autogenerate -m 'create users (table name)'
users = [
    User(username="kyuhee"),
    User(username="lee"),
    User(username="kim"),
]