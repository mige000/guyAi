import { useState, useRef, useEffect } from "react";
import "./App.css";
import mascotGif from "./assets/guygif.gif";
import Dashboard from "./pages/Dashboard";
import Insights from "./pages/Insights";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);
  //const [currentPage, setCurrentPage] = useState("dashboard");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    try {
      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await res.json();
      const botMsg = { sender: "bot", text: data.reply };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
      const errorMsg = { sender: "bot", text: "⚠️ Error: Could not connect to the backend." };
      setMessages((prev) => [...prev, errorMsg]);
    }
  };


  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const [currentPage, setCurrentPage] = useState("dashboard");

  return (
    <>
      <header className="app-header">
        <div className="header-left">Tech Guy</div>
        <nav className="header-right">
          <button
            className={`nav-item ${currentPage === "dashboard" ? "active" : ""}`}
            onClick={() => setCurrentPage("dashboard")}
          >
            Dashboard
          </button>
          <button
            className={`nav-item ${currentPage === "insights" ? "active" : ""}`}
            onClick={() => setCurrentPage("insights")}
          >
            Insights
          </button>
          <button className="nav-item">Account</button>
        </nav>
      </header>

      <div className="page-container">
        {currentPage === "dashboard" && <Dashboard />}
        {currentPage === "insights" && <Insights />}
      </div>

      <div className="chat-container">
        <h1>GUY</h1>

        <div className="chat-box">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
          <div ref={chatEndRef}></div>
        </div>

        <div className="input-area">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Type your message..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
      <img src={mascotGif} alt="Chat Mascot" className="chat-mascot" />
      
    </>
  );
}

export default App;