import axios from "../api/axios";

export const login = async (username: string, password: string) => {
    const data = new FormData();

    data.append("username", username);
    data.append("password", password);

    return await axios.post("/login", data)
        .then((res) => {
            localStorage.setItem("appToken", res.data.access_token);
            return true;
        }).catch((err) => {
            alert(err.response.data.detail);
            return false;
        });
};
