const express = require("express");
const path= require("path")

const app= express();
const PORT=3000;
const BACKEND_URL= process.env.BACKEND_URL || "http://localhost:5000";

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

// send data here, and we forward it to the backend
app.post("/submit", async (req, res) => { 
    try {
        const response = await fetch(`${BACKEND_URL}/submit`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(req.body)
        });
        const data = await response.json();
        res.status(response.status).json(data);
        
    } catch (error) {
        console.error("Could not reach backend:", error.message);
        res.status(500).json({ success: false, error: "Backend is not reachable" });
    }
});

app.listen(PORT,"0.0.0.0", () => {
    console.log(`Frontend server is running on port ${PORT}, backend at ${BACKEND_URL}`);
});
