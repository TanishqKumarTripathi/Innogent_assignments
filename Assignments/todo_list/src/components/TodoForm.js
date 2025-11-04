import React, { useState } from 'react';

function TodoForm({ addTask }) {
  const [task, setTask] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!task.trim()) {
      setError('Task name cannot be empty!');
      return;
    }
    addTask(task.trim());
    setTask('');
    setError('');
  };

  return (
    <form onSubmit={handleSubmit} className="d-flex mb-4">
      <input
        type="text"
        className="form-control me-2"
        placeholder="Enter task..."
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button type="submit" className="btn btn-primary">
        Add Task
      </button>
      {error && <small className="error-msg">{error}</small>}
    </form>
  );
}

export default TodoForm;
