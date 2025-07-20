// server.js
const express = require("express");
const axios = require("axios");
const pdf = require("pdf-parse");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());

// Convert Google Drive "view" link to direct download
const convertToDirectLink = (url) => {
  const match = url.match(/\/file\/d\/(.*?)\//);
  if (match && match[1]) {
    return `https://drive.google.com/uc?id=${match[1]}&export=download`;
  }
  return null;
};

app.get("/api/fetch-text", async (req, res) => {
  const { url } = req.query;
  if (!url) return res.status(400).json({ error: "Missing ?url param" });

  const directUrl = convertToDirectLink(url);
  if (!directUrl) return res.status(400).json({ error: "Invalid Google Drive URL" });

  try {
    const response = await axios.get(directUrl, { responseType: "arraybuffer" });
    const text = await pdf(response.data);
    res.json({ text: text.text });
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch or parse PDF", details: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
