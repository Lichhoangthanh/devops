
import os
import pytest
# tests/test_student.py
from flask import Flask
from app import db
from models import Student

os.environ['FLASK_ENV'] = 'testing'
os.environ['FLASK_APP'] = 'your_app'
os.environ['PGUSER'] = 'postgres'
os.environ['PGPASSWORD'] = 'linky1337'
os.environ['DATABASE'] = 'devops'
os.environ['PGHOST'] = 'localhost'
os.environ['PGPORT'] = '5432'

# Sử dụng fixture để tạo ứng dụng và cơ sở dữ liệu
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['PGUSER']}:{os.environ['PGPASSWORD']}@{os.environ['PGHOST']}:{os.environ['PGPORT']}/{os.environ['DATABASE']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app

# Fixture để có một đối tượng Student để kiểm tra
@pytest.fixture
def sample_student():
    return Student(
        lastname='Doe',
        name='John',
        surname='Smith',
        admission_year=2022,
        education_form='Full-time',
        group='A1'
    )

# Test tạo một đối tượng Student và lưu vào cơ sở dữ liệu
def test_create_student(app, sample_student):
    with app.app_context():
        db.session.add(sample_student)
        db.session.commit()

        retrieved_student = Student.query.filter_by(lastname='Doe').first()

        assert retrieved_student is not None
        assert retrieved_student.lastname == 'Doe'
        assert retrieved_student.name == 'John'
        assert retrieved_student.surname == 'Smith'
        assert retrieved_student.admission_year == 2022
        assert retrieved_student.education_form == 'Full-time'
        assert retrieved_student.group == 'A1'

# Import lớp mới từ module models
from models import PlanOfStudy, Gradebook

# Thêm fixture cho một đối tượng PlanOfStudy thử nghiệm
@pytest.fixture
def sample_plan_of_study():
    return PlanOfStudy(
        speciality='Computer Science',
        discipline='Data Structures',
        semester=2,
        hours=60,
        exam_or_test='Exam'
    )


# Kiểm tra tạo đối tượng PlanOfStudy và lưu vào cơ sở dữ liệu
def test_create_plan_of_study(app, sample_plan_of_study):
    with app.app_context():
        db.session.add(sample_plan_of_study)
        db.session.commit()

        retrieved_plan_of_study = PlanOfStudy.query.filter_by(discipline='Data Structures').first()

        assert retrieved_plan_of_study is not None
        assert retrieved_plan_of_study.speciality == 'Computer Science'
        assert retrieved_plan_of_study.semester == 2
        assert retrieved_plan_of_study.hours == 60
        assert retrieved_plan_of_study.exam_or_test == 'Exam'

# # Thêm fixture cho một đối tượng Gradebook thử nghiệm
# @pytest.fixture
# def sample_gradebook(sample_student, sample_plan_of_study):
#     return Gradebook(
#         year=2022,
#         student_id=sample_student.id,
#         discipline_id=sample_plan_of_study.id,
#         mark=85
#     )
# # Kiểm tra tạo đối tượng Gradebook và lưu vào cơ sở dữ liệu
# def test_create_gradebook(app, sample_gradebook):
#     with app.app_context():
#         db.session.add(sample_gradebook)
#         db.session.commit()

#         retrieved_gradebook = Gradebook.query.filter_by(mark=85).first()

#         assert retrieved_gradebook is not None
#         assert retrieved_gradebook.year == 2022
#         assert retrieved_gradebook.mark == 85
