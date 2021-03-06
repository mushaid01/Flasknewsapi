"""empty message

Revision ID: 2b4fdb2c00eb
Revises: 
Create Date: 2022-06-02 03:47:32.043822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b4fdb2c00eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('desc_en', sa.String(length=1000), nullable=True),
    sa.Column('source', sa.String(length=100), nullable=True),
    sa.Column('news_id', sa.String(length=100), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('timestamp', sa.String(length=100), nullable=True),
    sa.Column('title_en', sa.String(length=500), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_data')
    # ### end Alembic commands ###
