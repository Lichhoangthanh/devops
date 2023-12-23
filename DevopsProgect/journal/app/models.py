import os
import sqlalchemy as sa
from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    admission_year = db.Column(db.Integer, nullable=False)
    education_form = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.lastname
    
    # __table_args__ = {'extend_existing': True}
    
class PlanOfStudy(db.Model):
    __tablename__ = 'planofstudy'

    id = db.Column(db.Integer, primary_key=True)
    speciality = db.Column(db.String(100), nullable=False)
    discipline = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    exam_or_test = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.discipline

class Gradebook(db.Model):
    __tablename__ = 'gradebook'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    discipline_id = db.Column(db.Integer, db.ForeignKey("planofstudy.id"), nullable=False)
    mark = db.Column(db.Integer, nullable=False)

    student = db.relationship('Student')
    planofstudy = db.relationship('PlanOfStudy')

