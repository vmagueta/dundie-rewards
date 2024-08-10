"""hash_passwords

Revision ID: d0bc3fc49feb
Revises: 63699c03d253
Create Date: 2024-08-10 15:20:15.449869

"""
from typing import Sequence, Union

from alembic import op
from dundie.models import User
from dundie.utils.user import get_password_hash, verify_password
from sqlmodel import Session, select


# revision identifiers, used by Alembic.
revision: str = 'd0bc3fc49feb'
down_revision: Union[str, None] = '63699c03d253'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    users = session.exec(
        select(User).where(
            ~User.password.like("$argon%")
        )
    )
    for user in users:
        plain = user.password
        hashed = get_password_hash(plain)
        if verify_password(plain, hashed):
            user.password = hashed
            session.add(user)

    session.commit()


def downgrade() -> None:
    pass
