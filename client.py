import requests
import json

API_BASE_URL = "http://127.0.0.1:8000"

def print_response(response):
    """Print response data in a formatted way."""
    if response.status_code in [200, 201]:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_item():
    """Send POST request to create a new item."""
    print("Enter item details:")
    name = input("Name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    brand = input("Brand: ")
    model = input("Model: ")
    release_year = int(input("Release Year: "))

    payload = {
        "name": name,
        "description": description,
        "price": price,
        "brand": brand,
        "model": model,
        "release_year": release_year
    }
    response = requests.post(f"{API_BASE_URL}/items", json=payload)
    print_response(response)

def read_all_items():
    """Send GET request to fetch all items."""
    response = requests.get(f"{API_BASE_URL}/items")
    print_response(response)

def read_item_by_id():
    """Send GET request to fetch an item by ID."""
    item_id = input("Enter item ID: ")
    response = requests.get(f"{API_BASE_URL}/items/{item_id}")
    print_response(response)

def update_item():
    """Send PUT request to update an item."""
    item_id = input("Enter item ID to update: ")
    print("Enter updated details:")
    name = input("Name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    brand = input("Brand: ")
    model = input("Model: ")
    release_year = int(input("Release Year: "))

    payload = {
        "name": name,
        "description": description,
        "price": price,
        "brand": brand,
        "model": model,
        "release_year": release_year
    }
    response = requests.put(f"{API_BASE_URL}/items/{item_id}", json=payload)
    print_response(response)

def delete_item():
    """Send DELETE request to delete an item."""
    item_id = input("Enter item ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/items/{item_id}")
    print_response(response)

def main():
    """Main menu for CRUD operations."""
    while True:
        print("\nMenu:")
        print("1. Create Item")
        print("2. Read All Items")
        print("3. Read Item by ID")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_item()
        elif choice == "2":
            read_all_items()
        elif choice == "3":
            read_item_by_id()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
