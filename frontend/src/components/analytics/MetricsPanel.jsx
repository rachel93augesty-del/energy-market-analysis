import React from "react";
import { Grid, Card, CardContent, Typography } from "@mui/material";

const MetricsPanel = ({ prices }) => {
  if (!prices.length) return null;

  const values = prices.map(p => p.Price);
  const avg = values.reduce((a, b) => a + b, 0) / values.length;
  const volatility =
    Math.sqrt(values.map(x => Math.pow(x - avg, 2))
      .reduce((a, b) => a + b, 0) / values.length);

  return (
    <Grid container spacing={3} sx={{ marginBottom: 3 }}>
      <Grid item xs={12} md={6}>
        <Card>
          <CardContent>
            <Typography variant="h6">Average Price</Typography>
            <Typography variant="h4">${avg.toFixed(2)}</Typography>
          </CardContent>
        </Card>
      </Grid>

      <Grid item xs={12} md={6}>
        <Card>
          <CardContent>
            <Typography variant="h6">Volatility (Std Dev)</Typography>
            <Typography variant="h4">{volatility.toFixed(2)}</Typography>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};

export default MetricsPanel;
