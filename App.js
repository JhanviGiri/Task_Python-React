//import { useEffect, useState } from "react";
//
//function App() {
//  const [tasks, setTasks] = useState([]);
//
//  useEffect(() => {
//    fetch("http://127.0.0.1:5000/api/tasks")
//      .then(res => res.json())
//      .then(data => setTasks(data));
//  }, []);
//
//  return (
//    <div>
//      <h2>Tasks</h2>
//      <ul>
//        {tasks.map(task => (
//          <li key={task.id}>{task.title}</li>
//        ))}
//      </ul>
//    </div>
//  );
//}
//
//export default App;
//


import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const loadTasks = () => {
    fetch("http://127.0.0.1:5000/api/tasks")
      .then(res => res.json())
      .then(data => setTasks(data));
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const addTask = () => {
    fetch("http://127.0.0.1:5000/api/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title })
    }).then(() => {
      setTitle("");
      loadTasks();
    });
  };

  return (
    <div>
      <h2>Tasks</h2>

      <input
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="Task title"
      />

      <button onClick={addTask}>Add</button>

      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
