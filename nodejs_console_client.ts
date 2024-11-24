// nodejs_console_client.ts

import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000";

async function createTodo() {
    const text = 'Sample Text';
    const is_complete = 'Sample is complete';
    try {
        const response = await axios.post(`${BASE_URL}/todos/`, { text, is_complete });
        console.log("Todo added successfully");
    } catch (error) {
        console.error("Error:", error.message);
    }
}

async function deleteTodo() {
    const todoId = 1;
    try {
        const response = await axios.delete(`${BASE_URL}/todos/${todoId}`);
        console.log("Todo deleted successfully");
    } catch (error) {
        console.error("Error:", error.message);
    }
}

createTodo();
deleteTodo();