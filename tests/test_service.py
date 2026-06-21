import unittest
from unittest.mock import MagicMock
from app.service import ItemService

class TestItemService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = ItemService(self.mock_repo)

    def test_create_item_success(self):
        item = self.service.create_item("Test Title", "Test Description")
        self.assertEqual(item.title, "Test Title")
        self.mock_repo.add.assert_called_once()

    def test_create_item_empty_title_throws_error(self):
        with self.assertRaises(ValueError):
            self.service.create_item("", "Some description")

if __name__ == "__main__":
    unittest.main()
