import os
import json
from typing import List, Optional
from app.models import Item

class JsonRepository:
    """Handles data persistence using a local JSON file architecture."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_all(self) -> List[dict]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_all(self, data: List[dict]):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_all(self) -> List[Item]:
        raw_data = self._load_all()
        return [Item.from_dict(d) for d in raw_data]

    def get_by_id(self, entity_id: str) -> Optional[Item]:
        items = self.get_all()
        for item in items:
            if item.id == entity_id:
                return item
        return None

    def add(self, item: Item) -> None:
        items_dict = self._load_all()
        items_dict.append(item.to_dict())
        self._save_all(items_dict)

    def delete(self, entity_id: str) -> bool:
        items_dict = self._load_all()
        initial_count = len(items_dict)
        items_dict = [d for d in items_dict if d["id"] != entity_id]
        
        if len(items_dict) < initial_count:
            self._save_all(items_dict)
            return True
        return False

