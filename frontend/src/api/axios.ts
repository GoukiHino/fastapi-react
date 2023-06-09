import axios from "axios";

const BASE_URL = "http://localhost:8000";

export default axios.create({baseURL: BASE_URL})
export const authAxios = axios.create({
    baseURL: BASE_URL,
    headers: {"Authorization": `Bearer ${localStorage.getItem("appToken")}`}
})
