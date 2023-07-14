import React from "react";
import {Link} from "react-router-dom";

import {AppBar, IconButton, Toolbar, Typography} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import LoginIcon from "@mui/icons-material/Login";

type Props = {
    toggleDrawer: () => void;
}

const Header = (props: Props) => {
    const {toggleDrawer} = props;

    return (
        <AppBar component="header" position="static">
            <Toolbar>
                <IconButton sx={{mr: 2, color: "inherit"}} onClick={toggleDrawer}>
                    <MenuIcon/>
                </IconButton>
                <Typography variant="h6" sx={{flexGrow: 1}}>App</Typography>
                <IconButton sx={{color: "inherit"}} component={Link} to="/login">
                    <LoginIcon/>
                </IconButton>
            </Toolbar>
        </AppBar>
    );
};

export default Header;
