"""removed unique constraint from movie title

Revision ID: eb2fae58520a
Revises: afaa5a1f6ef3
Create Date: 2022-09-08 22:55:21.969245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb2fae58520a'
down_revision = 'afaa5a1f6ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_movie_title', table_name='movie')
    op.create_index(op.f('ix_movie_title'), 'movie', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movie_title'), table_name='movie')
    op.create_index('ix_movie_title', 'movie', ['title'], unique=False)
    # ### end Alembic commands ###