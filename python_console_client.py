# python_console_client.py

import requests

BASE_URL = "http://127.0.0.1:8000"

def create_todo():
    text = input("Enter Todo Text: ")
    is_complete = input("Is Complete? (y/n): ").lower()
    
    if is_complete == 'y':
        is_complete = True
    elif is_complete == 'n':
        is_complete = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    response = requests.post(f"{BASE_URL}/todos/", json={"text": text, "is_complete": is_complete})
    if response.status_code == 200:
        print("Todo added successfully")

def delete_todo():
    todo_id = input("Enter Todo ID to delete: ")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    if response.status_code == 200:
        print("Todo deleted successfully")
    else:
        

if __name__ == "__main__":
    create_todo()
    delete_todo()