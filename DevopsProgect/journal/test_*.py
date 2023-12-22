# /path/to/your/project/tests/test_student.py

from app.app import db, app
from app.models import Student

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:testpassword@localhost/testdbname'

def test_create_student():
    # Kiểm tra và tạo cơ sở dữ liệu nếu cần
    with app.app_context():
        db.create_all()

        student = Student(lastname='Doe', name='John', surname='Smith', admission_year=2022,
                          education_form='Full-time', group='A1')

        db.session.add(student)
        db.session.commit()

        retrieved_student = Student.query.filter_by(lastname='Doe').first()

        assert retrieved_student is not None
        assert retrieved_student.lastname == 'Doe'
        assert retrieved_student.name == 'John'
        assert retrieved_student.surname == 'Smith'
        assert retrieved_student.admission_year == 2022
        assert retrieved_student.education_form == 'Full-time'
        assert retrieved_student.group == 'A1'
