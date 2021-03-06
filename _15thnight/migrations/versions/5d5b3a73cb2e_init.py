"""init

Revision ID: 5d5b3a73cb2e
Revises:
Create Date: 2016-02-13 15:49:03.416645

"""

# revision identifiers, used by Alembic.
revision = '5d5b3a73cb2e'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects.postgresql import ENUM
import sqlalchemy as sa

try:
    from config import DATABASE_URL
except:
    from configdist import DATABASE_URL


def upgrade():
    role_column = sa.Column(
        'role', sa.Enum('admin', 'advocate', 'provider'), nullable=True)
    if DATABASE_URL[:8] == 'postgres':
        role_enum = ENUM(
            'admin', 'advocate', 'provider', name='pgenum', create_type=False)
        role_enum.create(op.get_bind(), checkfirst=False)
        role_column = sa.Column('role', role_enum)
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.Text(), nullable=False),
        sa.Column('phone_number', sa.String(length=20), nullable=False),
        sa.Column('shelter', sa.Boolean(), nullable=True),
        sa.Column('clothes', sa.Boolean(), nullable=True),
        sa.Column('food', sa.Boolean(), nullable=True),
        sa.Column('other', sa.Boolean(), nullable=True),
        role_column,
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_table(
        'alerts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('description', sa.String(length=200), nullable=False),
        sa.Column('shelter', sa.Boolean(), nullable=False),
        sa.Column('clothes', sa.Boolean(), nullable=False),
        sa.Column('food', sa.Boolean(), nullable=False),
        sa.Column('other', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'responses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('alert_id', sa.Integer(), nullable=True),
        sa.Column('message', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['alert_id'], ['alerts.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responses')
    op.drop_table('alerts')
    op.drop_table('users')
    ### end Alembic commands ###
