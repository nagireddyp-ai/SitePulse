import { useState } from "react";

const mockArticles = [
  {
    id: "kb-1001",
    title: "KB: Linux server disk usage spike",
    category: "Linux",
    summary: "Steps to resolve log rotation failures and reclaim disk space."
  },
  {
    id: "kb-1002",
    title: "KB: SSH authentication failing",
    category: "Linux",
    summary: "Fix PAM misconfiguration and restore SSH access safely."
  }
];

export default function KnowledgeBase() {
  const [query, setQuery] = useState("");
  const results = mockArticles.filter((article) =>
    article.title.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <section>
      <header className="section-header">
        <h2>Knowledge Base</h2>
        <p>Search generated playbooks and resolutions.</p>
      </header>
      <div className="search-row">
        <input
          type="search"
          placeholder="Search KB articles"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
        <button type="button">Filter</button>
      </div>
      <div className="panel">
        <ul className="list">
          {results.map((article) => (
            <li key={article.id}>
              <div>
                <strong>{article.title}</strong>
                <p>{article.summary}</p>
              </div>
              <span className="tag">{article.category}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
