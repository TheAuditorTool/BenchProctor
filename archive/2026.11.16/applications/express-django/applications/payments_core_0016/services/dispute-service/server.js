const express = require("express");
const session = require("express-session");

const openDispute = require("./dispute_open").openDispute;
const rotateRoster = require("./rotate_roster").rotateRoster;
const annotateReport = require("./annotate_report").annotateReport;
const auditLedger = require("./audit_ledger").auditLedger;
const enrichRoster = require("./enrich_roster").enrichRoster;
const formatWindow = require("./format_window").formatWindow;
const fetchPolicy = require("./fetch_policy").fetchPolicy;
const fetchManifest = require("./fetch_manifest").fetchManifest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/openDispute", route(openDispute));
app.post("/rotateRoster", route(rotateRoster));
app.post("/annotateReport", route(annotateReport));
app.post("/auditLedger", route(auditLedger));
app.post("/enrichRoster", route(enrichRoster));
app.post("/formatWindow", route(formatWindow));
app.post("/fetchPolicy", route(fetchPolicy));
app.post("/fetchManifest", route(fetchManifest));

app.listen(3000, "0.0.0.0");
