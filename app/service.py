from typing import List
from app.models import Item
from app.repository import JsonRepository

class ItemService:
    """Contains business logic and performs validation before data operations."""
    def __init__(self, repository: JsonRepository):
        self.repository = repository

    def create_item(self, title: str, description: str) -> Item:
        if not title or title.strip() == "":
            raise ValueError("Title cannot be empty or whitespace.")
        
        new_item = Item(title=title.strip(), description=description.strip())
        self.repository.add(new_item)
        return new_item

    def search_by_title(self, keyword: str) -> List[Item]:
        all_items = self.repository.get_all()
        return [item for item in all_items if keyword.lower() in item.title.lower()]

