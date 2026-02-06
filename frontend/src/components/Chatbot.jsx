import { useState } from "react";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hi! Ask me about any Linux incident and I'll pull from the KB."
    }
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) {
      return;
    }
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: userMessage.content })
    }).then((res) => res.json());

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        content: response.answer,
        sources: response.sources
      }
    ]);
  };

  return (
    <section className="chat">
      <header className="section-header">
        <h2>RAG Chat Assistant</h2>
        <p>Ask a question and see knowledge sources from incidents and KB articles.</p>
      </header>
      <div className="chat-window">
        {messages.map((message, index) => (
          <div
            key={`${message.role}-${index}`}
            className={`bubble ${message.role}`}
          >
            <p>{message.content}</p>
            {message.sources && (
              <div className="sources">
                <span>Sources:</span>
                <ul>
                  {message.sources.map((source, idx) => (
                    <li key={idx}>{source.incident_id ?? source.category ?? "KB"}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask about disk usage or SSH errors..."
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />
        <button type="button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </section>
  );
}
