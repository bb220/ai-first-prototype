"use client";
import { useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setLoading(true);
    setInput("");

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();
    setMessages([...newMessages, { role: "assistant", content: data.response }]);
    setLoading(false);
  };

  return (
    <main className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">💸 Finance Copilot</h1>
      <div className="space-y-3 mb-6">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-3 rounded-md ${
              msg.role === "user" ? "bg-gray-100" : "bg-blue-100"
            }`}
          >
            <strong>{msg.role === "user" ? "You" : "Copilot"}:</strong> {msg.content}
          </div>
        ))}
        {loading && <div className="italic text-gray-500">Thinking...</div>}
      </div>
      <div className="flex gap-2">
        <input
          className="border border-gray-300 rounded w-full px-3 py-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask about your finances..."
        />
        <button
          onClick={sendMessage}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </main>
  );
}
