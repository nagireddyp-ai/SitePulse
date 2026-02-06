import { useEffect, useState } from "react";
import Dashboard from "./components/Dashboard.jsx";
import KnowledgeBase from "./components/KnowledgeBase.jsx";
import Chatbot from "./components/Chatbot.jsx";
import ITSMPanel from "./components/ITSMPanel.jsx";

const tabs = [
  { id: "dashboard", label: "Dashboard" },
  { id: "kb", label: "Knowledge Base" },
  { id: "chat", label: "Chatbot" },
  { id: "itsm", label: "ITSM Panel" }
];

export default function App() {
  const [activeTab, setActiveTab] = useState("dashboard");
  const [metrics, setMetrics] = useState(null);
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    fetch("/dashboard-metrics")
      .then((res) => res.json())
      .then(setMetrics)
      .catch(() => setMetrics(null));

    fetch("/incidents")
      .then((res) => res.json())
      .then((data) => setIncidents(data.incidents || []))
      .catch(() => setIncidents([]));
  }, []);

  return (
    <div className="app">
      <aside className="sidebar">
        <h1>SitePulse</h1>
        <p className="subtitle">Agentic IT Ops Platform</p>
        <nav>
          {tabs.map((tab) => (
            <button
              key={tab.id}
              className={activeTab === tab.id ? "active" : ""}
              onClick={() => setActiveTab(tab.id)}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </aside>
      <main className="content">
        {activeTab === "dashboard" && (
          <Dashboard metrics={metrics} incidents={incidents} />
        )}
        {activeTab === "kb" && <KnowledgeBase />}
        {activeTab === "chat" && <Chatbot />}
        {activeTab === "itsm" && <ITSMPanel incidents={incidents} />}
      </main>
    </div>
  );
}
