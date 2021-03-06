"""added tables

Revision ID: 5e55f12f083b
Revises: 
Create Date: 2021-03-02 22:13:06.030541

"""
import geoalchemy2
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e55f12f083b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('zipcode', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_numbers', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('telegram', sa.String(), nullable=True),
    sa.Column('facebook', sa.String(), nullable=True),
    sa.Column('roles', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stadium_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('long', sa.Float(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT,4326', from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stadium',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('long', sa.Float(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT,4326', from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('stadium_group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stadium_group_id'], ['stadium_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stadium_image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('order_number', sa.Integer(), nullable=True),
    sa.Column('is_default', sa.Boolean(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('stadium_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stadium_id'], ['stadium.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('stadium_image')
    op.drop_table('stadium')
    op.drop_table('stadium_group')
    op.drop_table('user')
    op.drop_table('address')
    # ### end Alembic commands ###
