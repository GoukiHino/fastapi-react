import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";

import {createTheme, ThemeProvider, CssBaseline} from "@mui/material";
import {indigo, grey} from "@mui/material/colors";

import Layout from "./template/Layout";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import UserPage from "./pages/UserPage";
import ProjectPage from "./pages/ProjectPage";
import TaskPage from "./pages/TaskPage";

function App() {
    const theme = createTheme({
        palette: {
            primary: {
                main: indigo[500]
            },
            secondary: {
                main: grey[500]
            }
        }
    });

    return (
        <BrowserRouter>
            <ThemeProvider theme={theme}>
                <CssBaseline/>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/login" element={<LoginPage/>}/>
                    <Route path="/users" element={<UserPage/>}/>
                    <Route path="/projects" element={<ProjectPage/>}/>
                    <Route path="/tasks" element={<TaskPage/>}/>
                </Routes>
            </ThemeProvider>
        </BrowserRouter>
    );
}

export default App;
