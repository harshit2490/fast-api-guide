# Task model - Helps us to define the tables and connection to the database

from src.utils.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)

    ## One user can have multiple tasks (One-to-Many Relationship)
    ## ondelete - If the parent row (user_table.id) is deleted, the related rows in the child table (user_tasks) will also be deleted.
    user_id = Column(Integer, ForeignKey("user_table.id", ondelete = "CASCADE"))


