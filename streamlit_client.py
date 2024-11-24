import streamlit as st
import requests

# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000"

def create_todo():
    text = st.text_input("Enter Todo:")
    is_complete = st.checkbox("Is Complete")
    if st.button("Add Todo"):
        response = requests.post(f"{FASTAPI_URL}/todos", json={"text": text, "is_complete": is_complete})
        if response.status_code == 200:
            st.success(response.json()["todo added"])
        else:
            st.error(f"Error: {response.text}")

def update_todo():
    todo_id = st.number_input("Enter Todo ID:")
    new_text = st.text_input("Enter New Text:")
    is_complete = st.checkbox("Is Complete")
    if st.button("Update Todo"):
        response = requests.put(f"{FASTAPI_URL}/todos/{todo_id}", json={"new_text": new_text, "is_complete": is_complete})
        if response.status_code == 200:
            st.success("Todo Updated")
        else:
            st.error(f"Error: {response.text}")

def delete_todo():
    todo_id = st.number_input("Enter Todo ID:")
    if st.button("Delete Todo"):
        response = requests.delete(f"{FASTAPI_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success(response.json()["todo deleted"])
        else:
            st.error(f"Error: {response.text}")

def main():
    st.title("FastAPI and Streamlit Todo App")

    menu = st.sidebar.selectbox("Menu", ["Create Todo", "Update Todo", "Delete Todo"])

    if menu == "Create Todo":
        create_todo()
    elif menu == "Update Todo":
        update_todo()
    elif menu == "Delete Todo":
        delete_todo()

if __name__ == "__main__":
    main()
