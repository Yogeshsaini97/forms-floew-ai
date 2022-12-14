"""add_tenant_fk_form_process_mapper

Revision ID: 6dd998fc6fed
Revises: 07591848eb83
Create Date: 2022-05-11 12:46:32.944166

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6dd998fc6fed'
down_revision = '07591848eb83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_form_version_uc', 'form_process_mapper', type_='unique')
    op.create_unique_constraint('_form_version_uc', 'form_process_mapper', ['form_id', 'version', 'tenant'])
    op.add_column('form_process_mapper', sa.Column('process_tenant', sa.String(), nullable=True,
                                                   comment='Tenant ID Mapped to process definition. This will be null for shared process definition.'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_form_version_uc', 'form_process_mapper', type_='unique')
    op.create_unique_constraint('_form_version_uc', 'form_process_mapper', ['form_id', 'version'])
    op.drop_column('form_process_mapper', 'process_tenant')
    # ### end Alembic commands ###
