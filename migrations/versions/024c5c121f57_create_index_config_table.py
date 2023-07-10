"""create index_config table

Revision ID: 024c5c121f57
Revises: 111f4f3af57b
Create Date: 2023-07-10 09:14:24.246861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024c5c121f57'
down_revision = '111f4f3af57b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vector_index_config',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('vector_index_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vector_index_config')
    # ### end Alembic commands ###