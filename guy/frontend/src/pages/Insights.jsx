// import React from "react";

// function Insights() {
//   return (
//     <div className="page-content">
//       <h2>Insights</h2>
//       <p>This page will show your business insights, analytics, and trends.</p>
//       <div className="recommendation-box">
//         <h2>Recommendations:</h2>
//       </div>
//     </div>
//   );
// }

// export default Insights;

import { useEffect, useState } from "react";
import "../App.css";

function Insights() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/api/insights")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="metric-box">Loading insights...</div>;
  if (!data) return <div className="metric-box">No data available</div>;

  return (
    <>
  <div className="insights-grid">
    <div className="metric-box">
        <h2>Dynamic Pricing</h2>
        {data.dynamic_pricing.map((item, index) => (
            <div key={index}>
                <strong>{item.item}</strong>: ${item.proposed_price}  
                <br />
                <em>{item.reasoning}</em>
            </div>
            ))}
        
    </div>

    <div className="metric-box">
        <h2>Wholesale Suggestion</h2>
        {/* <p className="metric-value">{data.return_wholesale_orders}</p> */}
        
        {Array.isArray(data.wholesale_suggestion) ? (
            data.wholesale_suggestion.map((item, index) => (
              <div key={index}>
                <strong>{item.item}</strong> — Order {item.order_qty}
                <br />
                <em>{item.reasoning}</em>
              </div>
            ))
          ) : (
            <p>No wholesale suggestions available.</p>
          )}
    </div>

    <div className="metric-box">
        <h2>Seasonal Suggestions</h2>
        {/* <p className="metric-value">{data.return_seasonal_items}</p> */}

        {Array.isArray(data.seasonal_suggestions) ? (
            data.seasonal_suggestions.map((item, index) => (
              <div key={index}>
                <strong>{item.item}</strong>: {item.reasoning}
              </div>
            ))
          ) : (
            <p>No seasonal suggestions available.</p>
          )}
    </div>

    {/* <div className="metric-box">
        <h2>Total Revenue</h2>
        <p className="metric-value">${data.revenue}</p>
    </div> */}
  </div>
    </>
  );
}

export default Insights;