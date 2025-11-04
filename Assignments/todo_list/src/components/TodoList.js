import React, { useState } from 'react';

function TodoList({ todos, deleteTask, toggleEdit, saveTask, toggleComplete }) {
  const [editTextMap, setEditTextMap] = useState({});

  const handleChange = (id, value) => {
    setEditTextMap({ ...editTextMap, [id]: value });
  };

  return (
    <>
      {todos.map((todo) => (
        <div key={todo.id} className="card mb-3 shadow-sm">
          <div className="card-body d-flex justify-content-between align-items-center">
            {todo.isEditing ? (
              <>
                <input
                  type="text"
                  className="form-control me-2"
                  value={
                    editTextMap[todo.id] !== undefined
                      ? editTextMap[todo.id]
                      : todo.text
                  }
                  onChange={(e) => handleChange(todo.id, e.target.value)}
                />
                <button
                  className="btn btn-success btn-sm"
                  onClick={() => {
                    if (!editTextMap[todo.id]?.trim()) {
                      alert('Task name cannot be empty!');
                      return;
                    }
                    saveTask(todo.id, editTextMap[todo.id]);
                    setEditTextMap({ ...editTextMap, [todo.id]: undefined });
                  }}
                >
                  Save
                </button>
              </>
            ) : (
              <>
                <div className="d-flex align-items-center">
                  <input
                    type="checkbox"
                    className="form-check-input me-2"
                    checked={todo.completed}
                    onChange={() => toggleComplete(todo.id)}
                  />
                  <span
                    style={{
                      textDecoration: todo.completed ? 'line-through' : 'none',
                      color: todo.completed ? '#6c757d' : '#f1f1f1',
                    }}
                  >
                    {todo.text}
                  </span>
                </div>
                <div>
                  <button
                    className="btn btn-warning btn-sm me-2"
                    onClick={() => toggleEdit(todo.id)}
                  >
                    Edit
                  </button>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => deleteTask(todo.id)}
                  >
                    Delete
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      ))}
    </>
  );
}

export default TodoList;
