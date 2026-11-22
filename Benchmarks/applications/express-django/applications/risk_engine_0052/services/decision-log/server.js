const express = require("express");
const session = require("express-session");
const multer = require("multer");

const recordDecision = require("./decision_record").recordDecision;
const renderPolicy = require("./render_policy").renderPolicy;
const formatBatch = require("./format_batch").formatBatch;
const pruneReceipt = require("./prune_receipt").pruneReceipt;
const normalizeBatch = require("./normalize_batch").normalizeBatch;
const auditWindow = require("./audit_window").auditWindow;
const resolveWindow = require("./resolve_window").resolveWindow;
const rotateCase = require("./rotate_case").rotateCase;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/recordDecision", recordDecision);
app.post("/renderPolicy", renderPolicy);
app.post("/formatBatch", formatBatch);
app.post("/pruneReceipt", pruneReceipt);
app.post("/normalizeBatch", normalizeBatch);
app.post("/auditWindow", auditWindow);
app.post("/resolveWindow", resolveWindow);
app.post("/rotateCase", rotateCase);

app.listen(3000, "0.0.0.0");
