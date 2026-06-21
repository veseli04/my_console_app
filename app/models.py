import uuid
from datetime import datetime

class BaseEntity:
    """Base class providing a unique identifier for all entities."""
    def __init__(self):
        self.id = str(uuid.uuid4())

class Item(BaseEntity):
    """Core domain entity representing managed project objects."""
    def __init__(self, title: str, description: str):
        super().__init__()
        self.title = title
        self.description = description
        self.created_at = datetime.utcnow().isoformat()

    def to_dict(self) -> dict:
        """Converts object attributes to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates an object instance from a dictionary."""
        item = cls(data["title"], data["description"])
        item.id = data["id"]
        item.created_at = data["created_at"]
        return item

