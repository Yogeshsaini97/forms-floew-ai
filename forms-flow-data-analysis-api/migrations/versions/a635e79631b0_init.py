"""init

Revision ID: a635e79631b0
Revises:
Create Date: 2021-08-31 08:15:43.169875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a635e79631b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sentiment_analysis_results',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('input_request', sa.String(length=100), nullable=True),
    sa.Column('output_response', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sentiment_analysis_results')
    # ### end Alembic commands ###
