import React from "react";
import { Typography } from "@mui/material";

const Header = () => {
  return (
    <>
      <Typography variant="h4" gutterBottom>
        Brent Oil Market Analysis Dashboard
      </Typography>
      <Typography variant="subtitle1" color="text.secondary">
        Interactive analysis of historical price movements and geopolitical events
      </Typography>
    </>
  );
};

export default Header;
