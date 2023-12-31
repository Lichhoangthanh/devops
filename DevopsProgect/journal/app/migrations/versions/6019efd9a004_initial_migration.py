"""Initial migration.

Revision ID: 6019efd9a004
Revises: 
Create Date: 2023-11-29 17:44:45.273335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6019efd9a004'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planofstudy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('speciality', sa.String(length=100), nullable=False),
    sa.Column('discipline', sa.String(length=100), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('hours', sa.Integer(), nullable=False),
    sa.Column('exam_or_test', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_planofstudy'))
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('admission_year', sa.Integer(), nullable=False),
    sa.Column('education_form', sa.String(length=100), nullable=False),
    sa.Column('group', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_students'))
    )
    op.create_table('gradebook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['planofstudy.id'], name=op.f('fk_gradebook_discipline_id_planofstudy')),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name=op.f('fk_gradebook_student_id_students')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_gradebook'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gradebook')
    op.drop_table('students')
    op.drop_table('planofstudy')
    # ### end Alembic commands ###
