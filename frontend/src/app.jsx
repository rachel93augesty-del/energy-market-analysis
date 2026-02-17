import React, { useEffect, useState } from "react";
import DashboardLayout from "./components/layout/DashboardLayout";
import Header from "./components/layout/Header";
import PriceChart from "./components/charts/PriceChart";
import MetricsPanel from "./components/analytics/MetricsPanel";
import DateFilter from "./components/filters/DateFilter";
import { getPrices, getChangePoints, getEvents } from "./services/api";

function App() {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const start = startDate ? startDate.toISOString() : null;
      const end = endDate ? endDate.toISOString() : null;

      setPrices(await getPrices(start, end));
      setChangePoints(await getChangePoints());
      setEvents(await getEvents());
    };

    fetchData();
  }, [startDate, endDate]);

  return (
    <DashboardLayout>
      <Header />
      <DateFilter
        startDate={startDate}
        endDate={endDate}
        setStartDate={setStartDate}
        setEndDate={setEndDate}
      />
      <MetricsPanel prices={prices} />
      <PriceChart
        prices={prices}
        changePoints={changePoints}
        events={events}
      />
    </DashboardLayout>
  );
}

export default App;
