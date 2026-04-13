from enum import Enum
from datetime import date
from dataclasses import dataclass

class TaskStatus(Enum):
    OPEN = "open"
    RESERVED = "reserved"
    FOR_REVIEW = "for_review"
    ISSUE = "issue"
    DONE = "done"

@dataclass
class User:
    id: int
    name: str

@dataclass
class Task:
    title: str
    description: str
    points: int
    due_date: date
    status: TaskStatus
    assignee: User

def create_task(title: str, description: str, points: int, due_date: date, 
                status: TaskStatus, assignee: User) -> Task:
    """Create a new task with the provided details."""
    return Task(
        title=title,
        description=description,
        points=points,
        due_date=due_date,
        status=status,
        assignee=assignee
    )