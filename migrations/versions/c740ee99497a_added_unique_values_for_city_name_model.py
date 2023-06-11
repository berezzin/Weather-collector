"""Added unique values for City.name model

Revision ID: c740ee99497a
Revises: d40f260fed81
Create Date: 2023-06-11 21:13:27.979442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c740ee99497a'
down_revision = 'd40f260fed81'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'city', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'city', type_='unique')
    # ### end Alembic commands ###
