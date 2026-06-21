import os
from app.repository import JsonRepository
from app.service import ItemService

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "storage.json")
    
    repository = JsonRepository(db_path)
    service = ItemService(repository)

    while True:
        print("\n=== Console Management System ===")
        print("1. View All Items")
        print("2. Add New Item")
        print("3. Search Items by Title")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            items = repository.get_all()
            if not items:
                print("No items found.")
            for item in items:
                print(f"ID: {item.id} | Title: {item.title} | Desc: {item.description}")

        elif choice == "2":
            title = input("Enter item title: ")
            description = input("Enter item description: ")
            try:
                new_item = service.create_item(title, description)
                print(f"Success! Created item with ID: {new_item.id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            results = service.search_by_title(keyword)
            print(f"\nFound {len(results)} results:")
            for item in results:
                print(f"- {item.title} (ID: {item.id})")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
