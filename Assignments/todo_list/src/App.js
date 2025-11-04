import React, { useState, useEffect } from 'react';
import TodoForm from './components/TodoForm';
import TodoList from './components/TodoList';
import FinishedTasks from './components/FinishedTask';

function App() {
  const [todos, setTodos] = useState(() => {
    const saved = localStorage.getItem('todos');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTask = (text) => {
    const newTask = {
      id: Date.now(),
      text,
      isEditing: false,
      completed: false,
    };
    setTodos([...todos, newTask]);
  };

  const deleteTask = (id) => setTodos(todos.filter((t) => t.id !== id));

  const toggleComplete = (id) =>
    setTodos(
      todos.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t))
    );

  const toggleEdit = (id) =>
    setTodos(
      todos.map((t) => (t.id === id ? { ...t, isEditing: !t.isEditing } : t))
    );

  const saveTask = (id, newText) =>
    setTodos(
      todos.map((t) =>
        t.id === id ? { ...t, text: newText, isEditing: false } : t
      )
    );

  return (
    <div className="container mt-5">
      <div className="card shadow p-4 bg-dark text-light">
        <h1 className="text-center mb-4">📝 React To-Do List</h1>
        <TodoForm addTask={addTask} />

        <div className="row mt-4">
          <div className="col-md-6">
            <h4>Active Tasks</h4>
            <TodoList
              todos={todos.filter((t) => !t.completed)}
              deleteTask={deleteTask}
              toggleEdit={toggleEdit}
              saveTask={saveTask}
              toggleComplete={toggleComplete}
            />
          </div>
          <div className="col-md-6">
            <h4>Finished Tasks</h4>
            <FinishedTasks todos={todos.filter((t) => t.completed)} deleteTask={deleteTask}/>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
