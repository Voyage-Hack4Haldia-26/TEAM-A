try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team A: Campus Helpdesk RAG", stack: "node" })
);

app.post("/api/ingest", (req, res) => {
  // TODO: Upload a document, chunk + embed it
  res.status(501).json({ error: "Not implemented", todo: "Upload a document, chunk + embed it" });
});

app.post("/api/ask", (req, res) => {
  // TODO: Body: {question} -> {answer, sources[]}
  res.status(501).json({ error: "Not implemented", todo: "Body: {question} -> {answer, sources[]}" });
});

app.get("/api/docs", (req, res) => {
  // TODO: List ingested documents
  res.status(501).json({ error: "Not implemented", todo: "List ingested documents" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team A server running on http://localhost:${PORT}`));
