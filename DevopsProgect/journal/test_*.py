# /path/to/your/project/tests/test_student.py

from app.app import db, Student, app

def test_create_student():
    # Tạo ngữ cảnh ứng dụng
    with app.app_context():
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
