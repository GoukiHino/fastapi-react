import React, {ChangeEvent, FormEvent, useState} from "react";
import {useNavigate} from "react-router-dom";

import {Avatar, Box, Button, TextField, Typography} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";

import {login} from "../../api/login";

const LoginForm = () => {
    const navigate = useNavigate();

    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleUsername = (e: ChangeEvent<HTMLInputElement>) => setUsername(e.target.value);
    const handlePassword = (e: ChangeEvent<HTMLInputElement>) => setPassword(e.target.value);

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const result = await login(username, password);
        if (result) navigate("/");
    };

    return (
        <Box sx={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            height: "50vh"
        }}>
            <Avatar sx={{bgcolor: "primary.main"}}>
                <LockOutlinedIcon/>
            </Avatar>
            <Typography component="h1" variant="h5" sx={{my: 2}}>Login</Typography>
            <Box component="form" onSubmit={handleSubmit}>
                <TextField
                    id="username"
                    name="username"
                    label="Username"
                    fullWidth
                    required
                    sx={{mb: 2}}
                    onChange={handleUsername}
                />
                <TextField
                    id="password"
                    name="password"
                    label="Password"
                    type="password"
                    fullWidth
                    required
                    sx={{mb: 2}}
                    onChange={handlePassword}
                />
                <Button
                    variant="contained"
                    color="primary"
                    type="submit"
                    fullWidth
                >
                    Submit
                </Button>
            </Box>
        </Box>
    );
};

export default LoginForm;
