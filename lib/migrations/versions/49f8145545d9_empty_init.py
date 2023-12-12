"""Empty Init

Revision ID: 49f8145545d9
Revises: 197e8a22f52a
Create Date: 2023-12-12 13:04:38.708641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49f8145545d9'
down_revision: Union[str, None] = '197e8a22f52a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
