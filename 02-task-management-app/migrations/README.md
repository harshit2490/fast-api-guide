Generic single-database configuration.

### Create the migration folder

> > pip install alembic
> > alembic init migrations
> > migrations, alembic.ini, README files are created

### Edit env.py

from src.utils.settings import settings
from src.user.models import UserModel
from src.tasks.models import TaskModel
from src.utils.db import Base

1.  Set the DATABASE_URL environment variable
    config.set_main_option("sqlalchemy.url", settings.DB_CONNECTION_STRING)

2.  Add the models to env.py
    target_metadata = Base.metadata

### Create the migration

> > alembic revision --autogenerate -m "Initial revision"
> > alembic upgrade head

### To check if the migration is created

> > alembic history
