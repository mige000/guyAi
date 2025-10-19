import { useState, useRef, useEffect } from "react";
import week1Data from "../week1.json";
import mascotGif from "../assets/guygif.gif";

function Dashboard() {
    const { inventory, budget, sales } = week1Data;


    const itemRevenues = sales.map((item) => ({
      product: item.product,
      revenue: item.current_price * item.units_sold,
    }));

    const totalSales = sales.reduce((sum, item) => sum + item.units_sold, 0);
    const totalRevenue = sales.reduce(
    (sum, item) => sum + item.current_price * item.units_sold,
    0
    );
    const totalInventory = inventory.reduce((sum, item) => sum + item.count, 0);
    const totalBudget = budget.total_weekly_budget;


  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

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
      const errorMsg = {
        sender: "bot",
        text: "Error",
      };
      setMessages((prev) => [...prev, errorMsg]);
    }
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <>

  <div className="dashboard-grid">
  <div className="revenue-box">
    <h2>Revenue</h2>
    <p className="metric-value">${totalRevenue.toLocaleString()}</p>
    {/* Revenue breakdown table here */}
  </div>

  <div className="sales-box">
    <h2>Sales</h2>
    <p className="metric-value">{totalSales.toLocaleString()} units</p>
    {/* Sales breakdown table here */}
  </div>

  <div className="metric-box">
    <h2>Inventory</h2>
    <p className="metric-value">{totalInventory.toLocaleString()} items</p>
    {/* Inventory table here */}
  </div>

  <div className="metric-box">
    <h2>Budget</h2>
    <p className="metric-value">${totalBudget.toLocaleString()}</p>
    {/* Budget breakdown table here */}
  </div>
</div>
    </>
  );
}

export default Dashboard;