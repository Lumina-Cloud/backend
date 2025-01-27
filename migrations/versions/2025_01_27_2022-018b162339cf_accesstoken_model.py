"""Accesstoken model

Revision ID: 018b162339cf
Revises: 402ed25556f2
Create Date: 2025-01-27 20:22:47.237156

"""

from typing import Sequence, Union

from alembic import op
import fastapi_users_db_sqlalchemy
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "018b162339cf"
down_revision: Union[str, None] = "402ed25556f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "accesstoken",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("token"),
    )
    op.create_index(
        op.f("ix_accesstoken_created_at"), "accesstoken", ["created_at"], unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_accesstoken_created_at"), table_name="accesstoken")
    op.drop_table("accesstoken")
