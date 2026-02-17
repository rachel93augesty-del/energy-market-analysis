import React from "react";
import { Container, Grid, Paper } from "@mui/material";

const DashboardLayout = ({ children }) => {
  return (
    <Container maxWidth="xl" sx={{ marginTop: 4 }}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper elevation={3} sx={{ padding: 3 }}>
            {children}
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default DashboardLayout;
