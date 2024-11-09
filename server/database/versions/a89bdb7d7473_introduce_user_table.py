"""Introduce User Table

Revision ID: a89bdb7d7473
Revises: 
Create Date: 2024-11-09 16:06:25.450707

"""

import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a89bdb7d7473"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True,
        ),
        sa.Column("nick_name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=True),
        sa.Column("last_name", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.now(),
        ),
    )
    op.create_unique_constraint("unique_email", "user", ["email"])


def downgrade() -> None:
    op.drop_constraint("unique_email", "user", type_="unique")
    op.drop_table("user")
