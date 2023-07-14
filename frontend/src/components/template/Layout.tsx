import React, {ReactNode, useState} from "react";

import Header from "./Header";
import Sidebar from "./Sidebar";
import Footer from "./Footer";
import {Container} from "@mui/material";

type Props = {
    children: ReactNode;
}

const Layout = (props: Props) => {
    const {children} = props;

    const [open, setOpen] = useState<boolean>(false);

    const toggleDrawer = () => setOpen(!open);

    return (
        <>
            <Header toggleDrawer={toggleDrawer}/>
            <Sidebar open={open} toggleDrawer={toggleDrawer}/>
            <Container component="main" maxWidth="lg" sx={{height: "95vh"}}>
                {children}
            </Container>
            <Footer/>
        </>
    );
};

export default Layout;
