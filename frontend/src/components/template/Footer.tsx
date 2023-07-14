import React from "react";
import {Typography} from "@mui/material";

const Footer = () => {
    return (
        <Typography variant="body2" align="center">
           Copyright &copy; {new Date().getFullYear()} i5net.
        </Typography>
    );
};

export default Footer;
