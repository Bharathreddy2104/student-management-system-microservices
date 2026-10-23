import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return (
    <main>
      <h1>Student Management System</h1>
      <p>Microservices project dashboard</p>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
