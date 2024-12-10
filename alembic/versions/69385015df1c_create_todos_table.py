"""create todos table

Revision ID: 69385015df1c
Revises: 
Create Date: 2024-12-10 14:13:09.295749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69385015df1c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        create table todos (
            id bigserial primary key,
            name text,
            completed boolean not null default false
        );
    """)


def downgrade():
    op.execute("drop table todos;")