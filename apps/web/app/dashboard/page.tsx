"use client";

import { useEffect, useState } from "react";

export default function Dashboard() {

  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("/api/logs")
      .then(res => res.json())
      .then(setLogs);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>🧠 AI Boot Dashboard</h1>

      <table border={1}>
        <thead>
          <tr>
            <th>CPU</th>
            <th>GPU</th>
            <th>Success</th>
          </tr>
        </thead>

        <tbody>
          {logs.map((l, i) => (
            <tr key={i}>
              <td>{l.cpu}</td>
              <td>{l.gpu}</td>
              <td>{l.success}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
