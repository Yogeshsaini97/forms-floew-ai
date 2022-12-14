"""Defaultvalue process key

Revision ID: 07591848eb83
Revises: 6a1b3ffbf3ab
Create Date: 2022-04-13 14:43:39.288902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07591848eb83'
down_revision = '6a1b3ffbf3ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('form_process_mapper', 'process_key',
               existing_type=sa.String(length=50),
               server_default="Defaultflow",
               existing_nullable=True)
    op.alter_column('form_process_mapper', 'process_name',
               existing_type= sa.String(length=100),
               server_default="Default Flow",
               existing_nullable=True)
    op.execute("update form_process_mapper set process_key = 'Defaultflow', process_name='Default Flow' where form_process_mapper.process_key is null or form_process_mapper.process_key = ''")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('form_process_mapper', 'process_key',
               existing_type=sa.String(length=50),
               server_default=None,
               existing_nullable=True)
    op.alter_column('form_process_mapper', 'process_name',
               existing_type=sa.String(length=100),
               server_default=None,
               existing_nullable=True)
    # ### end Alembic commands ###
