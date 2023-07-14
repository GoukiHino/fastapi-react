import React from "react";

import Footer from "../template/Footer";
import LoginForm from "../login/LoginForm";
import {Container} from "@mui/material";

const LoginPage = () => {
    return (
        <>
            <Container component="main" maxWidth="xs">
                <LoginForm/>
            </Container>
            <Footer/>
        </>
    );
};

export default LoginPage;
