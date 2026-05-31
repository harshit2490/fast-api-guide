# Controller handles the business logic - Perform operations on the task data
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel

def create_task(body:TaskSchema, db: Session, user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], 
                         description = data["description"], 
                         is_completed = data["is_completed"], 
                         user_id = user.id) 
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db: Session, user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    if not tasks:
        raise HTTPException(404, detail="No tasks found")
    return tasks


def get_one_task(task_id: int, db: Session, user: UserModel):
    one_task:TaskModel = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")

    if one_task.user_id != user.id:
        raise HTTPException(401, detail="You are not authorized to get this task")
        
    return one_task


def update_task(body:TaskSchema, task_id: int, db: Session, user: UserModel):
    one_task:TaskModel = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")
    
    if one_task.user_id != user.id:
        raise HTTPException(401, detail="You are not authorized to update this task")

    data = body.model_dump()
    for field, value in data.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task


def delete_task(task_id: int, db: Session, user: UserModel):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")

    if one_task.user_id != user.id:
        raise HTTPException(401, detail="You are not authorized to delete this task")

    db.delete(one_task)
    db.commit()
    return None