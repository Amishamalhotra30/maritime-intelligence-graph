import "./App.css";
import { useState } from "react";

import Dashboard from "./pages/Dashboard";
import GraphPage from "./pages/GraphPage";
import AnalyticsPage from "./pages/AnalyticsPage";

function App() {

  const [page, setPage] =
    useState("dashboard");

  return (

    <div>

      <div className="sidebar">

        <button
          onClick={() =>
            setPage("dashboard")
          }
        >
          Dashboard
        </button>

        <button
          onClick={() =>
            setPage("graph")
          }
        >
          Graph Explorer
        </button>

        <button
          onClick={() =>
            setPage("analytics")
          }
        >
          Analytics
        </button>

      </div>

      <div className="content">

        {page === "dashboard" &&
          <Dashboard />}

        {page === "graph" &&
          <GraphPage />}

        {page === "analytics" &&
          <AnalyticsPage />}

      </div>

    </div>

  );
}

export default App;