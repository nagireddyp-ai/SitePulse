import { useState } from "react";

export default function ITSMPanel({ incidents }) {
  const [selected, setSelected] = useState(incidents[0] || null);

  return (
    <section>
      <header className="section-header">
        <h2>ITSM Panel</h2>
        <p>Track tickets, simulate ServiceNow updates, and resolve incidents.</p>
      </header>
      <div className="itsm-grid">
        <div className="panel">
          <h3>Incident Queue</h3>
          <ul className="list">
            {incidents.map((incident) => (
              <li key={incident.id} onClick={() => setSelected(incident)}>
                <div>
                  <strong>{incident.title}</strong>
                  <p>{incident.description}</p>
                </div>
                <span className="tag">{incident.priority}</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="panel detail">
          <h3>Ticket Detail</h3>
          {selected ? (
            <div className="detail-body">
              <p className="detail-title">{selected.title}</p>
              <p>{selected.description}</p>
              <div className="detail-metadata">
                <span>Status: {selected.status}</span>
                <span>Priority: {selected.priority}</span>
                <span>SLA: {selected.sla_timer}h</span>
              </div>
              <button type="button">Update Status</button>
            </div>
          ) : (
            <p>Select an incident to view details.</p>
          )}
        </div>
      </div>
    </section>
  );
}
