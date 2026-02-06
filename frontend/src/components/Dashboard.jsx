export default function Dashboard({ metrics, incidents }) {
  return (
    <section>
      <header className="section-header">
        <h2>Operations Dashboard</h2>
        <p>Live view of incident volume, SLA risk, and priority distribution.</p>
      </header>
      <div className="cards">
        <div className="card">
          <h3>Total Incidents</h3>
          <span>{metrics?.total_incidents ?? "--"}</span>
        </div>
        <div className="card">
          <h3>Open</h3>
          <span>{metrics?.open ?? "--"}</span>
        </div>
        <div className="card">
          <h3>Resolved</h3>
          <span>{metrics?.resolved ?? "--"}</span>
        </div>
        <div className="card">
          <h3>SLA Breaches</h3>
          <span>{metrics?.sla_breaches ?? "--"}</span>
        </div>
      </div>

      <div className="grid">
        <div className="panel">
          <h3>Priority Distribution</h3>
          {metrics ? (
            <ul className="bars">
              {Object.entries(metrics.priority_distribution).map(([key, value]) => (
                <li key={key}>
                  <span>{key}</span>
                  <div className="bar">
                    <div style={{ width: `${(value / metrics.total_incidents) * 100}%` }} />
                  </div>
                  <strong>{value}</strong>
                </li>
              ))}
            </ul>
          ) : (
            <p>Loading metrics…</p>
          )}
        </div>
        <div className="panel">
          <h3>Recent Incidents</h3>
          <ul className="list">
            {incidents.slice(0, 4).map((incident) => (
              <li key={incident.id}>
                <div>
                  <strong>{incident.title}</strong>
                  <p>{incident.description}</p>
                </div>
                <span className={`status ${incident.status.replace(" ", "-").toLowerCase()}`}>
                  {incident.status}
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
