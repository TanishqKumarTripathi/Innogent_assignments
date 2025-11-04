import React from 'react';

function FinishedTasks({ todos, deleteTask }) {
  if (todos.length === 0)
    return <p className="text-muted">No finished tasks yet!</p>;

  return (
    <>
      {todos.map((todo) => (
        <div key={todo.id} className="card mb-3 border-success shadow-sm">
          <div className="card-body d-flex justify-content-between align-items-center">
            <span style={{ textDecoration: 'line-through', color: '#6c757d' }}>
              {todo.text}
            </span>
            <button
              className="btn btn-danger btn-sm"
              onClick={() => deleteTask(todo.id)}
            >
              Delete
            </button>
          </div>
        </div>
      ))}
    </>
  );
}

export default FinishedTasks;

