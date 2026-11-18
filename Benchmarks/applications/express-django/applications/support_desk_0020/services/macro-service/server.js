const express = require("express");
const session = require("express-session");

const applyMacro = require("./macro_apply").applyMacro;
const publishEscalation = require("./publish_escalation").publishEscalation;
const normalizeDigest = require("./normalize_digest").normalizeDigest;
const fetchRoster = require("./fetch_roster").fetchRoster;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const buildReceipt = require("./build_receipt").buildReceipt;
const exportReport = require("./export_report").exportReport;
const renderThreshold = require("./render_threshold").renderThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/applyMacro", route(applyMacro));
app.post("/publishEscalation", route(publishEscalation));
app.post("/normalizeDigest", route(normalizeDigest));
app.post("/fetchRoster", route(fetchRoster));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/buildReceipt", route(buildReceipt));
app.post("/exportReport", route(exportReport));
app.post("/renderThreshold", route(renderThreshold));

app.listen(3000, "0.0.0.0");
