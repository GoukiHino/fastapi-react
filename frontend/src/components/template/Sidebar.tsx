import React from "react";
import {Link} from "react-router-dom";

import {Drawer, List, ListItem, ListItemButton, ListItemIcon, ListItemText} from "@mui/material";
import HomeIcon from "@mui/icons-material/Home";
import PeopleIcon from "@mui/icons-material/People";
import AssignmentIcon from "@mui/icons-material/Assignment";
import TaskIcon from "@mui/icons-material/Task";

type Props = {
    open: boolean;
    toggleDrawer: () => void;
}

const Sidebar = (props: Props) => {
    const {open, toggleDrawer} = props;

    return (
        <Drawer anchor="left" open={open} onClose={toggleDrawer}>
            <List sx={{width: 250}} onClick={toggleDrawer}>
                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/">
                        <ListItemIcon>
                            <HomeIcon/>
                        </ListItemIcon>
                        <ListItemText primary="Home"/>
                    </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/users">
                        <ListItemIcon>
                            <PeopleIcon/>
                        </ListItemIcon>
                        <ListItemText primary="User"/>
                    </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/projects">
                        <ListItemIcon>
                            <AssignmentIcon/>
                        </ListItemIcon>
                        <ListItemText primary="Project"/>
                    </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/tasks">
                        <ListItemIcon>
                            <TaskIcon/>
                        </ListItemIcon>
                        <ListItemText primary="Task"/>
                    </ListItemButton>
                </ListItem>
            </List>
        </Drawer>
    );
};

export default Sidebar;
