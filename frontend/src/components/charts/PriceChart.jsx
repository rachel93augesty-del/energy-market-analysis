import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ReferenceLine,
  ResponsiveContainer,
  Brush
} from "recharts";

const PriceChart = ({ prices, changePoints, events }) => {
  return (
    <ResponsiveContainer width="100%" height={500}>
      <LineChart data={prices}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="Price" stroke="#1976d2" dot={false} />

        {/* Change Points */}
        {changePoints.map((cp, i) => (
          <ReferenceLine key={i} x={cp.Date} stroke="red" strokeDasharray="3 3" />
        ))}

        {/* Events */}
        {events.map((event, i) => (
          <ReferenceLine
            key={i}
            x={event.Date}
            stroke="green"
            label={event.Event}
          />
        ))}

        {/* Zoom / Range Selector */}
        <Brush dataKey="Date" height={30} stroke="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default PriceChart;
