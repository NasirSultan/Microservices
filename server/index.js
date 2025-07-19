const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/api/chat", async (req, res) => {
  const { message } = req.body;

  try {
    
    const aiResponse = await axios.post("http://langchain-api:8000/generate", {
      message,
    });

    res.json({
      user: message,
      ai: aiResponse.data.response,
    });
  } catch (error) {
    console.error("Error calling AI service:", error.message);
    res.status(500).json({ error: "AI service failed." });
  }
});

app.listen(5000, () => console.log("Node.js server running on port 5000"));
